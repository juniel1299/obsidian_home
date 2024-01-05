# DateTime 
## Date 클래스 , Calendar 클래스 

자바의 날짜와 시간의 자료형 
1. Date 클래스
2. Calendar 클래스
3. java.time 패키지 > 추가 클래스 (상대적으로  최신)

Epoch Time 유닉스 시간 , 시간을 나타내는 방법

시각 > 포인트
시간 > 양 

시각 - 시각 = 시간
시간 + 시간 = 시간
시간 - 시간 = 시간

시간 + 시간 = 시각
시각 - 시간 = 시각

```java
private static void m7() {

// TODO Auto-generated method stub

//현재 시각의 tick

Calendar now = Calendar.getInstance();

System.out.println(now.getTimeInMillis());

//전용 메서드 (현재 시각만 구함)

System.out.println(System.currentTimeMillis());

}

  

  

  

private static void m6() {

// TODO Auto-generated method stub

// 연산

// 시간 + 시간 = 시간

// 시간 - 시간 = 시간

// 2시간 + 1시간 = 3시간

int h1 = 2;

int h2 = 1;

System.out.println(h1 + h2);

// 2시간 30분 + 10분 = 2시간 40분

int hour = 2;

int min = 30;

min +=10;

System.out.printf("%d시간 %d분\n",hour,min);

// 2시간 30분 + 40분 = 3시간 10분

// 2시간 30분 + 10분 = 2시간 40분

hour = 2;

min = 30;

min +=40;

hour = hour + (min / 60); // 2시간 + 1시간 > 자리올림

min = (min % 60); // 나머지 -> 분

System.out.printf("%d시간 %d분\n", hour, min);

}

  

  

  

private static void m5() {

// TODO Auto-generated method stub

//연산

// 시각 - 시각 = 시간

Calendar now = Calendar.getInstance();

Calendar birthday = Calendar.getInstance();

birthday.set(1999, 12, 15, 12, 0, 0);

//Epoch Time 이용 , Tick

// 1970년 1월 1일 0시 0분 0초로부터 몇 밀리초가 흘렀는지 누적값(ms)

System.out.println(birthday.getTimeInMillis());

System.out.println(now.getTimeInMillis());

long gap = now.getTimeInMillis() - birthday.getTimeInMillis();

System.out.printf("살아온 시간: %,dms\n",gap);

System.out.printf("살아온 시간: %,d시간\n",gap/1000 /60 / 60);

System.out.printf("살아온 시간: %,d일\n",gap /1000 / 60 / 60 / 24);

//년과 월은 윤월, 2월 때문에 정확하지 않음.

System.out.printf("살아온 시간: %,d년\n",gap /1000 / 60 / 60 / 24 /365);

// 수료일까지 112일

Calendar end = Calendar.getInstance();

end.set(2024, 5, 17);

System.out.printf("수료일까지 남은 일 : %d\n",(end.getTimeInMillis() - now.getTimeInMillis()) /1000 /60 / 60 / 24 );

// 집에 가려면 몇시간?

Calendar out = Calendar.getInstance();

out.set(Calendar.HOUR_OF_DAY, 17);

out.set(Calendar.MINUTE, 50);

System.out.printf("남은 시간 : %.1f시간\n", (out.getTimeInMillis() - now.getTimeInMillis())/1000.0/60/60 );

  

}

  

  

  

private static void m4() {

// TODO Auto-generated method stub

// 연산

// 시각 + 시간

// 시각 - 시간

//오늘 만난 커플 > 100일 ?

// 오늘(시각) + 100일 = 기념일(시각)

Calendar now = Calendar.getInstance();

System.out.printf("1일차 :%tF\n ", now ); //오늘 출력

now.add(Calendar.DATE, 99); // (기존 값 , 더할 값)

System.out.printf("100일 :%tF\n", now);

// 1주일 전

now = Calendar.getInstance();

now.add(Calendar.DATE, -7);

System.out.printf("일주일전: %tF\n", now);

//컵라면 > 3분 뒤

now = Calendar.getInstance();

now.add(Calendar.MINUTE, 3);

System.out.printf("3분 뒤 : %tT\n", now);

}

  

  

  

private static void m3() {

//TODO > 이클립스에서만 인식, 해야 할 일

// XXX 치명적 문제

// FIXME 오류 해결

//Calendar 메서드

//1. int get(int); : 읽기

//2. void set(값); : 쓰기

// TODO window Show View > task 들어가면 todo 나옴

// window > 설정 > java Task Tag 들어가면 원하는 명칭으로 바꿀 수 있음.

//특정 날짜 생성하기 > 크리스마스 [현재시각을 받고 수정하여 맞추는 방식

Calendar christmas = Calendar.getInstance(); // 현재 시각

System.out.printf("%tF\n",christmas);

//수정

//christmas.set(Calendar.DATE, 25); // 일 수정 , (수정할 데이터 , 수정 값)

//christmas.set(Calendar.MONTH, 11); // 월 수정 (수정할 데이터 , 수정 값)

//System.out.printf("%tF\n",christmas);

// 두번째 방법

//christmas.set(2024, 11, 25);

//System.out.printf("%tF\n",christmas);

//세번째 방법

christmas.set(2024, 11, 25, 18, 30, 0);

System.out.printf("%tF %tT\n",christmas,christmas);

}

  

private static void m1() {

  

// 메인보드 > 시계

// TODO Auto-generated method stub

// Date 클래스

Date now = new Date(); // java.util import 해야함 , now > 컴퓨터의 시각을 가져온다.

System.out.println(now); // 컴퓨터 시계를 가져오는 것이기 때문에 잘 안씀

  

}

  

private static void m2() {

// TODO Auto-generated method stub

  

// Calendar 클래스

Calendar c1 = Calendar.getInstance();

System.out.println(c1);

System.out.println();

  

// 집합 데이터 > 내가 원하는 항목을 추출

  

// int get (int) //숫자 하나를 주면 숫자 하나를 돌려줌

  

int year = 1;

  

// YEAR는 int (숫자형, 파이널변수(불변 상수))

// Calendar.YEAR > 켈린더 상수

System.out.println(c1.get(Calendar.YEAR)); // 2024년

System.out.println(c1.get(Calendar.MONTH) + 1); // 0 > 월(0~11) + 추가로 1 더함

System.out.println(c1.get(Calendar.DATE));// 5 > 일

System.out.println(c1.get(Calendar.HOUR)); // 11 > 시

System.out.println(c1.get(Calendar.HOUR_OF_DAY)); // 11 > 시(24H 표기법)

System.out.println(c1.get(Calendar.MINUTE)); // 9 > 분

System.out.println(c1.get(Calendar.SECOND)); // 35 > 초

System.out.println(c1.get(Calendar.MILLISECOND)); // 0.506 > 밀리초

System.out.println(c1.get(Calendar.AM_PM));// 0/1 > 오전/오후

System.out.println(c1.get(Calendar.DAY_OF_YEAR)); // 5 > 올해 5번째 날

System.out.println(c1.get(Calendar.DAY_OF_MONTH)); // 5 > 이번달 5번째 날

// 일요일이 1, 토요일이 7로 설정이 되어있음.

// 주차는 목요일을 포함하는 것을 기준으로 함

System.out.println(c1.get(Calendar.DAY_OF_WEEK)); // 6 > 이번주 6번째 날 (요일)

System.out.println(c1.get(Calendar.WEEK_OF_YEAR)); // 1 >올해 1번째 주

System.out.println(c1.get(Calendar.WEEK_OF_MONTH)); // 1 > 이번달 1번째 주

  

System.out.println();

System.out.println();

  

// 요구사항] "오늘은 2024년 1월 5일입니다." 출력하시오

// 0월을 지우기 위해 (c1.get(Calendar.MONTH)+1)

System.out.printf("오늘은 %d년 %d월 %d일입니다.\n", c1.get(Calendar.YEAR), (c1.get(Calendar.MONTH) + 1),

c1.get(Calendar.DATE));

  

System.out.printf("오늘은 %d년 %d월 %s일입니다.\n", c1.get(Calendar.YEAR), (c1.get(Calendar.MONTH) + 1),

c1.get(Calendar.DATE) < 10 ? "0" + c1.get(Calendar.DATE) : c1.get(Calendar.DATE) + "");

  

// %02d 하면 2자리를 불러와야 할 때 1자리이면 0으로 채운다.

System.out.printf("오늘은 %d년 %02d월 %02d일입니다.\n", c1.get(Calendar.YEAR), (c1.get(Calendar.MONTH) + 1),

c1.get(Calendar.DATE));

  

System.out.println();

  

// 요구사항) "지금은 오전 11시 36분 49초입니다."

  

System.out.printf("지금은 %s %02d시 %02d분 %02d초 입니다.\n", c1.get(Calendar.AM_PM) == 0 ? "오전" : "오후",

c1.get(Calendar.HOUR), c1.get(Calendar.MINUTE), c1.get(Calendar.SECOND));

  

System.out.println();

  

// printf() > 형식문자 (날짜 , 시간)

System.out.printf("%tF\n", c1); // %tF 사용 2024-01-05 , 형식 고정이라 다른 형식은 위 처럼 만들어야함

System.out.printf("%tT\n", c1); // %tT 사용 11:32:10

System.out.printf("%tA\n", c1); // %tA 사용 금요일 , 지역에 맞는 요일로 출력

  

}

  

}
```