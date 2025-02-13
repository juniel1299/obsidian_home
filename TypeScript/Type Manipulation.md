# 타입 조작
- 인덱스드 엑세스 타입 
객체 , 배열 , 튜플 타입에서 특정 프로퍼티 또는 요소의 타입을 추출하는 타입 

- keyof 연산자
특정 객체 타입으로부터 프로퍼티 키들을 모두 스트링 리터럴 유니온 타입으로 추출하는 연산자

- 맵드 타입
기존의 객체 타입으로부터 새로운 객체 타입을 만드는 타입 

- 템플릿 리터럴 타입
스트링 리터럴 타입을 기반으로 정해진 문자열만 포함하는 타입


## 인덱스드 엑세스 타입 
```typeScript
interface Post {

	title:string;
	
	content:string;

	author: {
	
		id:number;
		
		name:string;
		
		age:number;
	
	};

}

  

function printAuthorInfo(author: Post["author"]) {

	console.log(`${author.name} - ${author.id}`);

}

  

const post:Post = {

	title: "제목",
	
	content : "게시글 본문",
	
	author : {
	
		id : 1,
		
		name : "dd",
		
		age : 11,
	
	},

};

  

printAuthorInfo(post.author);
```

속성이 추가가 될 수록 계속 넣어주지 않고 배열처럼 \['author] 적으면 
Post 에서 추가해도 따로 function 부분에 추가 할 필요가 없음 
(특정 속성 타입만 빼오는 방법)

```typeScript
type PostList = {

	title:string;
	
	content:string;
	
	author: {
	
		id:number;
		
		name:string;
		
		age:number;

	};

}[];

  

function printAuthorInfo(author: PostList[number]["author"]) {

	console.log(`${author.name} - ${author.id}`);

}

  

const post:PostList[0] = {

	title: "제목",
	
	content : "게시글 본문",
	
	author : {
	
		id : 1,
		
		name : "dd",
		
		age : 11,
		
	},

};

  

printAuthorInfo(post.author);
```
interface를 사용하지 않을 경우 type 끝나는지점에 \[] 작성

PostList\[0] 은 리터럴 넘버 타입 (숫자 아님..)

PostList\[number]\["author"] 순서대로 추출해야함 ;;

```typeScript
//튜플 방식
type Tup = [number,string,boolean];

  

type Tup0 = Tup[0];

type Tup1 = Tup[1];

type Tup2 = Tup[2];

type TupNum = Tup[number];
```

## keyof 연산자
```typeScript
type Person = typeof person ; 

// keyof 다음은 무조건 타입이 옴.
function getPropertyKey(person : Person, key : keyof Person){ 
	return person[key];

}

  

const person = {

	name : 'ㅇㅇ',
	
	age : 22,

};

  

getPropertyKey(person, "name");
```
keyof 타입 을 사용하게 될 경우 해당 타입 또는 타입 선언된 내부 데이터를 다 가져옴 

typeof 를 타입 정의 시에 사용하게 되면 해당 타입들을 추출 할 수 있음.
```typeScript
  
interface User {
	id : number;
	
	name : string;
	
	age : number;
}

  

type PartialUser = {

	[key in 'id' | 'name' | 'age'] : User[key];

}

  

type BooleanUser = {

	[key in keyof User] : boolean;

}

  

type ReadonlyUser = {

	readonly [key in keyof User]: User[key];

}

  

// 한명의 유저 정보를 불러오는 기능

function fetchUser():User{

	return{
	
		id : 1,
		
		name : 'ㅈㅈ',
		
		age : 22,
	
	};

}

// 한명의 유저 정보를 수정하는 기능

function updateUser(user : User){

//수정하는 기능

  

}

updateUser({

	id : 1,
	
	name : "ddd",
	
	age : 22,

});
```
key in keyof User : boolean 을 진행하게 되면 user 내부 타입 주석이 모두 boolean 으로 적용됨.

## 매ㅂ드