# 조건부 타입

- 확장 (extends). 와 3항 연산자를 활용하여 타입을 부여하는 방식 (제네릭에서 많이 씀)


```typeScript
type A = number extends string ? string : number;

type ObjA = {
	a : number;
};

type ObjB = {
	a : number;
	b : number;
}
// ObjB는 ObjA의 확장이므로 number
type B = ObjB extends ObjA ? number : string;
```


```typeScript
type StringNumberSwitch<T> = T extends number ? string : number;

// 
let varA : StringNumberSwitch<number>

  
let varB : StringNumberSwitch<string>
```