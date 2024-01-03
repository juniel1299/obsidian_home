# 콘솔의 출력

> 콘솔의 입출력 , Console Input Output > IO 라고 부름. 
> 기본 입력 장치 : 키보드
> 기본 출력 장치 : 모니터 

> 콘솔의 출력
> 클래스.필드.메서드 (인자 or 파라미터);
> System.out.println(값); 
> println 메서드는 
> print + line 으로 println 사용시 값을 행단위로 출력  사용시 값 출력 후 엔터를 눌러줌


예시
```java
System.out.println(100);

System.out.println(200);

System.out.println(300);
```

> System.out.print(값); 
> 말 그대로 print 즉 출력만 함 (엔터나 스페이스바 없이 \\n 없으면 쭉 이어서 침)

예시 ) 성적표 출력하기
```java
String name1 = "홍길동";

int kor1 = 100;

int eng1 = 90;

int math1 = 80;

  

String name2 = "아무개";

int kor2 = 95;

int eng2 = 98;

int math2 = 87;

  

System.out.println("\n===============================");

System.out.println(" 성적표");

System.out.println("===============================");

  

System.out.println("[이름]\t[국어]\t[영어]\t[수학]");

System.err.println("===============================");

System.out.print(name1);

System.out.print("\t");

System.out.print(kor1 + "\t");

System.out.print(eng1 + "\t");

System.out.print(math1 + "\r\n");

  

System.out.println(name2 + "\t" + kor2 + "\t" + eng2 + "\t" + math2);
```

> System.out.printf(값); 
> printf 메서드는 
> print format 으로 출력 형식을 제공함 
> String.format() 메서드와 동일한 역할을 함

>printf()
>형식 문자(PlaceHolder 제공)
>가독성 향상 

> 형식에는 
> %s > String
> %d > Decimal (정수) > byte, short, int, long
> %f > float(실수) > float , double
> %c > char(문자(1개))
> %b > Boolean (논리형)

예시1
```java
// 요구사항) "안녕하세요. 홍길동님" 문장을 출력하시오.

String name = "홍길동"; // 사용자가 키보드로 입력한 이름

  

System.out.println("안녕하세요. " + name + "님");

System.out.printf("\n안녕하세요. %s님", name);
```

예시2
```java
// 요구사항) "안녕하세요. 홍길동님. 안녕히가세요 홍길동님" 출력하시오

  

System.out.println("\n안녕하세요. " + name + "님 " + "안녕히가세요 " + name + "님");

System.out.printf("안녕하세요 %s님 안녕히가세요 %s님", name, name);

  

System.out.println();

  

System.out.printf("문자열: %s\n", "문자열");

  

System.out.printf("정수:%d\n", 100);

  

System.out.printf("실수: %f\n", 3.14);

  

System.out.printf("문자: %c\n", 'A');

  

System.out.printf("논리: %b\n", true);

  

System.out.println();

```

>형식 문자는 추가적 기능이 존재
>%d , %c 