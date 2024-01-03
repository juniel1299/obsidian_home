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
>%d , %s , %c %f %b 사이에 숫자 삽입할 수 있음.
>출력할 내용의 너비 지정하기 위함.
>+ 는 우측 정렬
> -는 좌측 정렬이다
> 공백을 넣어 길이를 맞춰 줄 수 있다.

```java
int num = 123;

System.out.printf("[%d]\n", num);

System.out.printf("[%10d]\n", num); //출력내용을 10칸 확보 (숫자가 3개니까 스페이스바 7번)

System.out.printf("[%-10d]\n", num);//음수로 적을 경우 왼쪽에 숫자 오른쪽 공백,

System.out.println();
```

>%f에서만 가능한 기능
>소수점 이하 자릿수 지정하는 방법 
>%.숫자f 

예시1
```java
// 소수점 이하 자릿수 지정

double num2 = 3.14;

System.out.printf("[%f]\n", num2);

System.out.printf("[%.2f]\n", num2); // 소수점 둘쨋자리까지 출력

System.out.printf("[%.0f]\n", num2); // .0 시 정수만 출력

System.out.printf("[%.3f]\n", 3.4567); // 소수점 셋째자리까지 출력 (반올림), 확인 후 작업(***)

System.out.println();
```

> %d와 %f에서만 가능한 기능
> %,d %,f 작성 시 천단위 표기 방식으로 숫자가 작성이 됨 (3칸 지날 때 , 찍힘)

예시
```java
//3. %,d , %,f(%d, %f에만 사용 가능) 자릿수 표기(천단위 표기방식 - 3자리)

int price = 123456;

System.out.printf("[금액 : %,d]",price);

double price2 = 1237.231;

  

System.out.printf("\n[금액 : %,f]",price2);

//천단위 + 소수이하(2자리) + 출력너비 (28자리 , 우측정렬)

double num3 = 1234567.7890123;

System.out.printf("\n[%,20.2f]\n", num3);
```

**정렬 예시**

```java
//메뉴판 출력 > 열 정렬

// 가장 긴거에 맞춰 정렬

System.out.println("================================");

System.out.println(" 음료 가격(단위:원)");

  

System.out.println("================================");

System.out.printf("콜라:\t\t%,6d\n", 2500);

System.out.printf("스무디:\t\t%,6d\n", 3500);

System.out.printf("사이다:\t\t%,6d\n", 500);

System.out.printf("아메리카노:\t%,6d\n", 15000);
```