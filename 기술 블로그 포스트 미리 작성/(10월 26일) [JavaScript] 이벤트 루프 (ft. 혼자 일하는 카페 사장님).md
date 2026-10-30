## 자바스크립트는 싱글 스레드다

자바스크립트를 공부하면 꼭 듣는 말

> "자바스크립트는 싱글 스레드 언어다"

스레드가 하나라는 건 **한 번에 한 가지 일만** 할 수 있다는 뜻이다.
(스레드가 헷갈린다면 [프로세스 vs 스레드](https://problem-child.tistory.com/104) 글을 먼저 보고 오면 좋습니다)

그런데 이상하다.

- API 를 호출해 놓고 응답을 기다리는 동안에도 버튼이 눌린다
- 타이머가 돌아가는 중에도 스크롤이 된다
- 이미지를 받으면서 애니메이션도 돌아간다

한 번에 하나밖에 못 한다면서 어떻게 이게 다 될까 ?
답은 **이벤트 루프 (Event Loop)** 에 있다.

---

## 혼자 일하는 카페 사장님

이벤트 루프는 **혼자 일하는 카페 사장님**으로 비유하면 쉽다.

- 사장님은 한 명이다 (싱글 스레드)
- 그래서 주문은 한 번에 한 명씩만 받는다
- 대신 커피 머신 , 오븐 같은 **기계**는 사장님 없이도 알아서 돌아간다
- 기계가 다 되면 **진동벨**이 울리고, 사장님은 손이 비었을 때 하나씩 처리한다

사장님이 커피 추출을 지켜보고 서 있으면 다음 손님을 못 받는다.
그래서 **기계에 맡겨두고 다음 주문을 받는 것** , 이게 핵심이다.

| 카페 | 자바스크립트 |
|---|---|
| 사장님 | 콜 스택 (Call Stack) |
| 커피 머신 , 오븐 | Web API (브라우저가 제공) |
| 진동벨 대기 줄 | 태스크 큐 (Task Queue) |
| 단골 VIP 대기 줄 | 마이크로태스크 큐 (Microtask Queue) |
| 손이 비었는지 계속 확인하는 습관 | 이벤트 루프 (Event Loop) |

---

## 구성 요소

### 콜 스택 (Call Stack)

지금 실행 중인 함수가 쌓이는 곳
자바스크립트 엔진에는 **콜 스택이 딱 하나**다. 이게 싱글 스레드라는 말의 정체다.

```javascript
function first() {
  second();
  console.log("first");
}

function second() {
  console.log("second");
}

first();
```

```
1. first() 들어감        [ first ]
2. second() 들어감       [ first , second ]
3. second 출력 후 빠짐   [ first ]
4. first 출력 후 빠짐    [ ]
```

나중에 들어온 게 먼저 나가는 스택 구조다.

### Web API

setTimeout , fetch , DOM 이벤트 (클릭 등) 는 **자바스크립트 엔진의 기능이 아니다.**
**브라우저**가 제공하는 기능이다.

```
브라우저
 ├─ 자바스크립트 엔진 (V8 등) → 콜 스택 1개 (싱글 스레드)
 └─ Web API → 타이머 , 네트워크 , 이벤트 처리 (브라우저가 별도로 처리)
```

자바스크립트는 싱글 스레드지만, **자바스크립트가 돌아가는 브라우저는 싱글 스레드가 아니다.**
오래 걸리는 일은 브라우저에게 맡기고, 자바스크립트는 다음 코드를 실행한다.

### 태스크 큐 (Task Queue)

Web API 가 일을 끝내면 **실행할 콜백**이 여기서 줄을 선다.

- setTimeout , setInterval 콜백
- 클릭 , 키보드 같은 이벤트 콜백

(매크로태스크 큐 , 콜백 큐 라고도 부른다)

### 마이크로태스크 큐 (Microtask Queue)

태스크 큐보다 **우선순위가 높은** 줄

- Promise 의 then , catch , finally 콜백
- await 다음에 오는 코드
- queueMicrotask()

### 이벤트 루프 (Event Loop)

계속 돌면서 이 규칙을 반복한다.

```
1. 콜 스택이 비었나 ?
2. 비었으면 → 마이크로태스크 큐를 "전부" 실행
3. 화면을 다시 그릴 타이밍이면 → 렌더링
4. 태스크 큐에서 "하나" 꺼내서 실행
5. 다시 1번으로
```

마이크로태스크는 **있는 대로 전부** , 태스크는 **한 번에 하나**
이 차이가 중요하다.

---

## 실행 순서 맞혀보기

```javascript
console.log("1");

setTimeout(() => {
  console.log("2");
}, 0);

Promise.resolve().then(() => {
  console.log("3");
});

console.log("4");
```

setTimeout 이 0초니까 1 , 2 , 3 , 4 일 것 같지만

```
1
4
3
2
```

### 왜 이렇게 될까 ?

```
[1] console.log("1")        → 콜 스택에서 바로 실행 → 1 출력
[2] setTimeout(... , 0)      → 브라우저(Web API)에 타이머 맡김
                               → 0초 뒤 콜백이 태스크 큐로 이동
[3] Promise.then(...)        → 콜백이 마이크로태스크 큐로 이동
[4] console.log("4")        → 콜 스택에서 바로 실행 → 4 출력

--- 콜 스택이 비었다 ---

[5] 마이크로태스크 큐 전부 실행 → 3 출력
[6] 태스크 큐에서 하나 실행     → 2 출력
```

카페로 치면

- 1 , 4 : 지금 줄 서 있는 손님 → 바로 처리
- 3 : 단골 VIP → 손이 비자마자 제일 먼저
- 2 : 진동벨 손님 → VIP 다음

**setTimeout(fn, 0) 은 "즉시 실행" 이 아니라 "최대한 빨리 줄 서기" 다.**

---

## async / await 도 결국 마이크로태스크

async , await 문법은 [동기 ? 비동기 ? async , await ?](https://problem-child.tistory.com/113) 글에서 정리했다.
이벤트 루프 관점에서 보면 이렇다.

```javascript
async function order() {
  console.log("A");
  await null;
  console.log("B"); // await 다음 코드는 마이크로태스크로 예약됨
}

console.log("1");
order();
console.log("2");
```

```
1
A
2
B
```

- order() 를 부르면 await 전까지 (A) 는 바로 실행된다
- await 를 만나면 함수가 **잠깐 멈추고** , 나머지 (B) 는 마이크로태스크 큐로 간다
- 그 사이 바깥 코드 (2) 가 먼저 실행된다

await 는 사장님을 붙잡아 두는 게 아니라, **"이건 나중에 마저 할게요"** 하고 다음 손님을 받는 것이다.

---

## 사장님이 붙잡히면 : 블로킹

이벤트 루프가 잘 돌려면 콜 스택이 **빨리 비워져야** 한다.
콜 스택을 오래 붙잡는 코드가 있으면 전부 멈춘다.

```javascript
button.addEventListener("click", () => {
  const start = Date.now();
  while (Date.now() - start < 5000) {} // 5초 동안 계속 반복
  console.log("끝");
});
```

이 버튼을 누르면 5초 동안

- 다른 버튼 클릭 안 됨
- 스크롤 안 됨
- 타이머 콜백도 실행 안 됨
- 화면 렌더링도 멈춤

사장님이 손님 한 명 붙잡고 5분 동안 수다를 떠는 상황이다.
뒤에 줄은 계속 길어진다.

### 마이크로태스크도 조심

마이크로태스크는 **큐가 빌 때까지 전부** 실행한다고 했다.
then 안에서 계속 새 마이크로태스크를 만들면 큐가 영원히 안 비고, 렌더링도 태스크도 실행되지 못한다.

VIP 손님이 계속 새 VIP 를 데려오는 셈이다.

---

## 무거운 작업은 어떻게 ?

### 1. 잘게 쪼개기

큰 작업을 나눠서 중간중간 이벤트 루프에게 차례를 넘긴다.

```javascript
function processInChunks(items, chunkSize = 1000) {
  let index = 0;

  function runChunk() {
    const end = Math.min(index + chunkSize, items.length);
    for (; index < end; index++) {
      heavyWork(items[index]);
    }
    if (index < items.length) {
      setTimeout(runChunk, 0); // 다음 조각은 태스크 큐로 → 그 사이 클릭 , 렌더링 처리 가능
    }
  }

  runChunk();
}
```

### 2. Web Worker : 알바생 고용

정말 무거운 계산은 **별도 스레드**에서 돌린다.

```javascript
// main.js
const worker = new Worker("worker.js");
worker.postMessage(bigData);              // 일 맡기기
worker.onmessage = (event) => {
  console.log("결과", event.data);         // 결과 받기
};
```

```javascript
// worker.js
self.onmessage = (event) => {
  const result = heavyCalculation(event.data);
  self.postMessage(result);
};
```

- 워커는 메인 스레드와 **따로** 돌아가서 화면이 멈추지 않는다
- 대신 DOM 에는 접근할 수 없고, 메시지로만 데이터를 주고받는다

주방에 알바생을 들인 셈이다. 계산대 (화면) 는 여전히 사장님만 만질 수 있다.

---

## Node.js 는 ?

Node.js 도 같은 원리다.

- 자바스크립트 실행은 싱글 스레드 (V8 엔진)
- 파일 읽기 , 네트워크 같은 일은 **libuv** 라는 라이브러리가 대신 처리
- 끝나면 이벤트 루프가 콜백을 실행

브라우저의 Web API 자리를 libuv 가 맡고 있다고 보면 된다.
(Node.js 이벤트 루프는 timers , poll , check 같은 단계로 더 세분화되어 있다)

---

## 정리

| 구성 요소 | 역할 | 카페 |
|---|---|---|
| 콜 스택 | 지금 실행 중인 코드 (1개뿐) | 사장님 |
| Web API | 타이머 , 네트워크 , 이벤트를 대신 처리 | 커피 머신 , 오븐 |
| 마이크로태스크 큐 | Promise , await 이후 코드 (전부 실행) | 단골 VIP 줄 |
| 태스크 큐 | setTimeout , 이벤트 콜백 (하나씩 실행) | 진동벨 줄 |
| 이벤트 루프 | 콜 스택이 비면 큐에서 꺼내 실행 | 손 비면 다음 일 확인 |
| Web Worker | 별도 스레드에서 무거운 계산 | 알바생 |

- 자바스크립트 **엔진**은 싱글 스레드지만, **브라우저**가 오래 걸리는 일을 대신 해준다
- 이벤트 루프는 콜 스택이 빌 때마다 **마이크로태스크 전부 → 태스크 하나** 순서로 실행한다
- setTimeout(fn, 0) 도 Promise.then 보다 늦다
- 콜 스택을 오래 붙잡으면 화면 전체가 멈춘다 → 쪼개거나 Web Worker 로

한 명이라도 일을 잘 맡기면 카페는 잘 돌아간다.
