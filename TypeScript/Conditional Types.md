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

// string 적용
let varA : StringNumberSwitch<number>

// number 적용
let varB : StringNumberSwitch<string>
```

```typeScript
function removeSpaces<T>(text : T) : T extends string ? string : undefined;

function removeSpaces(text:any) {
	if(typeof text === 'string'){
		return text.replaceAll(" ","");
	}
	else{
		return undefined;
	}
}

let result = removeSpaces("가 나 다 라 마");
console.log(result.toUpperCase());
```

이렇게 하면 T 가 string이 들어오면 string 으로 인식 , 이외에는 undefined로 