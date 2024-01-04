# Operator 연산자
유효성 검사 

예시 ) 사용자로부터 문자 1개 입력 > 영어 소문자인지 검사\

우선 시나리오 
 1. BufferedReader 생성, 
 2. 안내 메세지 출력, 
 3. 입력 > 문자 1개, 
 4. 유효성 검사, 
 5. 결과 처리 + 출력
```java
BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

System.out.println("문자 입력: ");
int code = reader.read();
String result = (code >=97 && code <= 122) ? "올바른 문자" : "올바르지 않은 문자";

System.out.printf("입력한 문자 '%c'는 '%s'입니다.\n", code, result);
System.out.println(100 >= 97); // code >= 97;

System.out.println(100 >= (int)'a');

System.out.println(100 >= 'a'); // 암시적 변환

String result1 = (code >='a' && code <= 'z') ? "올바른 문자" : "올바르지 않은 문자"; // 가독성 높임

System.out.printf("입력한 문자 '%c'는 '%s'입니다.\n", code, result);
// 영어 소문자 , 대문자

String result2 = (code >='a' && code <= 'z')| (code >='A' && code <= 'Z') ? "올바른 문자" : "올바르지 않은 문자"; // 가독성 높임

System.out.printf("입력한 문자 '%c'는 '%s'입니다.\n", code, result);
```

**read() vs readline()**

// read(): 1문자, 문자코드 값이 필요 할 때

// readLine() : N 문자, 문자 코드값 알아내기가 번거로움

