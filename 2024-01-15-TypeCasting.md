


# 자료형 변환 

암시적 형변환 (Promotion) 과 명시적 형변환(Casting)이 존재하며   

하나의 자료형을 다른 자료형으로 변환 시키는 작업   

코드 작성을 유연하게 하기 위해 사용됨   


## 암시적 형변환 (자동 형변환) (Promotion)

큰 자료형 = 작은 자료형; 의 구조로  
에러 없이 당연하게 되는 형태임   

예시)   

```java

  

public class ttttt {

public static void main(String[] args) {

byte b1;

  

short s1;

  

b1 = 10;

  

s1 = b1;

  

System.out.println(s1);

  

}

}

```

![출력]()


이는 컴파일러 자체에서 컴파일을 할 때 s1 = (short)b1;의 형태로 변환하여 출력하기 때문에  
앞에 형변환을 작성하지 않아도 자동적으로 가능하다.  


## 명시적 형변환(강제 형변환) Casting

작은 자료형 = 큰 자료형; 의 구조로
경우에 따라 가능할 수도 가능하지 않을 수도 있다


예시 
```java
public class ttttt {

public static void main(String[] args) {

byte b1;

  

short s1;

  

b1 = 10;

  

b1 = s1;

  

System.out.println(s1);
}

}
```

![출력]()

Type mismatch 라는 오류가 발생하는 것을 알 수 있다 . 

이를 수정하기 위해선 앞에 자료형을 추가하여 명시적으로 형변환을 하여야 한다. 

예시)

```java
byte b2;

short s2;

s2 = 10; //원본


// 작은형 = 큰형

// 이러한 경우 큰형 = 작은형처럼 자동으로 되지 않음



b2 = (byte)s2; 

System.out.println(b2); // 복사본
```
![출력]()

앞에 (byte) 를 추가하니 바로 정상적으로 동작한다 . 


# 오버플로우 

하지만 Type이 맞지 않는데 명시적 표현을 통해 억지로 자료형을 맞추다 보면 발생할 수 있는 에러 중 하나가 오버플로우이다. 

예시)

```java
int m1;

long m2 = 3000000000L;

m1 = (int)m2;
System.out.println("결과: " + m1);
```
![출력]()

결과 값이 음수로 나오게 되는데 이는 2의 보수 개념을 통해 컴퓨터는 양수와 음수를 나타내는데   

int는 4 byte
long은 8 byte이므로  

long이 작은 공간에 들어가다 보니 비트 자릿수가 안 맞게 되었고 그로 인해 음수 값이 출력이 되었으며  

이를 오버플로우 현상이라고 한다.  

# 정수와 실수 변환

만약 앞에서 말한 byte의 문제라면   
float 와 int 모두 4byte이니 동작 할 것이라 생각 할 수 있다 .


예시)
```java

int n3; //복사본(4)

float n4 = 100; //원본(4)

// 정수 = 실수 형태 , 명시적 형변환

//n3 = n4;

// 분명 비트는 같지만 실수는 소수점 아래 범위까지 존재하므로 int 데이터 비트 안에 들어갈 수 없음. (실제 수의 범위)

n3 = n4;

System.out.println(n3);

```
![출력]()

결과는 Type mismatch라고 뜬다 

분명 둘 다 4byte인데 왜 오류가 발생하는가 라고 하면   

float는 실수형으로 int보다 더 많은 범위의 숫자를 표현 가능하여 범위가 넓으므로 명시적 형변환을 통하여 형변환을 해주어야 한다.    
즉 n3=(int)n4; 를 해야한다.   


마찬가지로 char에서도 명시적 형변환을 해주어야 한다.  
```java
char c2; // 2byte

short t2; //2byte

c2 = '가';

t2 = c2;
```
![출력]()

마찬가지로 Type mismatch가 발생하는데   

이 또한 char가 나타낼 수 있는 범위가 shor
