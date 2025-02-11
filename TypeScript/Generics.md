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

## 타입 변수 응용
```typeScript
function swap<T, U>(a:T,b:U){

	return [b,a];

}
const [a,b] = swap ("1",2);
```

기존처럼 \<T> 진행하게 될 시 
a : T , b : T 가 되는데 
그럼 "1" 로 인해 string 타입을 가지게 됨 
-> 그러므로 U 로 변수 하나를 더 주어서 string, number 로 바꿔 가져갈 수 있음

```typeScript
function returnFirstValue<T>(data:T[]){

return data[0];

}
let num = returnFirstValue([0,1,2]);

let str = returnFirstValue(["dd",'ww']);
```
T\[] 작성하지 않으면 언노운으로 잡힘 . (배열인지 알 수 없음 -> 에러남)

```typeScript
function returnFirstValue<T>(data:[T, ...unknown[]]){

	return data[0];

}

  
  

let num = returnFirstValue([0,1,2]);

  

let str = returnFirstValue([1,"dd",'ww']);
```

응용하게 되면 첫번째는 T 나머지 요소는 모르겠다 + 배열을 명시해줌


```typeScript
function getLength<T extends {length : number}>(data: T){

	return data.length;

}

  

let var1 = getLength([1,2,3]);

  

let var2 = getLength("12345");

  

let var3 = getLength({length : 10});

  

let var4 = getLength(10);
```

length 가 존재하는 경우만 전달하도록 하기 위해선 extends 를 통해 확장하여 진행한다 
( 그러므로 var4 는 에러 )

## map , forEach

```typeScript
const arr = [1,2,3];

const newArr = arr.map((it) => it * 2);

  
	
	function map<T,U>(arr:T[],callback:(item:T) => U){
	
		let result = [];
	
		for (let i = 0; i < arr.length; i++){
	
			result.push(callback(arr[i]));
	
		}
	
	return result;

	}

  

map(arr, (it) => it * 2);

map(['hi','hello'],(it) => it.toUpperCase());

map(['hi','hello'],(it) => parseInt(it));
```
map 의 값을 number , string 두개의 타입을 받기 위해 T, U 필요함

```typeScript
const arr2 = [1,2,3];

arr2.forEach((it) => console.log(it));

  

function forEach<T>(arr : T[], callback: (item : T) => void){

	for (let i = 0; i < arr.length; i++){
	
		callback(arr[i]);
	
	}

}

  

forEach(arr2, (it) =>{

	console.log(it.toFixed());

})

  

forEach(['123','456'], (it) =>{

	it;

})
```
forEach의 경우 

## 제네릭 인터페이스 (타입 변수 , 제네릭 타입 변수)

```typeScript
// 제네릭 인터페이스 , 타입 변수 (제네릭 타입 변수)

interface KeyPair<K,V> {

	key: K,
	
	value : V

};
let keyPair : KeyPair<string,number> = {

	key : 'key',
	value : 0,
};

  

let keyPair2 : KeyPair<boolean,string[]> = {
	
	key:true,
	
	value:['1','1'],
};

// 인덱스 시그니처
interface NumberMap {
	[key : string] : number;
}

  

let numberMap1 : NumberMap = {

	key : 11,
	
	key2 : 131

};

  

interface Map<V>{

	[key : string] : V;

}

  

let stringMap : Map<string> = {

	key : "value",

};

  

let booleanMap : Map<boolean> = {

	key:true,

};

  

// 제네릭 타입 별칭

  

type Map2<V> = {

	[key: string] : V;

};

  

let stringMap2 : Map2 <string> = {

	key: "hello"

};

  

// 제네릭 인터페이스 활용 예시

// 유저 관리 프로그램 , 유저구분 : 학생 , 개발자

  

interface Student {

	type : 'student';
	
	school : string;

};

  

interface Developer {

	type : 'developer';
	
	skill : string;

};

  

interface User<T> {

	name : string;
	
	profile : Student | Developer;

}

  

function goToSchool(user:User<Student>){

	if(user.profile.type !== 'student'){
	
		console.log('???');
		
		return;

	}

	const school = user.profile.school;

	console.log(`${school}로 완료`);

}

  

const developer1 : User<Developer> = {

	name : 'ㅇㅇ',
	
	profile : {
		type : "developer",
		skill : "TypeScript",
	},

};

  

const studentUser : User<Student> = {

	name : 'ㅇㅇ',
	
	profile : {
	
		type : "student",
		
		school : "ㄹㄹ",
	
	},

}

  

goToSchool(developer1);
```
## 제네릭 클래스
```typeScript
class List<T> {

constructor(public list: T[]){}

  

push(data : T){

this.list.push(data);

}

pop(){

return this.list.pop();

}

print(){

console.log(this.list);

}

}

  

const numberList = new List([1,2,3]);

numberList.pop();

numberList.push(4);

numberList.print();

  

const stringList = new List(['1','2']);
```

클래스 또한 제네릭을 적용 할 수 있음. (자바랑 같음 단, 와일드 카드 같은건 없음)

## 프로미스
```typeScript
interface Post {

	id : number;
	
	title : string;
	
	content : string;

};

  

function fetchPost(): Promise<Post>{

	return new Promise((resolve,reject) => {
	
		setTimeout(() => {
		
			resolve({
		
				id : 1,
		
				title : 'dㅇ',
		
				content : 'ㄴㄹㅂ',
		
			});
		
		},3000);
	
	});

}

  

const postRequest = fetchPost();

postRequest.then((post) => {

	post.id;

})
```
function 자체에 타입과 제네릭을 설정해 post 를 호출할 때 타입 에러가 발생하지 않도록 할 수 있다.