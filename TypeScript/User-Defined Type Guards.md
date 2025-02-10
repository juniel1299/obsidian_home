# 사용자 정의 타입가드
타입 좁히기를 돕기 위한 함수
조건문을 통해 해당 값이 특정 타입임을 typeScript가 인지하도록 하는 것이 목표 



기존의 typeof 를 이용해서 하는 방법 이외에 is 를 이용해서 할 수 있다.

```typeScript
type Cat = {

	name : string;
	
	isScratch : boolean;

};

  

type Animal = Dog | Cat;

  

// 강아지인지 고양이인지 구분 (???)

function isDog(animal : Animal): animal is Dog{

	return (animal as Dog).isBark !== undefined;

}

  

function isCat(animal : Animal) : animal is Cat {

	return (animal as Cat).isScratch !== undefined;

}

  
  

function warning(animal:Animal){

	if("isBark" in animal){

	}
	else if ("isScratch" in animal){

	}

}
```
