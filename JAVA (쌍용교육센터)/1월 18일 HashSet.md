

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
먼저 toString