# 서로소 유니온 타입
1. 교집합이 없는 타입들로만 만들었을 때


```typeScript
type Admin = {

	name : string;
	
	kickCount : number;

};

  

type Member = {

	name : string;
	
	point : number;

};

  

type Guest = {

	name : string;
	
	visitCount : number;

};

  
  

type User = Admin | Member | Guest;

  
  

// Admin -> {name} 님이 현재 {kickCount}번 강퇴했습니다.

// Member -> {name} 님이 현재 {point}번 강퇴했습니다.

// Guest -> {name} 님이 현재 {visitCount}번 강퇴했습니다.

function login(user : User){

	if('kickCount' in user){
	
		console.log(`${user.name}님 ${user.kickCount} 번 강퇴했습니다.`);
	
	}
	
	else if('point' in user){
	
		console.log(`${user.name}님 ${user.point} 번 강퇴했습니다.`);
	
	}
	
	else if ('visitCount' in user){
	
		console.log(`${user.name}님 ${user.visitCount} 번 강퇴했습니다.`);
	
	}

}
```

이렇게 해도 동작은 하지만 직관성이 떨어짐 

```typeScript
type Admin = {
	tag : 'ADMIN';
	name : string;
	kickCount : number;
};

  

type Member = {
	tag : 'MEMBER';
	name : string;
	point : number;
};

  

type Guest = {
	tag : 'GUEST';
	name : string;	
	visitCount : number;
};

type User = Admin | Member | Guest;

// Admin -> {name} 님이 현재 {kickCount}번 강퇴했습니다.

// Member -> {name} 님이 현재 {point}번 강퇴했습니다.

// Guest -> {name} 님이 현재 {visitCount}번 강퇴했습니다.

function login(user : User){

switch(user.tag){

	case "ADMIN" :
	
	{
		console.log(`${user.name}님 ${user.kickCount} 번 강퇴했습니다.`);
		break;
	}
	
	case "MEMBER" :
	
	{
		console.log(`${user.name}님 ${user.point} 번 강퇴했습니다.`);
		break;
	}
	
	case "GUEST" :
	
	{
		console.log(`${user.name}님 ${user.visitCount} 번 강퇴했습니다.`);
		break;
	}
	break;
	}
}
```

리터럴 타입 특성을 이용하게 되면 
리터럴 타입 = 교집합이 없음 (그 값 자체가 타입이기 때문에)
-> 구분자로 쓸 수 있음.


## 키 값이 다 다른 경우
```typeScript
const loading : AsyncTask = {

	state : 'LOADING',

};

  

const failed : AsyncTask = {

	state : 'FAILED',
	
	error : {
	
		message : "오류",
	
	},

};

  

const success : AsyncTask = {

	state : "SUCCESS",
	
	response : {
	
		data : "ㅇㅇ",
	
	},
};
```
이렇게 각자 키 값이 다르면 또 ! 를 붙이면서 진행하게 되는데 그러면 관리가 어려워짐 

이럴땐 각각의 타입을 선언해주자. 
```typeScript
type LoadingTask = {

	state : "LOADING"

};

  

type FailedTask = {

	state : "FAILED",
	
	error : {
	
		message : string;
	
	}

}

  

type SuccessTask = {

	state : "SUCCESS",
	
	response : {
	
		data : string;
	
	}

}

  

type AsyncTask = LoadingTask | FailedTask | SuccessTask;

// 로딩중 -> 콘솔 로딩중 출력

// 실패 -> 실패 메세지 출력

// 성공 -> 데이터 출력

  

function processResult(task : AsyncTask) {

switch(task.state){

case "LOADING" :

{

console.log('로딩중');

break;

}

case "FAILED" :

{

console.log(`에러 발생 ${task.error.message}`);

break;

}

case "SUCCESS" :

{

console.log(`${task.response.data}`);

break;

}

}

}
```