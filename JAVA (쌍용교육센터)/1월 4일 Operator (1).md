#  연산자, Operator

>수학 연산자 > 프로그래밍 연산자
>피연산자를 대상으로 미리 정해진 연산(행동)을 한 후에 연산(행동)의 결과를 반환하는 역할
>주로 기호 , 단어 사용

## 연산자 구성
>1. 문장, Statement
>2. . 표현식, Expression
>3. 연산자, Operator
>4. 피연산자, Operand
>5. 연산자 우선 순위
>6. 연산자 연산 방향

### 문장
> 1개 이상의 표현식이 모여 문장을 만든다. 
> int sum  = 10 + 20;

### 표현식
>문장을 구성하는 최소 단위
>int sum
>10 + 20 
>sum = 30 으로 3덩이의 표현식을 가짐 . 

### 연산자 
> + - = 등이 있음.

### 피연산자
> 연산자의 피연산자는 sum 과 30임

### 연산자 우선 순위 

> 하나의 문장 속에서 누가 먼저 실행되는지 정해져있음
> ex) 1+2 * 3 에서 곱하기가 먼저 동작하는 것과 같이 정해져있음.

### 연산자의 연산 방향
> 하나의 문장 속에서 연산자들이 모두 우선 순위가 같을 때 누구를 먼저 실행 할 지 정해져있는 순서

## 연산자 종류
행동에 따른 연산자
> 2. 산술 연산자
> 3. 비교 연산자
> 4. 논리 연산
> 5. 대입 연산자
> 6. 증감 연산자
> 7. 조건 연산자
> 8. 비트 연산자

형태 (피연산자 개수)  
1형 연산자 (단항 연산자)
2항 연산자
3항 연산자 존재 

### 산술 연산자
> + - = / %(mod) 존재
> + 2항 연산자이기도 함 
> + 피연산자는 숫자형이어야 함 (정수 혹은 실수)

예제 
```java
int a = 10;

int b = 3;

  

System.out.printf("%d + %d = %d\n", a, b, a + b);

System.out.printf("%d - %d = %d\n", a, b, a - b);

System.out.printf("%d * %d = %d\n", a, b, a * b);

System.out.printf("%d / %d = %d\n", a, b, a / b);

System.out.printf("%d %% %d = %d\n", a, b, a % b); // %%를 통해 에러 수정 -> Escape

  

double c = 10;

double d = 3;

  

System.out.printf("%.0f / %.0f = %f\n", c, d, c / d);
```
### 산술 연산자의 특징

정수 / 정수 = 정수
실수 / 실수 = 실수
실수 / 정수 = 실수
정수 / 실수 = 실수 

**모든 산술 연산자의 결과값의 자료형 >  두 피연산자의 자료형 중에서 크기가 큰 자료형을 고르게 됨 .**

이유 : 데이터 손실(오버플로우) 방지를 위해 크기가 큰 곳에 맞춰 답이 나오게 된다.

예제)
```java
System.out.println(10 / 3); // 정수 / 정수 = 3 -> 기본값 int 이기 때문에 정수로 나옴

System.out.println(10.0 / 3.0); // 실수 / 실수 = 3.3333 -> 실수 기본 값이 double 이므로

  

System.out.println(10.0 / 3); // 정수 / 실수 = 3.3333

System.out.println(10 / 3.0); // 실수 / 정수 = 3.3333

int e = 1000;

byte f = 10;

System.out.println(e + f); // int + byte = int -> Integer로 변환됨

int g = 1_000_000_000;

int h = 2_000_000_000;

long i = (long)g + h;

System.out.println(i); // int

//System.out.println(1000000000 + 2000000000); // 기본값이 int 이므로 30억은 오버플로우 발생

System.out.println((long)1000000000 + 2000000000); // 앞에 형식을 바꿔줘야함 -> 하나만 해도 됨

byte j = 10;

byte k = 20;

System.out.println(j + k);

//Type mismatch: cannot convert from int to byte

// *** byte와 short 연산의 결과는 항상 int이다.

//byte l = j + k;

byte l = (byte)(j+k); // 이렇게 수정하면 할 수 있으나 대부분 int 사용
```

*오류를 줄이기 위해서 정수는 대부분 int 를 사용 (가끔 long 씀)*
*실수는 대부분 double을 사용함 (정밀도 때문에)*

% 나머지 연산자.
패턴 생성에 주로 쓰임 .
```java
System.out.println(10%2);

System.out.println(9%2);

//달력을 % 를 이용하여 만들 때.

// 1. 만들고자 하는 년,월 > 1일은 무슨 요일?

// 서기 1년 1월 1일 > 월요일

// 2. 만들고자 하는 년 월에 마지막 일?
```

