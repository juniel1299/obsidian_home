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
	
	if(user.tag === 'ADMIN'){
	
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