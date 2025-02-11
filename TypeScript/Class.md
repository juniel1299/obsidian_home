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

자바와 다른점은 class가 아닌 안에 들어있는 객체에도 붙일 수 있음 

기능은 똑같이 
public 이면 모든 곳에서 수정 가능 (접근 가능) 
private 면 해당하는 클래스 내부에서만 수정 가능 (접근 가능)
protected 면 상속 관계에서만 수정 가능 (접근 가능)

```typeScript
employeeB.age = 13;

employeeB.name = 'ㅈㅈ';

employeeB.position = 'ㅂㅂ';
```
즉 위의 코드를 예시로 이 코드들은 age , position 에서 에러 발생. 

```typeScript
class Employee {

//생성자

	constructor(public name:string, private age:number, protected position:string) {}

  

//메서드

	work(){
	
		console.log('일함');
	
	}

};
```
필드를 생략하고 생성자에 public , protected , public 붙이는 것도 가능함. + this 문법 또한 생략 가능