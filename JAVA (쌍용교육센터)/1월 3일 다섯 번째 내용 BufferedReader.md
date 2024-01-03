# BufferedReader

> System.in.read(); 는 한 글자만 되는 반면 BufferedReader의 경우 유니코드(한글) 가능
> 문장 입력 가능
> readLine은 숫자를 받아도 문자열인 String으로 동작함 (int 못 씀)

예시 
// 요구사항 ) 사용자로부터 문자 1개를 입력받아 화면에 출력

  

*도구에 대한 선언을 해야 동작 가능 , -> 패키지에 맞는 명령어 (import) 즉 라이브러리를 가져와야함.*

## 유니코드
```java

BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

//A(65) ~ Z(90)

//a(97) ~ z(122)

//'0'(48) ~ '9'(57)

// 숫자는 2진수 ex 1일때-> 0000001 -> 2^0 = 1 , 문자는 49임.

// \r(13)

// \n(10)

// spacebar (32)

// tab (9)

// backspace(8)
// 완성형 vs 조합형 한글 > 완성형밖에 없음. (완성형: 모든 글자를 이미지로 저장 -> 한계가 존재)

// 가(44032) ~ 힣(55203) > 11172
```

> 
```java
System.out.print("입력: ");

int code = reader.read();

System.out.println(code);

//콘솔로부터 키보드값을 입력받을 수 있는 도구

//System.in.read() 와 같음 -> 단 문자단위 이기 때문에 2글자 이상 사용이 가능 (String)

/*System.out.print("문자 입력: ");

int code = reader.read();

System.out.println(code);

System.out.printf("%c\n", code);

*/
```
```java
// 이름 입력

/* System.out.print("이름: ");

String name = reader.readLine(); // read는 한글자이지만 readline은 입력된 라인 전체를 읽음.

System.out.printf("안녕하세요. %s님\n", name);

// 나이 입력

System.out.print("나이: ");

String age = reader.readLine();

System.out.printf("%s님의 나이는 %s입니다\n", name, age);

*/

```

```java
// 요구사항) 사용자로부터 2개의 숫자를 입력받아 둘을 더하시오

System.out.print("첫번째 숫자: ");

String input1 = reader.readLine();

System.out.print("두번째 숫자: ");

String input2 = reader.readLine();

System.out.println(input1 + input2);
```

## 문자 -> 실제 숫자 (정수)
```java


// 문자열 > 변환 > 숫자

// Integer.parseInt()

// Byte.parseByte()

//Short.parseShort()

//Long.parseShort()

//Float.parseFloat()

//Double.parseDouble()

//Boolean.parseBoolean()

// 1. 어떤 숫자 자료형으로 바꿀 것인가 ex) Integer

// Integer.parseInt();

int num1 = Integer.parseInt(input1); // "10" > 10 문자 10이 아닌 실제 숫자 10으로 바꿔줌

int num2 = Integer.parseInt(input2);

System.out.println(num1 + num2);


```

## 문자 -> 실제 숫자 (실수)

```java
//실수의 경우

double num1 = Double.parseDouble(input1);

double num2 = Double.parseDouble(input2);

System.out.println(num1 + num2);
```