---
aliases:
  - "\bFunction OverLoading"
---
# 함수 오버로딩
자바에서 쓰는 오버로딩과 같음 . 

하나의 함수를 매개변수의 개수나 타입에 따라서 여러가지 버전 만들 수 있음 . 

```typeScript
function func(a:number): void;

function func(a:number,b:number,c:number): void;

  

// 구현부

  

function func(a:number,b?:number,c?:number){
	
	if(typeof b ==='number' && typeof c === 'number'){

		console.log(a+b+c);
	}

else {

console.log(a + 20);

}

};

  

func(1);

func(1,3,2);
```