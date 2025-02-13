# Inference (추론)
 ```typeScript
type FuncA = () => string;

  

type FuncB = () => number;



type ReturnType<T> = T extends () => string ? string : never;

type A = ReturnType<FuncA>;

type B = ReturnType<FuncB>;
```

T에 Func 가 들어가는데 Func는 string -> 결과값은 string이 됨 . 

