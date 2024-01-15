


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

이렇게 Type이 맞지 않아 발생할 수 있는 에러 중 하나가 오버플로우이다. 

