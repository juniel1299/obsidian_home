# 형변환 , 자료형변환

> Promotion , Casting
> 하나의 자료형을 다른 자료형으로 변환시키는 작업
> 코드 작성을 유연하게 하기 위해서 사용
> 	- int > double
> 	- float > short

## 암시적 형변환 (자동 형변환) , Promotion
> 큰형 = 작은형 > short = byte (형변환에 읽는 데이터량과 무조건 관련은 없음 뒤에 예시있음)
> 100% 되는 경우임. [자동으로 동작함] 

## 명시적 형변환 (강제 형변환) Casting
> 작은형 = 큰형 
> 경우에 따라 될 수도 있고 안 될 수도 있음.
> short 2byte , byte 1byte 이므로 
> byte = short 로 코드로 짜게 되면 
> 오른쪽에 있는 내용을 왼쪽에 복사를 하는데 
> short는 2칸 , byte는 1칸 이므로 0~9까진 동작하지만 
> 10부터는 byte 입장에서 자리가 모자름 > 에러 발생

*암시적 형변환 예시*

**컴파일러 자체에서 컴파일할 때 s1 = (short)b1; 의 형태로 알아서 바꿔줌 > 오류가 나지 않고 동작함**
```java
byte b1;

short s1;

b1 = 10; // 원본

// 자동형변환 예시

// LValue = RValue , ** 왼쪽과 오른쪽의 자료형은 무조건 같아야한다.

// 왼쪽은 공간 오른쪽은 값이므로 b1 값 10을 s1에도 삽입

//(short = Byte인데 오류가 안나는 이유)

//(자료형) : 형변환 연산자

// 범위가 작은 값에서 큰 값으로 넣을 땐 문제가 없음 > short는 2byte , byte는 1byte 이며

// 컴파일러 자체에서 컴파일할 때 s1 = (short)b1; 의 형태로 알아서 바꿔줌 > 오류가 나지 않고 동작함

// s1 = (short)b1; -> short = short 로 자료형이 양쪽이 맞춰짐 .

s1 = b1;

System.out.println(s1); // 복사본
```

*명시적 형변환 예시*
b2는 byte , s2는 short 이므로 
byte = short 
```java
byte b2;

short s2;

s2 = 10; //원본

//byte(1) = short(2)

// 작은형 = 큰형

// 이러한 경우 큰형 = 작은형처럼 자동으로 되지 않음

//b2 = s2;

b2 = (byte)s2; // 이렇게 수정해야함

System.out.println(b2); // 복사본
```
