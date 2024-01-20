
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


} //main 

  
public static int factorial(int n) {

return (n == 1) ? 1 : n * factorial(n-1);

}
  

  

public static void printFactorial(int n, int result) {

System.out.printf("%d! = %d\n",n, result);

}
```

n=4를 factorial 메서드에 넣어 4 == 1 이 아니므로 밑에 factorial n-1 자기 자신을 계속 호출 및 리턴을 하여 
4 * 3 * 2 까지 만들고  1일때 1 반환하므로 총

4 * 3 * 2 * 1 = 24라는 값을 result에 삽입하고

그 값을 최종 printFactorial 이라는 메서드에서 출력하게 된다



