# 함수 타입 표현식
비슷한 형태의 타입 선언이 많이 필요하다면 하나의 타입 선언을 반복적으로 사용 할 수 있다 . 

```typeScript

type Operation = (a:number , b:number) => number;

const add : Operation = (a,b) => a + b;
const minus : Operation = (a,b) => a - b;
const multiply : Operation = (a,b) => a ** b;
const divide : Operation = (a,b) => a / b;
```

## 호출 시그니처 (콜 시그니처)
```typeScript

```