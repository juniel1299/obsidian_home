# 에러 . 
## 에러의 종류
1. 컴파일 에러 : 컴파일 작업 중 발생하는 에러  
	- 컴파일러 발견 > 번역하다가 > 문법이 틀려서 > 발생 > 컴파일 작업 중단 > 프로그램 생성 불가 > 반드시 고쳐야 동작함
	- 난이도가 가장 낮은 에러 > 컴파일러가 오류를 알려줌 > 에러 메세지 
	- 에러 메세지 , 빨간 줄

2. 런타임 에러 : 동작시에 오류가 발생 
	- 런타임(RunTime) > 실행중
	- 컴파일 작업 중에는 없었는데 실행하면 발생하는 에러
	- 문법은 오류가 없음 > 다른 원인으로 발생
	- 예외 (Exception) , 난이도 중간 에러 > 발견 할 수도 있고 못 할 수도 있음
3. 논리 에러 
	- 컴파일 성공 + 실행 성공 > 결과가 이상

> 논리 에러 예시 (본인은 A + B 를 하려 햇는데 오타 )

```java
int n1 = 10;

int n2 = 5;

System.out.println(n1 - n2);

//Arithmetic > 정수에서 많이 뜨는 오류 ,
```

