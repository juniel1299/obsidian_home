# 자바스크립트의 함수
**JavaScirpt는 자료형을 명시적으로 표현이 불가능하다**
- number, string, boolean, object

Java에서의 Method
```java

public \[static\] int m1(int num){
return 10;
}
```

JavaScirpt에서의 Method (자바스크립트는 클래스가 없음)
```js
function m1(num){
return 10;
}
```


## argument 내장 배열
자바스크립트가 스스로 만들어서 제공해주는 배열 
함수의 실인자들을 저장하는 내장 배열 

```js 
function m2(name){
console.log(argument[0]);
console.log(argument[1]);
}
m2('홍길동');
```
**undefined > 변수 생성 후 초기화가 안 된 상태**




