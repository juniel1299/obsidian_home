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


class ExecutiveOfficer extends Employee {

	//필드
	
	officeNumber : number;
	
	  
	
	//생성자
	
	constructor(name:string,age:number,position:string,officeNumber:number){
	
		super(name,age,position);
		
		this.officeNumber = officeNumber;
	
	}

}
const employeeB = new Employee("ㅇㅇ",22,"ㅇㅇ");
```

생성자를 만들지 않으면 초기값이 없어서 에러가 발생
(만약 "" 같은 null을 넣어도 가능은 하지만 일반적으로 생성자 사용)

또한 클래스는 그 자체로 타입으로 사용이 가능함 
( const employeeB = new Employee )  
해당 내용으로 인해 employeeB 의 타입은 Employee 가 됨 
```typeScript
const employeeC : Employee = {
	name : "",
	age : 1,
	position : '33',
	work(){},
};
```

그로 인해 이렇게 타입을 줄 수도 있음 . 

## 접근 제어자 
- 타입스크립트에서 존재하는 기능 (자바스크립트 x)
- 그냥 자바의 public , private , protected 생각하면 됨 

```typeScript
class Employee {

	//필드
	
	public name: string;
	
	private age : number;
	
	protected position : string;

  

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