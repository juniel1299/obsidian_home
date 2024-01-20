
# 지역 변수와 멤버 변수


변수가 선언이 된 지점에 따라 둘이 나뉨 

## 멤버 변수 (MemberVariable)

선언 위치가 클래스영역인 만큼 해당 클래스안에서 변수를 공유하게 됩니다.

지역 변수는 메서드 내에서 선언하여 메서드 블럭을 넘어가게 되면 소멸이 되는 반면 멤버 변수는 소멸이 되지 않기 때문에 보다 더 신중하게 사용하여야 합니다.
## 지역 변수 (LocalVariable)

선언한 지역에서만 사용되는 변수 

즉 메서드 내부에서 선언하면 해당 메서드 내부에서만 변수 선언이 됨 

지역 변수의 생명주기 (Life Cycle)은 
변수 선언문이 작성되는 시점에 생성이 되어 
변수 선언문이 포함된 블럭을 빠져나갈 때 소멸이 된다

**main 메서드의 변수는 소멸이 상대적으로 늦기 때문에 메모리량이 증가한다**

---

물론 인스턴스 , 파이널 변수 등 더 많은 변수가 있지만 가장 대표적인 두 변수만 작성하였다.

지역변수 예시 
```java
public static void main(String[] args) {
int a = 10; // 지역 변수

int c = 50;

int num=100;

}

public static void aaa() {

int a = 10;

bbb();

}

public static void bbb() {

if(a>5) {

System.out.println("a는 5보다 큽니다");

}

}


```

![결과](https://github.com/juniel1299/juniel1299.github.io/assets/62318700/13b98f21-f231-4c45-b52f-a407caa3e268)

int a = 10; 으로 a가 선언이 되어있지만 bbb 메서드에서 a가 선언이 필요하다고 빨간 줄이 생성이 되어있는 모습을 볼 수 있다.



멤버변수(static)의 예
```java

public class LocalVariable {

  

int b = 20;

public static void main(String[] args) {

}



public void bbb() {

if(b>5) {

System.out.println("a는 5보다 큽니다");

}
```