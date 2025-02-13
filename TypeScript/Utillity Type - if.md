# 조건부 타입 기반 유틸리티 
- Exclude \<T,U\>
- Extract \<T,U\>
- ReturnType\<T\>

## Exclude\<T,U\>
- T에서 U 를 제거하는 타입 

```typeScript
// string , boolean 타입에서 boolean 제거 . 
type A = Exclude <string | boolean , boolean>; 
```

```typeScript
type Exclude<T,U> = T extends U ? never : T; 

// 1. <string , boolean> <boolean , boolean> 
// 2. string | never 됨 . 
```

## Extract\<T,U\>
- T 에서 U를 추출하는 타입 . 
```typeScript
type B = Extract<string | boolean,boolean> 
// B : boolean
```

```typeScript
type Extract<T,U> = T extends U ? T : never; 
```

위와 같은 내용임..

## ReturnType\<T\>

- 함수의 반환 값 타입을 추출하는 타입

```typeScript
function funcA(){
	return "hello";
};

function funcB(){
	return 10;
};

type ReturnA = ReturnType<typeof funcA>;

type ReturnB = ReturnType<typeof funcB>;
```
Asms 문자 B는 숫자를 리턴 받았기 때문에 타입은 string , number 임 . 

```typeScript
type ReturnType<T extends (...args: any) => any > = T extends(

	...agrs : any
	
)   => infer R
	
	? R

	: never;
```

해당 내용과 같음. 