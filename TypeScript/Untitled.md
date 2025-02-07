number Type 슈퍼타입 (부모 타입)

number literal Type 서브타입 (자식 타입)

부모 타입 안에 자식 타입이 있으므로 

자식 타입을 부모 타입 취급은 가능하지만 
부모 타입을 자식 타입 취급은 불가능함. 

예시 

가능한 경우 (업 캐스팅)
```typescript

let num1 : number = 10;
let num2 : 10 = 10;

num1 = num2;
```


불가능한 경우(다운 캐스팅)
```typescript

let num1 : number = 10;
let num2 : 10 = 10;

num2 = num1;
```

