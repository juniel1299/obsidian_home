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


HashSet은 제네릭 <> 을 사용함 

HashSet<String> set = new HashSet<String>();

1. 요소 추가 방법 (add)
	set.add("사과");
	set.add("딸기");
	set.add("바나나");


```java
	set.add("사과");
	set.add("딸기");
	set.add("바나나");
	
	System.out.println(	set.add("딸기"));