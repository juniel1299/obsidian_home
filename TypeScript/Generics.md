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

