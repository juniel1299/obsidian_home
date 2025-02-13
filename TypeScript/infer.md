# Inference (추론)
 ```typeScript
type FuncA = () => string;

type FuncB = () => number;

type ReturnType<T> = T extends () => string ? string : never;

type A = ReturnType<FuncA>;

type B = ReturnType<FuncB>;
```

T에 FuncA 가 들어가는데 FuncA는 string -> 결과값은 string이 됨 . 
FuncB도 같은 방식으로 number가 됨 .

추론을 사용하게 되면
```typeScript
type FuncA = () => string;

type FuncB = () => number;

type ReturnType<T> = T extends () => infer R ? R : never;

type A = ReturnType<FuncA>;

type B = ReturnType<FuncB>;

type C = ReturnType<number>;
```

R 이라는 타입일 때 맞으면 R , 아니면 never 라고 생각하면 됨 . 

FuncA 기준으로 

T extends () => infer R 에서 

1. T에 string 이 들어감
2. R이 string이 들어간다면 true 가 되기 때문에(서브타입) typeScript는 R = string 으로 추론  
3. string : string 이므로 참 -> R 이 됨 (R = string 이므로 타입은 string)

하지만 C는 현재 선언된 내용이 없음 -> 추론이 불가능함. -> false에 있는 never 가 타입으로 적용됨.



