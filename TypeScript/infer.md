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
```

R 이라는 타입일 때 맞으면 R , 아니면 never 라고 생각하면 됨 . 

