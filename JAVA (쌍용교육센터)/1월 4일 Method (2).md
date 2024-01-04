# Method 
public static void hello() {}에서

void > 반환 타입 
hello > 메서드명 
***메서드명은 캐멀 표기법으로 한다. 맨 앞은 소문자, 키워드 앞글자 대문자***
() > 인자 리스트

## 메서드 인자리스트
>파라미터 (parameters)
>인자(arguments)
>매개변수

예시)
요구사항)// 요구사항) '홍길동'에게 인사를 하는 메서드를 구현하시오.

// 요구사항) '아무개'에게 인사를 하는 메서드를 구현하시오.

// 요구사항) '테스트'에게 인사를 하는 메서드를 구현하시오.

// 요구사항) 강의실 모든 사람에게 인사를 하는 메서드를 구현하시오.

```java
public static void checkScore(int kor, int eng, int math) { //매개변수를 늘릴 때 , 를 이용하면 된다.

int total = kor + eng + math; //총점

double avg = total / 3.0;

String result = avg >= 60 ? "합격" : "불합격";

System.out.printf("평균 점수 %.1f점은 %s입니다. \n",avg,result);

}

  

public static void checkAge(int age) {

String result = age >= 18 ? "통과" : "거절";

System.out.printf("입력한 나이 %d세는 %s입니다.\n", age, result);

}

public static void hello() {

System.out.println("홍길동님. 안녕하세요.");

}

public static void hello2() {

System.out.println("아무개님. 안녕하세요.");

}

public static void hello3() {

System.out.println("테스트님. 안녕하세요.");

}

  

public static void helloEveryOne(String name) { //가인자 (Formal Args)

//String name = "홍길동";

System.out.println(name + "님. 안녕하세요.");

}
```

## 문서 주석 
> /** 하면 @param 형식으로 옆에 작성가능,  주석이 달려서 옴 

