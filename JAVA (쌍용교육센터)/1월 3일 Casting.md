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
byte = short 로 short가 byte에 맞춰서 들어가도록 수정해야함.
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

## 오버플로우
> 원본 s3는 2byte -> 16칸 , b3는 1byte -> 8칸인데 
> 형변환을 통해 s3를 byte로 만들게 되면 형변환이 발생하면서 8칸에 맞추기 위해 
> 본인이 가진 16칸 중 8칸을버림 
> 여기서 맨 앞 비트는 부호 (0일때 양수 1일때 음수)를 의미하는데 
> 앞에 8칸을 버리면서 원래 숫자를 나타내던 비트가 맨 앞으로 오면서 음수가 되어버림

예시 
```java
byte b3;

short s3;

s3 = 128;

b3 = (byte)s3;

System.out.println(b3);
```
예시2
```java
//기업은행 > 계좌

int m1;

long m2 = 3000000000L;

//계좌이체

// 형변환을 통해 int = int로 맞춰줌

m1 = (int)m2;

// 앞에 설명과 같이 long은 8byte -> 64bit 총 64칸임 , int는 4byte -> 32bit 총 32칸임

// int = int로 맞춰주는 과정에서 long이 앞에 32칸을 버림

// 원래 숫자를 나타내던 칸이 부호를 나타내는 칸이되며 결과값이 음수로 나오게 되어버림 .

System.out.println("계좌이체결과: " + m1);
```
형변환 정리
>  큰형 = 작은형 (암시형변환)
>  long = int
>  long = byte
>  long = short
>  int = short
>  int = byte
>  short = byte


> 작은형 = 큰형 (명시적 형변환)
> byte = short
> byte = int
> byte = long
> short = int
> short = long
> int = long
> 

long = int

 long = short

long = byte

 int = short

 int = byte

short = byte

작은형 = 큰형 (명시적형변환)

byte = short

byte = int

byte = long

 short = int

 short = long

 int = long

정수형 리터럴은 int이다.

실수형 리터럴은 double이다.