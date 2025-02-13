# 분산적인 조건부 타입 
```typeScript
type StringNumberSwitch<T> = T extends number ? string : number;

let a : StringNumberSwitch<number>;

let b : StringNumberSwitch<string>;
```

이렇게 하면 결과는 a : string , b : number 가 나오게 된다 . 

```typeScript
let c : StringNumberSwitch<number | string>;

let d : StringNumberSwitch<boolean | number | string>;
```

이렇게 유니온 타입으로 넣어주게 될 경우 분산적 조건부 타입