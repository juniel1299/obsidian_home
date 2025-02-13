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

이렇게 유니온 타입으로 넣어주게 될 경우 분산적 조건부 타입이 되어버림 

하나씩 값이 들어감 , c 기준으로 한번은 number 한번은 string 이렇게 들어감 

그렇다면 
c 는 string , number 가 되고 이후 하나로 묶이게 됨 
c : \<string | number\>

d : \<number | string\> (중복은 지워짐)


```typeScript
type Exclude <T,U> = T extends U ? never : T;
type A = Exclude<number | string | boolean,string>;
```

마찬가지로 이렇게 들어오면 
A : number | never | boolean 에서 
never는 생략되므로 
A : \<number | boolean\> 이 된다

```typeScript
type Extract<T,U> = T extends U ? T : never;
type B = Extract<number | string | boolean , string > ;
```

반대로 작성하면 

B : \<\>