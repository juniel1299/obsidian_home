
# 재귀 메서드 (Recursive Method)

재귀 구조를 가진 메서드이다. 

메서드 구현부에서 자기 자신을 호출하는 메서드

파일 디렉토리 구조와 트리 구조에서 많이 사용함 

// 예제 ) 요구사항) 팩토리얼 메서드를 구현하시오


```java

public static void main(String[] args) {
int n = 4;

int result = factorial(n); //factorial 블럭 후 F3 누르면 선언된 위치로 이동

printFactorial(n, result);


m3(n);

result = m4(n);
} //main 

private static int m4(int n) {

// TODO Auto-generated method stub

return 0;

}

  

  

  

private static void m3(int n) {

// TODO Auto-generated method stub

}

  
public static int factorial(int n) {

return (n == 1) ? 1 : n * factorial(n-1);

}
  

  

public static void printFactorial(int n, int result) {

System.out.printf("%d! = %d\n",n, result);

}
```

