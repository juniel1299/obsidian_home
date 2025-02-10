# 타입 좁히기
- 조건문을 활용해서 넓은 타입에서 좁은 타입으로 범위를 좁히는 기능.


```typeScript

function func(value : number | string) {

	if(typeof value === 'number'){
	
		console.log(value.toFixed());

	}

	else if (typeof value === 'string'){

		console.log(value.toUpperCase());

	}

};

```
## 일반적이지 않은 타입


타입스크립트는 typeof 를 통해 위에 내용은 number , 아래 내용은 string 이라고 추론함 . 
(if문 밖에서 찍으면 number | string 타입으로 찍힘..)

들어오는 타입에 따라 조건문을 통해 두 갈랫길을 만들 수 있음.

만약 node 에서 제공하는 Date 타입을 받기 위해선 
조건문에 value instanceof Date  작성 해야함.
```typeScript
else if (value instanceof Date){

	console.log(value.getTime());

}
```

## 내가 만든 타입 
내가 만든 타입에 따라 동작이 다르게 하기 위해선 

```typeScript
type Person = {
	name : string,
	age : number,
};


```