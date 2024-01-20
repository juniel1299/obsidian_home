# 메서드 오버로딩 (Method Overloading)
같은 이름의 메서드를 여러개 만드는 방법

메서드의 인자 리스트를 다양한 형태로 구성하여 같은 이름의 메서드를 여러개 만듬 

매개변수의 개수 , 매개변수의 자료형을 통해 여러개 만들 수 있음 
단, 매개변수의 이름, 반환값의 자료형을 가지고는 만들 수 없음


예시)
> 1. public static void test(){} // 가능
> 2. public static void test(){} // 불가능 (1번과 겹쳐서 안 됨)
> 3. public static void test(int n){} //가능 
> 4. public static void test(int m ){} //불가능 , 3번과 겹침
> 5. public static void test(int n, int m){} // 가능 (인자를 2개 받아야 하기 때문에 안 겹침)
> 6. public static void test(String m ){} // 불가능 (참조형 안 됨)
> 7. public static int test () {} //불가능 1번과 겹침


예시 

```java

drawLine();

drawLine();

drawLine("+");

System.out.println("");

drawLine("-");

System.out.println("");

drawLine("*");

System.out.println("");

drawLine("^");

System.out.println("");


public static void drawLine() {

System.out.println("==========");

System.out.println("");

}

  

public static void drawLine(String c) {

  

System.out.print(c);

System.out.print(c);

System.out.print(c);

System.out.print(c);

System.out.print(c);

System.out.print(c);

  

}
```

![출력](https://github.com/juniel1299/juniel1299.github.io/assets/62318700/9bd28dab-07e3-4f8b-a223-454867c3ebf0)

메서드 명은 같은 drawLine 이지만 안에 값을 넣으니 아래쪽에 있는 메서드가 기존 메서드를 덮어쓰기 한 것 처럼 
위의 메서드가 출력되는 것이 아닌 아래의 메서드가 출력이 된다.