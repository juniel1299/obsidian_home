## 'use client' , 언제 붙여야 할까 ?

[Page Router vs App Router](https://problem-child.tistory.com/124) 글에서 App Router 의 핵심이 서버 컴포넌트라고 짧게 정리했다.
그런데 막상 쓰다 보면 이런 질문이 생긴다.

- 클라이언트 컴포넌트는 브라우저에서만 실행될까 ?
- 왜 함수를 props 로 넘기면 에러가 날까 ?
- 클라이언트 컴포넌트 안에 서버 컴포넌트를 넣을 수 있을까 ?

이번 글은 둘의 차이를 **동작 원리부터** 정리한다.

고깃집으로 생각하면 쉽다.

- **서버 컴포넌트** : 주방에서 완성해서 나오는 요리. 손님은 **결과만** 받고, 레시피는 모른다
- **클라이언트 컴포넌트** : 불판에서 손님이 직접 굽는 고기. 주방에서 **밑작업**을 하고, 테이블에서 **마저 굽는다**

---

## 제일 흔한 오해

> 서버 컴포넌트 = 서버에서 실행 , 클라이언트 컴포넌트 = 브라우저에서 실행 ❌

틀린 말이다.
**클라이언트 컴포넌트도 서버에서 실행된다.**

직접 확인해 봤다.

```jsx
// app/Counter.js
"use client";

import { useState } from "react";

export default function Counter({ initial }) {
  const [count, setCount] = useState(initial);
  console.log("Counter 실행");

  return <button onClick={() => setCount(count + 1)}>count: {count}</button>;
}
```

```jsx
// app/page.js (use client 가 없으니 서버 컴포넌트)
import Counter from "./Counter";

export default async function Page() {
  console.log("Page 실행");

  return (
    <main>
      <h1>오늘의 메뉴</h1>
      <Counter initial={10} />
    </main>
  );
}
```

`next build` 를 하면 터미널에 **둘 다** 찍힌다.

```
Page 실행
Counter 실행
```

완성된 HTML 에도 `count: 10` 이 이미 들어 있다.
불판 위 고기도 주방에서 밑작업을 해서 내보내는 것이다.

정확한 구분은 이렇다.

- **서버 컴포넌트** : 서버에서**만** 실행된다
- **클라이언트 컴포넌트** : 서버에서 HTML 을 만들 때도 실행되고, **브라우저에서도** 실행된다

그래서 이름이 조금 헷갈린다. "브라우저 전용" 이 아니라 **"브라우저까지 가는"** 컴포넌트다.

---

## 서버 컴포넌트 : 주방에서 완성

App Router 에서는 **아무것도 안 붙이면 서버 컴포넌트**다.

```jsx
// app/posts/page.js
import { db } from "./db";

export default async function PostsPage() {
  const posts = await db.post.findMany();  // DB 에 바로 접근

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

할 수 있는 것

- `async / await` 로 컴포넌트에서 바로 데이터 가져오기
- DB , 파일 , 비밀 환경변수 같은 **서버 자원**에 직접 접근
- 큰 라이브러리를 써도 **브라우저로 코드가 안 간다**

할 수 없는 것

- `useState` , `useEffect` 같은 상태 / 생명주기 Hook
- `onClick` 같은 이벤트 핸들러
- `window` , `localStorage` 같은 브라우저 API

주방에서 나간 요리는 **이미 완성품**이다.
테이블에서 다시 조리할 수 없으니, 상태도 이벤트도 없다.

### 언제 실행될까

페이지 종류에 따라 다르다.

- **Static 페이지** : **빌드할 때** 실행해서 결과를 저장해 둔다
- **Dynamic 페이지** : **요청이 올 때마다** 실행한다

위 예제의 `Page 실행` 이 `next build` 에서 찍힌 것도 Static 페이지였기 때문이다.

---

## 클라이언트 컴포넌트 : 불판에서 마저 굽기

파일 최상단에 `"use client"` 를 쓰면 된다.

할 수 있는 것

- `useState` , `useEffect` , `useRef` 등 Hook
- `onClick` , `onChange` 같은 이벤트
- `window` , `localStorage` 같은 브라우저 API

대신 **코드가 JS Bundle 에 포함되어 브라우저로 간다.**

위 예제를 빌드해서 브라우저로 가는 파일 (`.next/static`) 을 검색해 보면

| 검색어 | 결과 |
|---|---|
| `Counter 실행` (클라이언트) | 있음 |
| `Page 실행` (서버) | **없음** |

서버 컴포넌트의 코드는 브라우저로 **아예 가지 않는다.**
쓸수록 Bundle 이 줄어드는 이유가 이것이다.

---

## 렌더링 순서

페이지에 처음 들어가면 이렇게 진행된다.

```
[서버]
1. 서버 컴포넌트 실행 → RSC Payload 생성
2. RSC Payload + 클라이언트 컴포넌트 → HTML 생성

[브라우저]
3. HTML 표시 (아직 버튼은 안 눌림)
4. JS Bundle 다운로드
5. 하이드레이션 : 클라이언트 컴포넌트에 이벤트 연결 (이제 버튼이 눌림)
```

(SSR 과 CSR 이 낯설다면 [SSR vs CSR](https://problem-child.tistory.com/118) 글을 먼저 보고 오면 좋습니다)

### RSC Payload 란

서버 컴포넌트의 **실행 결과를 직렬화한 데이터**다.
위 예제를 빌드한 파일을 보기 좋게 줄이면 이런 모양이다.

```
["$","main",null,{"children":[
  ["$","h1",null,{"children":"오늘의 메뉴"}],
  ["$","$L12",null,{"initial":10}]
]}]
```

- `h1` 은 **결과 그대로** 들어 있다 (주방에서 완성된 요리)
- `$L12` 는 **"여기에 클라이언트 컴포넌트가 들어간다"** 는 자리 표시다
- `initial: 10` 은 그 컴포넌트에게 넘길 **props** 다

주문서에 "완성 요리는 여기 , 이 자리엔 불판 , 고기는 10인분" 이라고 적혀 있는 셈이다.

### 페이지 이동할 때는 다르다

`Link` 로 이동하면 HTML 을 처음부터 받지 않는다.
**RSC Payload 를 받아서** 화면을 갱신하고, 클라이언트 컴포넌트는 브라우저에서 실행된다.

그래서 "클라이언트 컴포넌트는 무조건 2번 실행" 은 첫 진입 기준의 이야기다.
그 뒤에는 상태가 바뀔 때마다 브라우저에서 다시 실행된다.

---

## 경계 규칙 3가지

### 1. "use client" 는 경계선이다

`"use client"` 는 그 파일 하나만 바꾸는 표시가 아니다.
**그 파일이 import 하는 모든 것이 클라이언트 쪽으로 넘어간다.**

```jsx
// app/Plain.js ("use client" 없음)
export default function Plain() {
  return <p>일반 컴포넌트</p>;
}
```

```jsx
// app/Wrap.js
"use client";

import Plain from "./Plain";  // 이 순간 Plain 도 클라이언트 컴포넌트

export default function Wrap() {
  return <Plain />;
}
```

빌드 결과를 확인해 보면 `Plain` 의 코드가 JS Bundle 에 들어가 있다.
그래서 `"use client"` 는 **최대한 아래쪽 , 필요한 작은 컴포넌트에** 붙인다.

페이지 전체에 붙이면 서버 컴포넌트를 쓰는 의미가 사라진다.

```
❌ page.js 전체에 "use client"

✅ page.js          (서버)
   ├─ Header        (서버)
   ├─ PostList      (서버)
   └─ LikeButton    (클라이언트 , 여기만 "use client")
```

### 2. 서버 컴포넌트는 children 으로 넘긴다

클라이언트 컴포넌트에서 서버 컴포넌트를 import 하면 위처럼 클라이언트가 된다.
하지만 **서버 컴포넌트가 둘을 조립**하면 서버 컴포넌트를 유지할 수 있다.

```jsx
// app/Wrap.js
"use client";

export default function Wrap({ children }) {
  return <div onClick={() => console.log("클릭")}>{children}</div>;
}
```

```jsx
// app/page.js (서버 컴포넌트)
import Wrap from "./Wrap";
import Slot from "./Slot";

export default function Page() {
  return (
    <Wrap>
      <Slot />  {/* 서버 컴포넌트 그대로 */}
    </Wrap>
  );
}
```

빌드 결과를 확인해 보면 `Slot` 의 코드는 JS Bundle 에 **없다.**

`Slot` 은 주방에서 이미 완성됐고, `Wrap` 은 그 **결과만** 받기 때문이다.
불판 옆에 완성된 반찬을 같이 내주는 것과 같다.

자주 쓰는 Context Provider 도 이 방식이다.

```jsx
// app/providers.js
"use client";

import { ThemeProvider } from "./theme";

export default function Providers({ children }) {
  return <ThemeProvider>{children}</ThemeProvider>;
}
```

`layout.js` 에서 `<Providers>{children}</Providers>` 로 감싸면 하위 페이지는 서버 컴포넌트로 남는다.

### 3. props 는 직렬화할 수 있어야 한다

서버에서 클라이언트로 넘기는 props 는 **RSC Payload 에 담겨서** 네트워크를 건너간다.
쟁반에 담을 수 있는 것만 나갈 수 있다는 뜻이다.

| 값 | 전달 |
|---|---|
| 문자열 , 숫자 , boolean , null | 가능 |
| 배열 , 일반 객체 | 가능 |
| Date , Map , Set | 가능 |
| JSX (children) | 가능 |
| 함수 | **불가** |
| 클래스 인스턴스 | **불가** |

함수를 넘기면 이런 에러가 난다.

```jsx
<Counter initial={1} format={() => "x"} />
```

```
Error: Functions cannot be passed directly to Client Components unless you explicitly
expose it by marking it with "use server".
```

주방장을 쟁반에 담아서 내보낼 수는 없다.

예외가 하나 있다. 에러 문구에 나온 `"use server"` 를 붙인 **Server Actions** 는 넘길 수 있다.
함수 자체가 가는 게 아니라, **서버 함수를 호출할 수 있는 참조**가 전달되는 것이다.

---

## 에러로 보는 차이

자주 만나는 에러 두 개

### 서버 컴포넌트에서 useState

```
Error: You're importing a module that depends on `useState` into a React Server Component
module. This API is only available in Client Components.
```

상태가 필요하니 그 부분을 **클라이언트 컴포넌트로 분리**하라는 뜻이다.

### 서버 컴포넌트에서 onClick

```jsx
export default function Page() {
  return <button onClick={() => {}}>클릭</button>;
}
```

```
Error: Event handlers cannot be passed to Client Component props.
```

`button` 은 브라우저로 가는데, onClick 함수는 쟁반에 못 담기 때문이다.
이것도 **버튼만 클라이언트 컴포넌트로 분리**하면 된다.

---

## 비밀값은 어떻게 될까

서버 컴포넌트는 브라우저로 안 가니 비밀값을 써도 된다.
그럼 클라이언트 컴포넌트에서 쓰면 어떻게 될까 ?

```bash
# .env
SECRET_KEY=abc123
NEXT_PUBLIC_API=pub456
```

```jsx
"use client";

export default function Wrap() {
  return <p>{String(process.env.SECRET_KEY)} | {process.env.NEXT_PUBLIC_API}</p>;
}
```

빌드 후 `.next/static` 을 검색해 보면

| 값 | JS Bundle |
|---|---|
| `SECRET_KEY` 값 | **없음** |
| `NEXT_PUBLIC_API` 값 | **있음** |

`NEXT_PUBLIC_` 이 붙은 값만 Bundle 에 들어간다.
즉 **`NEXT_PUBLIC_` 이 붙은 값은 누구나 볼 수 있다.** 비밀값에 붙이면 안 된다.

DB 코드처럼 서버 전용 파일이 클라이언트로 넘어가는 실수는 `server-only` 패키지로 막을 수 있다.

```javascript
// app/db.js
import "server-only";

export const getUser = () => { /* DB 조회 */ };
```

클라이언트 컴포넌트에서 import 하면 **빌드가 실패한다.**

```
Error: You're importing a module that depends on "server-only" into a React Client Component
module.
```

주방 출입문에 **"직원 외 출입 금지"** 를 붙이는 셈이다.

---

## 뭘 써야 할까 ?

기본은 서버 컴포넌트 , 필요할 때만 클라이언트 컴포넌트

| 하고 싶은 일 | 선택 |
|---|---|
| DB , API 에서 데이터 가져오기 | 서버 |
| 비밀 키 사용 | 서버 |
| 큰 라이브러리 사용 (마크다운 변환 등) | 서버 |
| 글 본문처럼 보여주기만 하는 화면 | 서버 |
| 버튼 클릭 , 입력 폼 | 클라이언트 |
| useState , useEffect 사용 | 클라이언트 |
| localStorage , window 사용 | 클라이언트 |
| Context 사용 | 클라이언트 |

판단 기준은 하나다.

> **사용자와 상호작용하거나 브라우저 기능이 필요한가 ?**

아니라면 서버 컴포넌트로 둔다.

---

## 서버 컴포넌트 vs 클라이언트 컴포넌트

| 항목 | 서버 컴포넌트 | 클라이언트 컴포넌트 |
|---|---|---|
| 선언 | 기본값 | 파일 최상단에 `"use client"` |
| 실행 위치 | 서버만 | 서버 (HTML 생성) + 브라우저 |
| 실행 시점 | 빌드 또는 요청 시 | 첫 진입 시 서버 + 하이드레이션 , 이후 상태 변경마다 |
| JS Bundle | 포함 안 됨 | 포함됨 |
| 하이드레이션 | 없음 | 있음 |
| async / await | 가능 | 지원 안 함 |
| Hook , 이벤트 | 불가 | 가능 |
| 서버 자원 (DB , 비밀 키) | 직접 접근 | 불가 |
| 브라우저 API | 불가 | 가능 (useEffect , 이벤트 안에서) |
| 다른 쪽 포함 | 클라이언트를 import 가능 | 서버는 children 으로만 |
| 받는 props | 제한 없음 | 직렬화 가능한 값 , Server Actions |
| 비유 | 주방에서 완성된 요리 | 불판에서 마저 굽는 고기 |

---

## 정리

- App Router 에서는 **기본이 서버 컴포넌트**고 , `"use client"` 를 붙이면 클라이언트 컴포넌트다
- **클라이언트 컴포넌트도 서버에서 실행된다.** 차이는 브라우저까지 가느냐다
- 서버 컴포넌트의 코드는 JS Bundle 에 들어가지 않는다
- `"use client"` 는 **경계선**이라 import 하는 것까지 넘어간다. 그래서 **작은 컴포넌트에** 붙인다
- 서버 컴포넌트를 유지하려면 **children** 으로 넘긴다
- 서버 → 클라이언트 props 는 **직렬화 가능**해야 한다
- `NEXT_PUBLIC_` 값은 공개된다. 서버 전용 코드는 `server-only` 로 막자

완성된 요리는 주방에서, 직접 구워야 맛있는 것만 불판으로.
