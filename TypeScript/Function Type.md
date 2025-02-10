# 함수 타입 정의
1. 함수를 설명하는 가장 좋은 방법
2. 어떤 매개변수를 받고, 어떤 결과값을 반환하는지 이야기
3. 어떤 타입의 매개변수를 받아 어떤 타입의 결과값을 반환하는지 ? 

```typeScript
// 일반적인 function 
function func(a:number , b:number) : number {
	return a + b
}

// 람다식
const func1 = (a1:number , b1:number) : number => a+b;

// 함수의 매개변수 (선택적 매개변수)
// 선택적 매개변수 (? 또는 ! 붙는거)는 무조건 맨 뒤로 가야한다.
// 필수적 매개변수는 선ㅌ책적 매개변수 뒤로 갈 수 없음. 

function introduce (name = 'ㅇㅇ',tall? : number) {
	console.log(`dd${name}${number}`);
};

introduce('ㅇㅇ'); // ? 로 인해 or 조건 (있어도 되고 없어도 되는)이므로 가능

// 정해지지 않은 개수의 값을 받을 때 
function getSum(...rest : number[]){

}
```