# 자바스크립트의 클래스
자바에서 사용하는 Class와 거의 동일함 

필드 : 클래스가 만들어낼 객체의 프로퍼티 
생성자 : 클래스를 호출하면 실제로 객체를 생성하는 함수 
클래스 호출 및 객체 생성에는 new 키워드 필요 
클래스를 이용해서 만든 객체 => 인스턴스 

자바랑 거의 같음 ..

# 타입스크립트의 클래스
```typeScript

class Employee {

	//필드
	
	name: string;
	
	age : number;
	
	position : string;

  

	//생성자

	constructor(name:string, age:number, position:string) {
	
		this.name = name;
		
		this.age = age;
		
		this.position = position;
	
	}
	//메서드
	work(){
		console.log('일함');
	}
};
```

생성자를 만들지 않으면 초기값이 없어서 에러가 발생 (만약 "" 같은 null을 넣어도 가능은 하지만 일반적으로 생성자 사용)

또한 클래스는 그 자체로 타입으로 사용이 가능함 
( const employeeB = new Employee )  
employeeB 의 타입은 Employee 가 됨 
