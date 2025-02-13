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


