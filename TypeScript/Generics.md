---
aliases:
  - "\bGenerics"
---
# 제네릭 타입
자바에서 쓴 제네릭과 같음. ( 단 일부분은 다름..)

```typeScript
function func<T>(value:T) : T{
	return value;
}

let num = func(10);

if(typeof num === 'number'){

	num.toFixed();

}

  

let bool = func(true);

  

let str = func('string');

let arr = func([1,2,3]);

// 튜플 
let arr = func<[number,number,number]>([1,2,3]);
```

상황에 따라 다른 타입을 담을 수 있게 제네릭 타입 적용을 하는데 위의 코드처럼 작성해야함 . 

(단, 자바처럼 ? 같은 와일드 카드가 없음)

## 타입 변수 응용
```typeScript
function swap<T, U>(a:T,b:U){

	return [b,a];

}
const [a,b] = swap ("1",2);
```

기존처럼 \<T> 진행하게 될 시 
a : T , b : T 가 되는데 
그럼 "1" 로 인해 string 타입을 가지게 됨 
-> 그러므로 U 로 변수 하나를 더 주어서 string, number 로 바꿔 가져갈 수 있음

```typeScript
function returnFirstValue<T>(data:T[]){

return data[0];

}
let num = returnFirstValue([0,1,2]);

let str = returnFirstValue(["dd",'ww']);
```
해당 코드 진행 시 값은 0 , dd가 나옴 (0번째 위치 배열 값)

