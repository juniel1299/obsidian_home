// public static void hello()

// void > 반환타입

// hello > 메서드명 > *** 메서드명은 캐멀 표기법 첫글자는 소문자, 이후 단어 첫글자만 대문자

// () > 인자리스트

  

// void == 없다. == null

>메서드 반환값 (반환타입)

```java
int num = test();

System.out.println(num);

System.out.println(checkNumber(10));

System.out.println(checkNumber(3));
```
```java
public static void getName() {

String name = "홍길동";

return; // 메서드 종료만 할 때 , null return 문 > 강제로 메서드 종료

}

public static int getNum() {

  

int num = 100;

  

System.out.println("메서드 종료");

return num; // 메서드 종료 + 값 변환 , 맨 밑에 와야 함 (예외 존재)

}

  

public static String checkNumber(int num) {

// String result = num % 2 == 0 ? "짝수" : "홀수";

// return result;

return num % 2 == 0 ? "짝수" : "홀수";

  

}

  

public static int test() {

int a = 10;

int b = 20;

int c = a + b;

  

return c;

}
```

