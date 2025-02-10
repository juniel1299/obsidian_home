타입에 이름을 지어주는 또 다른 문법 

```typeScript
type A = {
	a : string;
	b : number;
}

interface A {
	a : string;
	b : number;
}

//둘은 같은 형태임 . 
```

객체의 구조를 정의하는데 특화된 문법으로 상속이나 합침 같은 특수 기능도 존재함. 

## 확장 
extends 를 붙이면 상속을 할 수 있다.

```typeScript
interface Animal {

	name : string;
	
	age : number;

};

  

interface Dog extends Animal {

	isBark : boolean;

};

  

interface Cat extends Animal {

	isScratch : boolean;

};

interface Chicken extends Animal {

	isFly : boolean;

};

  
  

const dog : Dog = {

	name : 'ㅇㅇ',
	
	age : 11,
	
	isBark : true,

}
```
이렇게 확장을 할 수 있으며 
만약 일부 타입 선언에서만 다른 타입을 가져오고 싶으면 
```typeScript
interface Animal {

	name : string;
	
	age : number;

};

  

interface Dog extends Animal {
	name : number;
	isBark : boolean;

};
```
이런식으로 상속 받은 것을 자바의 오버라이딩처럼 할 수 있다