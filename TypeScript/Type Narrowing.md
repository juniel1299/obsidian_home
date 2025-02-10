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


타입스크립트는 typeof 를 통해 위에 내용은 number , 아래 내용은 string 이라고 추론함 . 
(if문 밖에서 찍으면 number | string 타입으로 찍힘..)

들어오는 타입에 따라 조건문을 통해 두 갈랫길을 만들 수 있음.
