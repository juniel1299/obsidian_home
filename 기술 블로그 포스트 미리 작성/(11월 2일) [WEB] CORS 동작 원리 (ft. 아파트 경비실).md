## CORS 에러 , 고치긴 했는데

예전에 [CORS 에러란 ?](https://problem-child.tistory.com/101) 글에서 Spring 으로 CORS 에러를 해결하는 방법을 정리했다.
그런데 설정만 복붙하고 넘어가면 이런 질문에 답을 못 한다.

- 요청은 서버에 **도착했을까 , 안 했을까 ?**
- GET 은 되는데 왜 JSON 으로 POST 하면 에러가 날까 ?
- 왜 갑자기 **OPTIONS** 요청이 하나 더 날아갈까 ?
- 쿠키를 같이 보내면 왜 `*` 가 안 될까 ?

이번 글은 CORS 가 **실제로 어떻게 동작하는지**를 정리한다.

아파트 경비실로 생각하면 쉽다.

- **브라우저** : 경비실 (출입을 막는 쪽)
- **서버** : 입주민 (누구를 들여보낼지 정하는 쪽)
- **CORS 헤더** : 입주민이 경비실에 맡겨둔 **방문 허가 명단**

---

## 출처 (Origin) 란

출처는 **프로토콜 + 호스트 + 포트** 세 개를 합친 것이다.
셋 중 하나라도 다르면 다른 출처다.

`http://localhost:3000` 기준으로 보면

| 주소 | 같은 출처 ? | 이유 |
|---|---|---|
| http://localhost:3000/about | O | 경로는 상관없음 |
| https://localhost:3000 | X | 프로토콜이 다름 |
| http://127.0.0.1:3000 | X | 호스트가 다름 (같은 컴퓨터여도) |
| http://localhost:8080 | X | 포트가 다름 |

프론트 (3000) 와 백엔드 (8080) 를 따로 띄우면 포트가 다르니까 **무조건 다른 출처**다.

---

## 동일 출처 정책 (SOP)

브라우저에는 **동일 출처 정책 (Same-Origin Policy)** 이 있다.

> 다른 출처에서 가져온 응답은 자바스크립트가 **읽을 수 없다**

왜 이런 규칙이 있을까 ?

내가 은행 사이트에 로그인한 채로, 수상한 사이트에 들어갔다고 해 보자.
수상한 사이트의 자바스크립트가 `fetch("https://bank.com/my-account")` 를 하면,
브라우저는 은행 쿠키를 같이 실어 보낼 수 있다.

SOP 가 없으면 그 응답 (내 계좌 정보) 을 수상한 사이트가 그대로 읽어 간다.
그래서 브라우저가 **"다른 출처 응답은 못 읽어"** 라고 막는 것이다.

### CORS 는 SOP 의 예외 규칙

그런데 요즘은 프론트와 API 서버가 다른 출처인 게 기본이다.
그래서 **"이 출처는 읽어도 돼"** 라고 서버가 허락하는 방법이 생겼다.
그게 **CORS (Cross-Origin Resource Sharing , 교차 출처 리소스 공유)** 다.

CORS 는 막는 규칙이 아니라, SOP 를 **풀어주는** 규칙이다.

---

## 핵심 : 요청은 이미 도착했다

제일 많이 오해하는 부분

> CORS 에러가 났다 = 서버가 요청을 거절했다 ❌

단순 요청 (아래에서 설명) 이라면 실제로는 이렇다.

```
브라우저 ── GET /api/users ──→ 서버
브라우저 ←── 200 OK + 데이터 ── 서버     (서버는 정상 응답)
브라우저 : "응답에 허가 명단 (Access-Control-Allow-Origin) 이 없네 ?"
         → 자바스크립트에게 응답을 안 넘겨줌 → CORS 에러
```

서버는 요청을 받고 , 처리하고 , 응답까지 보냈다.
**브라우저가 그 응답을 자바스크립트에게 안 보여줄 뿐**이다.

경비실이 택배를 받아 놓고, 명단에 없는 사람이라 **안 내주는** 것과 같다.

그래서

- **Postman , curl** 로는 CORS 에러가 안 난다 (브라우저가 아니니까 경비실이 없음)
- **서버끼리** 통신할 때도 CORS 는 상관없다
- 해결은 결국 **서버가 허가 명단 (응답 헤더) 을 주는 것**이다

(101번 글에서 "프론트에서는 사실상 해결 방법이 없다" 고 한 이유가 이것이다)

---

## CORS 요청 3가지

브라우저는 요청 종류에 따라 다르게 행동한다.

### 1. 단순 요청 (Simple Request)

바로 본 요청을 보내고, 응답 헤더를 확인한다.

```
브라우저 → 서버
GET /api/users
Origin: http://localhost:3000

서버 → 브라우저
200 OK
Access-Control-Allow-Origin: http://localhost:3000   ← 이게 있으면 통과
```

단순 요청이 되려면 **아래 조건을 전부** 만족해야 한다.

| 조건 | 허용 |
|---|---|
| 메서드 | GET , HEAD , POST |
| 직접 넣은 헤더 | Accept , Accept-Language , Content-Language , Content-Type , Range 만 |
| Content-Type | application/x-www-form-urlencoded , multipart/form-data , text/plain 만 |

여기서 중요한 건 **Content-Type**

`application/json` 이 **목록에 없다.**
그래서 JSON 으로 POST 하는 순간, 단순 요청이 아니게 된다.
`Authorization` 헤더 (토큰) 를 넣어도 마찬가지다.

즉 우리가 평소에 보내는 API 요청은 대부분 **단순 요청이 아니다.**

### 2. 사전 요청 (Preflight Request)

단순 요청이 아니면, 브라우저가 본 요청 전에 **OPTIONS 요청으로 먼저 물어본다.**

경비실이 방문객을 바로 들여보내지 않고, **인터폰으로 먼저 확인**하는 것과 같다.

```
① 사전 요청 (브라우저가 자동으로 보냄)
OPTIONS /api/users
Origin: http://localhost:3000
Access-Control-Request-Method: POST              ← "POST 해도 돼 ?"
Access-Control-Request-Headers: content-type     ← "이 헤더 넣어도 돼 ?"

② 서버 응답
204 No Content
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Max-Age: 600                      ← "600초 동안은 다시 안 물어봐도 돼"

③ 허락됐으니 본 요청
POST /api/users
Origin: http://localhost:3000
Content-Type: application/json
```

개발자 도구 Network 탭에서 같은 주소로 요청이 **두 번** 찍히는 이유가 이것이다.

사전 요청이 단순 요청과 다른 점

- 사전 요청에서 거절되면 **본 요청은 아예 안 보낸다**
- 그래서 PUT , DELETE 처럼 서버 데이터를 바꾸는 요청이 허락 없이 실행되는 걸 막아준다

`Access-Control-Max-Age` 로 사전 요청 결과를 캐싱할 수 있다.
다만 브라우저마다 최대값이 있어서 (Chrome 은 2시간) 그 이상 줘도 소용없다.

### 3. 인증 정보 포함 요청 (Credentialed Request)

다른 출처로 `fetch` 하면 기본적으로 **쿠키가 실리지 않는다.**
쿠키 (세션 , 로그인 정보) 를 같이 보내려면 프론트에서 따로 켜야 한다.

```javascript
// fetch
fetch("http://localhost:8080/api/me", {
  credentials: "include",
});

// axios
axios.get("http://localhost:8080/api/me", {
  withCredentials: true,
});
```

그리고 서버도 조건이 더 까다로워진다.

```
Access-Control-Allow-Origin: http://localhost:3000   ← * 불가 , 정확한 출처만
Access-Control-Allow-Credentials: true               ← 필수
```

왜 `*` 가 안 될까 ?

`*` 는 "아무나 들어와" 라는 뜻이다.
쿠키까지 실린 요청을 아무 출처에나 열어주면, 처음에 말한 **은행 계좌 문제**가 그대로 생긴다.
그래서 브라우저는 쿠키가 실린 요청에 `*` 가 오면 **무조건 막는다.**
(Allow-Methods , Allow-Headers 의 `*` 도 이때는 와일드카드로 인정되지 않는다)

---

## 직접 만들어 보는 CORS 서버 (Node.js)

프레임워크 없이 헤더만으로 처리하면 이렇게 된다.

```javascript
const http = require("http");

const ALLOWED_ORIGIN = "http://localhost:3000";

http.createServer((req, res) => {
  // 허용한 출처일 때만 CORS 헤더를 붙인다
  if (req.headers.origin === ALLOWED_ORIGIN) {
    res.setHeader("Access-Control-Allow-Origin", ALLOWED_ORIGIN);
    res.setHeader("Access-Control-Allow-Credentials", "true");
    res.setHeader("Vary", "Origin");
  }

  // Preflight (OPTIONS) 응답
  if (req.method === "OPTIONS") {
    res.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
    res.setHeader("Access-Control-Max-Age", "600");
    res.writeHead(204);
    return res.end();
  }

  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ message: "hello" }));
}).listen(8080);
```

curl 로 사전 요청을 흉내 내 보면

```bash
curl -i -X OPTIONS localhost:8080/api \
  -H "Origin: http://localhost:3000" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: content-type"
```

```
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Credentials: true
Vary: Origin
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Max-Age: 600
```

허용 안 한 출처로 보내 보면

```bash
curl -i localhost:8080/api -H "Origin: http://evil.com"
```

```
HTTP/1.1 200 OK
{"message":"hello"}
```

**200 OK 에 데이터까지 그대로 온다.**
허가 명단 (Allow-Origin) 만 없을 뿐이다.
브라우저였다면 이 응답을 자바스크립트에게 안 넘겨줬을 것이다. 위에서 말한 "요청은 이미 도착했다" 가 이것이다.

### Vary: Origin 은 왜 넣었을까 ?

요청한 출처에 따라 응답 헤더가 달라지기 때문이다.
이걸 안 알려주면 중간 캐시 (CDN 등) 가 A 출처용 응답을 B 출처에게 그대로 줄 수 있다.
출처마다 다른 응답이니 **출처별로 따로 캐싱하라**는 표시다.

---

## 자주 하는 실수

### 1. mode: "no-cors" 로 해결하기

에러 메시지에 이런 문장이 있어서 많이 시도한다.

> If an opaque response serves your needs, set the request's mode to 'no-cors'

`no-cors` 는 CORS 를 끄는 옵션이 아니다.
**"응답은 안 읽을 테니 보내기만 할게"** 라는 뜻이다.
응답이 **opaque (불투명)** 상태가 되어서 status 는 0 , body 는 비어 있다. 데이터를 못 쓴다.

### 2. 들어온 Origin 을 그대로 돌려주기

```javascript
// ❌ 위험
res.setHeader("Access-Control-Allow-Origin", req.headers.origin);
res.setHeader("Access-Control-Allow-Credentials", "true");
```

`*` 가 안 되니까 요청의 Origin 을 그대로 복사해서 넣는 경우가 있다.
이러면 **모든 출처에 쿠키 포함 요청을 허락**하는 것과 같다. `*` 보다 더 위험하다.
허용할 출처는 **목록으로 정해 두고 비교**해야 한다.

### 3. 사전 요청이 인증에 막힘

사전 요청 (OPTIONS) 에는 `Authorization` 헤더나 쿠키가 **실리지 않는다.**
그런데 서버가 모든 요청에 로그인 검사를 하면, OPTIONS 가 401 로 막히고 CORS 에러가 난다.
CORS 처리는 **인증보다 앞에서** 해야 한다.
(Spring Security 에서 `.cors()` 를 따로 켜는 이유가 이것이다. 설정 방법은 [CORS 에러란 ?](https://problem-child.tistory.com/101) 글 참고)

### 4. CORS 를 서버 보안으로 생각하기

CORS 는 **브라우저가 지키는 규칙**이다.
curl 이나 서버에서 보내는 요청은 CORS 와 상관없이 그대로 들어온다.
위의 evil.com 예시처럼 응답도 그대로 받는다.

그래서 CORS 설정은 API 보안 (인증 , 권한 검사) 을 **대신하지 않는다.**

---

## 개발할 때는 프록시

개발 중에 매번 서버 설정을 건드리기 번거롭다면, **프록시**를 쓰는 방법도 있다.

```
브라우저 → localhost:3000/api/users   (같은 출처라 CORS 없음)
           ↓ 개발 서버가 대신 전달
           localhost:8080/api/users   (서버끼리 통신이라 CORS 없음)
```

브라우저 입장에서는 계속 3000 번에만 요청하니 같은 출처다.

### Vite

```javascript
// vite.config.js
import { defineConfig } from "vite";

export default defineConfig({
  server: {
    proxy: {
      "/api": "http://localhost:8080",
    },
  },
});
```

### Next.js

```javascript
// next.config.js
module.exports = {
  async rewrites() {
    return [
      {
        source: "/api/:path*",
        destination: "http://localhost:8080/api/:path*",
      },
    ];
  },
};
```

단 Vite 프록시는 **개발 서버에서만** 동작한다.
배포할 때는 서버의 CORS 설정이나 Nginx 같은 리버스 프록시로 다시 처리해야 한다.
(Nginx 가 요청을 나눠주는 방식은 [L4 vs L7](https://problem-child.tistory.com/128) 글 참고)

---

## 단순 요청 vs 사전 요청 vs 인증 포함 요청

| 항목 | 단순 요청 | 사전 요청 | 인증 포함 요청 |
|---|---|---|---|
| 조건 | GET / HEAD / POST + 기본 헤더 + 폼 형식 Content-Type | 단순 요청 조건을 벗어남 (JSON , PUT , DELETE , Authorization 등) | credentials: include , withCredentials: true |
| 요청 횟수 | 1번 | 2번 (OPTIONS + 본 요청) | 위 둘 중 하나를 따름 |
| 거절되면 | 요청은 처리됨 , 응답만 못 읽음 | 본 요청 자체를 안 보냄 | 응답 못 읽음 |
| Allow-Origin | `*` 가능 | `*` 가능 | 정확한 출처만 |
| 추가 헤더 | 없음 | Allow-Methods , Allow-Headers , Max-Age | Allow-Credentials: true |
| 비유 | 택배 받아두고 명단 확인 | 인터폰으로 먼저 확인 | 집 열쇠까지 맡기는 방문객 |

---

## 정리

- 출처는 **프로토콜 + 호스트 + 포트**다
- 브라우저는 **동일 출처 정책**으로 다른 출처 응답을 막고 , **CORS** 는 서버가 그 예외를 허락하는 방법이다
- CORS 에러가 나도 **요청은 서버에 도착했을 수 있다.** 브라우저가 응답을 안 보여줄 뿐이다
- JSON POST , PUT , DELETE , Authorization 헤더는 **사전 요청 (OPTIONS)** 을 먼저 보낸다
- 쿠키를 보내려면 프론트는 `credentials: "include"` , 서버는 **정확한 출처 + Allow-Credentials: true**
- CORS 는 브라우저 규칙일 뿐 , **서버 보안을 대신하지 않는다**

경비실이 아무리 꼼꼼해도, 명단을 쓰는 건 입주민이다.
