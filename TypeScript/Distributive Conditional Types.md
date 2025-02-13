# 분산적인 조건부 타입 
```typeScript
type StringNumberSwitch<T> = T extends number ? string : number;

let a : StringNumberSwitch<number>;

let b : StringNumberSwitch<string>;
```

이렇게 하면 결과는 a : string , b : number 가 나오게 된다 . 