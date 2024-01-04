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

