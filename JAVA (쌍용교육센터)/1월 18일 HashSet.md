

# HashSet

1.  List
	- 순서가 있는 집합
	- 첨자(방번호)
	- 데이터 중복을 허용함

2. Map
	- 순서가 없는 집합
	- 키(방이름)
	- 데이터 중복 허용

3. Set
	- 순서가 없는 집합
	- 식별자가 없다(방번호,방이름x) > 방을 구분 할 수 없다.
	- 데이터 중복을 허용하지않음(중요)


## HashSet
제네릭"<>"을 사용함 

# HashSet

 1. List 
	- 순서가 있는 집합
	- 첨자(방번호)
	- 데이터 중복을 허용함 ( 방번호가 있어 겹쳐도 구분이 가능하므로)

2. Map
	- 순서가 없는 집합
	- 키(방이름)
	- 데이터 중복을 허용 (방 이름이 있으므로 겹쳐도 구분이 가능함)

3. Set
	- 순서가 없는 집합
	- 식별자가 없다. (방번호x 방이름x) > 방을 구분 할 수 없다.
	- 데이터 중복을 허락하지 않음 (중요) , 대표적으로 로또 문제에서 유리


## HashSet 문법
HashSet은 제네릭 을 사용함

예시
```java
HashSet<String> set = new HashSet<String>();
```

요소를 추가할 땐 add를 이용하며 똑같은 내용이 들어가면 Set안에 추가가 되지 않는다 

예시
```java
HashSet<String> set = new HashSet<String>();

set.add("사과");

set.add("딸기");

set.add("바나나");

System.out.println( set.add("딸기"));
System.out.println( set.size() );

System.out.println(set);
```
![출력]()

딸기가 이미 들어간 상태에서 또 들어가니 false가 출력되는 것을 볼 수 있으며 
size 또한 뒤에 추가된 딸기가 false 이므로 3이 출력되며 
set을 출력하면 사과, 바나나, 딸기 즉 순서에 상관없이 출력이 된다.


요소를 읽을 때 Set은 방을 구분하는 첨자나 키가 존재하지 않기 때문에 따로 읽기 도구를 통해야 하는데 

Iterator 라는 것을 이용해야 한다. (향상된 for문 같은 느낌이다)

```java
Iterator<String> iter = (set.iterator());
```
Set과 똑같이 제네릭을 통해 선언을 해야한다.

```java
HashSet<String> set = new HashSet<String>();

set.add("사과");

set.add("딸기");

set.add("바나나");

Iterator<String> iter = (set.iterator());

System.out.println(iter.hasNext()); // 다음 요소가 존재하는가

System.out.println(iter.next());

System.out.println(iter.hasNext()); // 다음 요소가 존재하는가

System.out.println(iter.next());

System.out.println(iter.hasNext()); // 다음 요소가 존재하는가

System.out.println(iter.next());

  

System.out.println(iter.hasNext()); // 다음 요소가 존재하는가 -> false 없음
```

![출력]()

hasNext를 통해 다음에 요소가 존재하는지 확인을 하고 
next를 통해 요소 하나를 출력한다 (단, 첨자나 번호가 없기 때문에 무조건 순서대로 나오진 않음)

```java

HashSet<String> set = new HashSet<String>();

set.add("사과");

set.add("딸기");

set.add("바나나");

Iterator<String> iter = (set.iterator());

for(String item:set) {

System.out.println(item);

}

```
향상된 for문을 활용하여 간결하게 할 수 있다

ArrayList 같은 경우 값이 겹쳐도 첨자 즉 방번호 개념이 있어 상관이 없는 반면 Set은 숫자가 겹칠 수 없으므로 

숫자가 겹치지 않고, 배열의 형식 > 로또 문제 같은 경우에 강점을 가질 수 있다.(숫자가 겹치지 않게 여러 숫자가 배열안에 들어가야 하는 경우)

# HashSet이 중복을 걸러내는 방식

우선 파일을 두개로 쪼개서 작성을 한 예시이다 

```java
public class Name {

  

private String name;

private int age;

public Name(String name, int age) {

this.name = name;

this.age = age;

}

public String getName() {

return name;

}


public int getAge() {

return age;

}

  

public String toString() {

return String.format("%s(%d)", this.name,this.age);

}


}
```
먼저 toString 과 이름 나이 정의를 Name 파일에 한 후 

```java
HashSet<Member> set = new HashSet<Member>();

Member m1 = new Member("홍길동",20);

set.add(m1);

set.add((new Member("아무개",25)));

set.add((new Member("강아지",4)));

set.add((new Member("고양이",2)));

System.out.println(set.add(m1));

//m1에서 불린 값과 직접 홍길동을 넣은 값이 같은데 출력이 되는 이유

//객체지향인 자바에선

//객체가 구분되므로 m1의 홍길동과 new Member("홍길동",20) 주소값이 다름

//new 작성할 때 인스턴스가 생성되므로 다름

set.add(new Member("홍길동",20)); //동일 인물로 처리하고 싶음

System.out.println(set);

System.out.println();

Member m2 = new Member("유재석", 50);

Member m3 = new Member("유재석", 50);

System.out.println(m2==m3); //사용x (진짜 메모리 주소 값 비교)

System.out.println(m2.equals(m3)); //사용o

//주소값

System.out.println(m2.hashCode());

System.out.println(m3.hashCode());
```

우선 이렇게 한번 찍어보면 
![출력]()

출력 결과를 보면 

처음에 
Member m1 = new Member("홍길동",20); 선언으로 인해 
System.out.println(set.add(m1)); 이 코드에서 false가 출력이 되었다 
그야 똑같은 m1이 한번 더 add로 들어왔으니 당연한거지만 

이후 set.add(new Member("홍길동",20)); 이 코드는 Set  안에 들어가 출력에도 홍길동이 2명이다

그 이유는 아래에 예시 유재석을 보면 알 수 있다 


우선 m2 == m3 가 같냐는 println 에서 false 가 나왔다 똑같은 유재석 50이라는 String과 int값이 들어갔는데 다르다는 것은  

우선 == 은 값형에 대해 비교인데 

참조형은 Heap 공간에 자신의 데이터를 두고 Stack 이라는 부분에 본인이  데이터 값을 두고 온 Heap의 주소를 두는 반면

값형은 Stack 공간에 본인의 실제 값을 둔다 

즉 m2의 주소값과 m3의 주소값이 다르기 때문에 false라 나온 것이며

그래서 참조형에서 비교하는 방식인 equals를 사용했는데도 false가 나오는 것은 

new 라는 선언을 할 때 Heap 공간에 객체가 생성이 되는데
m2 라는 참조형 변수를 만들 때 new를 선언하고 
또 m3라는 참조형 변수를 만들 때 new를 선언하여 

Heap 공간에 각자의 데이터를 생성 해놓았기에 둘은 같지 않다고 false를 출력하는 것이다

이를 같은 값으로 출력하게 하기 위해선 hashCode를 활용해야한다


## hashCode
hashCode는 실제 Heap 주소값을 한 번 정리하여 출력한 값으로 이 hashCode를 