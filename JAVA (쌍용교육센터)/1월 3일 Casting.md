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
>	- 정수형 리터럴은 int이다
>	- 실수형 리터럴은 double이다.

명시적 형변환 예시 
```java
//명시적 형변환

byte a1 = (byte)10; // 원래는 해야하지만 자동으로 맞춰줌

//short a2 = 10;

short a2 = (byte)10;

int a3 = 10;

// 큰형 = 작은형

// 암시적 형변환 ,

long a4 = 10;

// 명시적 형변환 (실수)

//float f1 = 3.14; 작은형 = 큰형

float f1 = (float)3.14; // float = double이므로 변환해줘야함

float f2 = 3.14F; // 또는 뒤에 F

double f3 = 3.14F; //double = float -> 8 = 4 이므로 암시적 형변환
```

## 정수와 실수 변환 

예시 ) 실수 = 정수 
```java
// 실수 = 정수 형태 , 암시적 형변환 > 안전 , 비트 수가 같으므로

int n1 = 100; // 원본 (4)

float n2; //복사본(4)

n2 = n1;

System.out.println(n2);

int n3; //복사본(4)

float n4 = 100; //원본(4)
```

예시 ) 정수 = 실수
**데이터 크기는 둘 다 4byte로 같지만 float의 경우 소수점 아래 범위까지 표현이 가능하므로 int보다 더 넓은 범위를 가지고 있어 명시적 형변환을 해야함**
```java
int n3; //복사본(4)

float n4 = 100; //원본(4)

// 정수 = 실수 형태 , 명시적 형변환

//n3 = n4;

// 분명 비트는 같지만 실수는 소수점 아래 범위까지 존재하므로 int 데이터 비트 안에 들어갈 수 없음. (실제 수의 범위)

n3 = (int)n4;

System.out.println(n3);
```
**비트가 더 큰 long 이어도  float는 소수점 아래까지 표현이 가능하므로 명시를 해야함**
```java
long n5;

float n6 = 10;

//long (8) = float(4)

//n5 = n6;

//비트 크기 자체는 long이 더 크나, float은 소수점 아래 범위까지 수를 넣기 때문에 long에 비해 범위가 넓음.

n5 = (long)n6;

System.out.println(n5);
```

***정수와 실수간의 크기 비교는 단순한 메모리 크기가 아닌, 실제 저장하는 수의 범위로 비교한다.***

*//byte(1) < short(2) < int(4) < long(8) <<<< float(4) < double(8)*

예시 ) char 형변환 
```java
//char 형변환

char c1 = 'A'; //겉으로는 문자 하나를 넣는 자료형이지만 내부에는 숫자임

System.out.println(c1); // 문자 출력

System.out.println((int)c1); //숫자로 출력이 됨

System.out.println((char)65); //숫자를 char 형변환하여 문자로 출력
```
예시2) char 형변환 
**같은 2byte여도 char가 더 큰 범위라고 인식하여 명시적 형변환을 하여야 함**
```java
char c2; // 2byte

short t2; //2byte

c2 = '가';

//문자 코드값으로 변환

// short = char , 작은형 = 큰형이라 인식하여 오류 , 명시적 형변환 필요 , char가 더 큰 범위라고 인식함.

//t2 = c2;

t2 = (short)c2;

System.out.println(t2);
```

예시3) char 형변환
```java
char c2; // 2byte

short t2; //2byte

c2 = '가';

//문자 코드값으로 변환

// short = char , 작은형 = 큰형이라 인식하여 오류 , 명시적 형변환 필요 , char가 더 큰 범위라고 인식함.

//t2 = c2;

t2 = (short)c2;

System.out.println(t2);

char c3;

short t3;

t3 = 65;

// char = short 작은형 = 큰형이라 인식하여 오류, 명시적 형변환이 필요

//c3 = t3;

c3 = (char)t3;

System.out.println(c3);
```

> short 는 -32768 ~ 32767 , char 는 0 ~ 65535 범위임.
> - 결국 0~32767 이외는 범위 밖임 > 0 밑으로 갈 시 언더플로우 , 32767 위로 갈 시 오버플로우가 발생함.
> - 결국 데이터가 깨질 수 있음.
> - ex) 가 = 44000임 > short 범위 밖으로 나감 > 가를 넣으면 -21504라는 값이 출력이 됨

**그러므로 char를 형변환 할 땐 반드시 int로 한다.**

오류 예시 )
**값형은 Stack에 값을 두는 반면 참조형은 Heap에 값을 두고 그 값의 위치 (주소)를 Stack에 적어놓으므로** 
*그러므로 값형과 참조형은 서로 형변환을 할 수 없음.*

즉, 참조형 -> 값형으로 바꾼게 아닌 표현임 .

**문자열을 숫자로 바꿀 순 있으나 , 참조형 -> 값형으로 형변환을 
```java
//cannot cast from String to int

//System.out.println((int)"A");
// '을 써서 해야함 .

System.out.println((int)'A');

// 값형은 Stack에 값을 두는 반면 참조형은 Heap에 값을 두고 그 값의 위치 (주소)를 Stack에 적어놓으므로

// 깂형과 참조형은 서로 형변환을 할 수 없음.

// 참조형 -> 값형으로 바꾼게 아닌 표현임. (문자열 -> 숫자로 바꿀 순 있으나 참조형 -> 값형으로 형변환을 할 순 없다)
```
```java
String txt = "100";

int result;

result = Integer.parseInt(txt); // "100" -> 100 문자 -> 숫자

// 100 -> "100" 숫자 -> 문자

String txt2 =String.valueOf(100); //정석 API

String txt3 = 100 + ""; // 한쪽이 숫자, 한쪽이 문자열이면 문자열로 출력이 됨

String txt5 = 3.14 +""; // 실수도 가능

String txt6 = true +""; // true false도 가능.
```

