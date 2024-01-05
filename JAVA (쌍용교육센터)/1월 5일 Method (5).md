# 재귀 메서드 Recursive Method
>재귀 구조를 가진 메서드
>메서드 구현부에서 자기 자신을 호출하는 메서드 
>어려움 > 머리 속에서 상상이 어려움
>파일 디렉토리 구조 또는 트리구조에서 많이 사용함

예제 ) 팩토리얼 메서드 구현하라 4! 
```java
int n = 4;

int result = factorial(n); //factorial 블럭 후 F3 누르면 선언된 위치로 이동

printFactorial(n, result);
// 이클립스 기능으로 메서드 작성

// 메서드에 넣고 싶은 범위 블럭 > 우클릭 > 리팩터 Method

// 변수 관계, 반환까지 다 해줌
printNumber();
//m3 메서드 만들기

//m3(n); 후 ctrl + 1 누르면 create 나옴

m3(n);

result = m4(n);
}//main

  

  

  

private static int m4(int n) {

// TODO Auto-generated method stub

return 0;

}

  

  

  

private static void m3(int n) {

// TODO Auto-generated method stub

}

  

  

  

public static void printFactorial(int n, int result) {

System.out.printf("%d! = %d\n",n, result);

}

  

  

  

public static void printNumber() {

System.out.println("하나");

System.out.println("둘");

System.out.println("셋");

}

public static int factorial(int n) {

return (n == 1) ? 1 : n * factorial(n-1);

}

public static void m1() { //재귀 메서드

System.out.println("메서드1");

m1(); // 본인이 본인을 호출 > 재귀 호출

}

}

//StackOverFlow > 메모리 공간을 다 써서 더이상 동작 불가능해 발생하는 오류
```