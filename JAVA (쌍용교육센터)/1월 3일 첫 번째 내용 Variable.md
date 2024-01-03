#  연산자  Variable

>10 + 20 = 30을 만들려고 함 
>A + B  > 이항 연산자 (피연산자 2개)
>연산자 우선순위는 사칙연산 개념과 같음 > 1+2 * 3 에서 곱하기 먼저 계산하듯 
>


**첫 번째 예제**
```java
//ex 1 
System.out.println( a + "+" + b + "=" + (a + b) );
// (a + b) 를 하지 않으면 그냥 1020 이 출력이 됨 그러므로 괄호가 필요함 . 
```
## 진법 , 기수법
> 주민등록번호 입력 > 출력  ex) 950105; 라 할 때


**두 번째 예제 
```java
int jumin1 = 950105;

System.out.println("주민등록번호 " + jumin1);

jumin1 = 030711;

System.out.println("주민등록번호 " + jumin1);
```

```java
//자바의 기수법

// 자바는 10진수 , 2진수 , 8진수 16진수 표현이 가능함

System.out.println(10); //10진수

System.out.println(0xFFF); //16진수 표현시 앞에 0x 붙여야함 > 색상값 표현

System.out.println(010); //8진수 표현시 앞에 0을 붙임 -> 030711 할 때 8진수가 동작하는 이유

System.out.println(0b101); // 2진수 표현시 앞에 0b 붙임
```

## 실수의 리터럴 

```java
double d1 = 1200;

double d2 = 1.2e+3;

System.out.println(d1);

System.out.println(d2);

  

d1 = 0.012;

d2 = 12e-3;

System.out.println(d1);

System.out.println(d2);
```
0.012 라 표현해도 되지만,  
12e-3 즉 12 * 10^(-3) 라는 형태로 표기해도 됨 . 