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
extends 를 붙이면 ㄱㅅ