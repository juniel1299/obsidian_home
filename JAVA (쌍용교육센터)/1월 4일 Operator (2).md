# 연산자 Operator

## 비교 연산자
>   , > , >= , <, <=, == (같다) != (다르다) 
>   2항 연산자
>   피연산자들의 우위 (동등) 비교
>   피연산자는 숫자형을 가지게 됨 . 
>   연산의 결과가 boolean 즉 true false로 나옴 


예제
```java
int a = 10;

int b = 3;

  

System.out.printf("%d > %d =%b\n ", a, b, a > b);

System.out.printf("%d >= %d =%b\n ", a, b, a >= b);

System.out.printf("%d < %d =%b\n ", a, b, a < b);

System.out.printf("%d <= %d =%b\n ", a, b, a <= b);

System.out.printf("%d == %d =%b\n ", a, b, a == b);

System.out.printf("%d != %d =%b\n ", a, b, a != b);

  

System.out.println();
```

예제 // 요구사항) 사용자 나이 입력 > 18세 이상이면 통과, 미만 거절

```java
* System.out.println("나이 입력: "); BufferedReader reader = new BufferedReader(new

* InputStreamReader(System.in)); //Ctrl + Shift + O

*

* String input = reader.readLine();

*

* int age = Integer.parseInt(input); // 문자 25 > 숫자 25

*

* System.out.println(age >= 18); System.out.println();
```

> == 와 != 연산자
> 문자열 (참조형) 비교

```java
int n1 = 100;

int n2 = 100;

int n3 = 50;

n3 = n3 + 50;

  

System.out.println(n1 == n2); //결과 true

System.out.println(n1 != n2); //결과 false

System.out.println(n1 == n3); // true

  

String s1 = "홍길동";

String s2 = "홍길동";

String s3 = "홍";

s3 = s3 + "길동";

System.out.println(s1 == s2); //문자열에선 이렇게 비교하면 오류남 

System.out.println(s1 == s3); //문자열에선 이렇게 비교하면 오류남

System.out.println();

System.out.println(s1.equals(s2));

System.out.println(s1.equals(s3)); // s1.equals(s3) 로 해야 문자열 비교가 가능
```

> **문자열의 비교는  ==  != 즉 연산자 사용을 하면 안된다.**

> **문자열의 비교는 equals() 라는 메서드를 이용해야 함**

## 논리연산자
> && (and) , || (or) , ! (not)
> 2항 연산자 && , ||
> 1항 연산자 ! 
> 피연산자의 자료형이 boolean이다.
> 연산의 결과 또한 boolean 이다 . 
> 피연산자를 정해진 규칙에 따라 연산을 한 뒤 값을 반환 

```java
//and 연산자는 둘 다 만족해야함.
A && B = ?

 T && T , T && F, F && T, F && F > 1, 0, 0, 0

  
// or 연산자는 하나만 만족해도 됨
A || B = ?

 T || T, T || F, F || T, F || F > 1, 1, 1, 0

  
// true를 false로 , false를 true로 
 !A = ?

  

 !T , !F 부정연산자 > (결과) 0,1\

// 베타적 논리합 (xor)

// A ^ B = ? 두개의 값이 다르면 true

T ^ T, T ^ F , F ^ T, F ^ F > 0, 1, 1, 0
```

예시 ) 요구사항) 사용자 나이 입력 > 18세 이상이면 통과, 미만 거절
```java
boolean f1 = true;

boolean f2 = false;

  

System.out.println(f1 && f2);

System.out.println(f1 || f2);

System.out.println(!f1);

System.out.println(f1 ^ f2);

  

// 나이 입력 > 18세 이상 + 60세 미만

  

int age = 25;

// System.out.println(18 <= age && age < 60);

System.out.println((18 <= age) && (age < 60));

System.out.println((age >= 18) && (age < 60)); // 가독성을 위해 주인공(변수)을 왼쪽
```

## 연산자 우선 순서

> 순서 : 산술 연산자 > 비교 연산자 > 논리 연산자 

## 대입 연산자, 할당 연산자

> = , +=, -=, /=, %= (복합 대입 연산자)
> Lvalue(변수) = Rvalue(상수 또는 변수)
> Lvalue Rvalue 자료형이 동일해야한다. > 형변환
> 대입 연산자는 모든 연산자들 중 우선 순서가 가장 낮다.
> 대입 연산자는 연산 방향이 오른쪽 > 왼쪽으로 실행한다.

예시 ) 
```java

int sum = 10 + 20 * 3; // 곱하기 > 더하기 > = , 곱하기 계산할 때 20 * 3만 보고 계산  
// 10 + 60 으로 대체가 됨

// 10 + 60 계산 > sum = 70 만 남음 > 70을 sum에 넣음
System.out.println(sum);
```

예시 2 ) 
```java
int m1 = 100;

int m2;

int m3;

  

// m2 = m1; 

// m3 = m1;

  

m3 = m2 = m1; //우선 m1 100 숫자가 m2에 들어감 -> m2의 100이 m3에 들어감 . 
// m1 m2 m3 모두 100이 됨 

// = 연산자는 오른쪽에서 왼쪽이기 때문에 가능함.

System.out.println(m2);

System.out.println(m3);
```
예시 3 )
```java
int n = 10;

  

// n에 1을 추가하시오 > n의 값에 1을 더한 값을 n에 다시 넣어라. > 누적

n = n + 1;

  

System.out.println(n); // 11 나옴

  

n += 5; 

  

System.out.println(n); //16 나옴

n = n - 2;

  

System.out.println(n); //14 나옴

n -= 2; 

  

System.out.println(n); // n= n-2 이므로 12 나옴

  

n *= 2; 
  

System.out.println(n); // n = n*2 이므로 24 나옴

n /= 2;

  

System.out.println(n); // n = n/2 이므로 12 나옴

n%= 3; // 

  

System.out.println(n); // n = n%3 = 나머지 0 나옴 

// n = 10 + n; , n +=10; 은 되지만 n = 10 - n , n-=10; 을 할 경우 n-10 이기 떄문에 논리 에러 발생함. 

// 실행 자체는 되지만 답이 틀리게 나옴 . 
```

## 증감 연산자 
> ++(증가 연산자) , -- (감소 연산자)
> 1항 연산자
> 피연산자는 숫자형을 가진다.
> 누적 연산을 한다.
> 기존 값에 1을 더하거나 뺀다.
> ***연산자와 피연산자 위치를 바꿔서 작성이 가능하다, 순서 주의***
> **연산자의 위치에 따라 연산자 우선 순위가 달라진다.
> ++n : 전위배치 (전치) > 연산자 우선 순위가 가장 높음.
> n++ : 후위배치(후치) > 연산자 우선 순위가 가장 낮음.


예시 1 
```java
n = 10;

++n;

n++;

System.out.println(n); // 10 + 1 + 1 = 12 결과 나옴

--n;

n--;

System.out.println(n); // 12 - 1 - 1 = 10 나옴 


```

예시 2 
```java
n = 10;

int result = 0;

result = 10 + ++n; 

// ++n 이 1순위 이므로 11 이 되고 10 + 11 이므로 최종 21이 나옴
System.out.println(result);


result = 10 + n++;

//n++ 이므로 마지막 순위이므로 10 + n 우선 함 > result = 20 ++ 
// result에 20 넣음 > ++은 역할을 할 수 없어서 그냥 사라짐 > 최종 20이 나옴 
System.out.println(result);


```

## 조건 연산자
> ? : 3항 연산자 ( 유일한 3항 연산자이다.)
> A ? "B" : "C" 의 형태이며
> A 는 boolean으로 조건임 
> true 일 경우 B가 출력되며 , false일 경우 C가 출력됨.
> 

```java
System.out.println(1 + 1);

System.out.println(1243124+ 124568);

System.out.println(true ? "남자" : "여자"); // 남자 출력

System.out.println(false ? "남자" : "여자"); // 여자 출력

age = 25;

System.out.println(age >= 18 ? "통과" : "거절"); // 25 >= 18 이므로 통과

n = 5;

System.out.println(n % 2 == 0 ? "짝수" : "홀수"); // 5를 2로 나누면 1 나옴 false 홀수
```

## 비트 연산자 , (논리 연산자) , 진짜 비트 연산

```java
a = 10;

b = 5;

System.out.println(a & b); // 10 > 1010 (2^3 + 2^1) , 5 > 0101 (2^2 + 2^0) 엔드이므로 1010 , 0101 비교 > 0000

System.out.println(a | b); // 위에 숫자 계산 1111 > 8 + 4 + 2 + 1 = 15
```

템플릿 저장하는 법 

// window > 설정 > Editor temlate > 작성