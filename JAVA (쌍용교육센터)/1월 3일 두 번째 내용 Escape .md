# Escape Sequence (특수문자)

> 컴파일러가 번역을 할 때, 소스를 문자 그대로 출력하지 않고, 약속된 표현으로 바꿔 출력하는 요소

## \\n  **줄 바꿈 (new line , line feed)**
개행문자 (즉 엔터를 의미)
예시 
```java
String msg = "안녕하세요.\n홍길동입니다.";

System.out.println(msg);
```

## \\r (carriage return)

//캐럿의 위치를 현재 라인의 맨 앞으로 이동

// 키보드 > home 키 역할

예시 
```java
msg = "안녕하세요.\r홍길동";

System.out.println(msg);
```

### 운영체제의 엔터
> 운영체제마다 엔터가 다름
> 1. 윈도우의 경우 \\r\\n 
> 2. 맥의 경우 \\r
> 3. 리눅스의 경우 \\n


```java
System.out.println("하나\r\n둘"); //정석

System.out.println("하나\n둘");
```

## \\t 탭 문자 (tab)

```java
msg = "하나\t둘\t셋";

System.out.println(msg);
```

##  \\b (backspace)

```java
msg = "홍길동\b입니다."; //홍길입니다. [단 이클립스에서 지원x]

System.out.println(msg);

```
## 이미 역할이 있는 문자를 없애는 형태 \\", \\', \\\


예시 
```java
//요구사항] 화면 > 홍길동: "안녕하세요."

msg = "홍길동:\"안녕하세요.\""; // 리터럴 안에는 " 못 씀 > 쓰기 위해선 \"로 붙여야함

//요구사항) 수업 폴더의 경로를 출력하시오 .

msg = "C:\\class\\code\\java"; // 리터럴 안에는 \ 못 씀 > 쓰기 위해선 \\로 써야함

System.out.println(msg);
```

