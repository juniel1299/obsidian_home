# Input 입력

> 콘솔 입력 
> System.in.read(); 
> 간단하게 말하면 System.out.println(); 의 반대 
> *단 1문자만 입력 가능* (1byte만 읽음) -> 연속해서 사용하면 사용한 숫자만큼 늘릴 순 있음.
> 문자 코드값을 반환 
> 한글 미지원 (한글은 2byte 이므로)
> **추후 나오는 BufferedReader 클래스를 통해 해결 가능**

예시 ) 사용자에게 문자 1개 입력 > 화면에 출력하라

> 라벨 출력 > 문자 입력 > 문자를 화면에 출력

예시
```java
System.out.print("문자 입력: ");

  

// 사용자로부터 키보드 입력을 받아서 입력한 문자를 돌려준다.

// 현재 상태 > 사용자가 키를 입력하기를 대기하고 상태

// 사용자가 입력 해야 대기 상태가 해제된다.

  

// 컴퓨터 입력 받는 형식

// 키보드로 A 입력 > 버퍼에 A가 입력 > 프로그램에서 65를 받고 데이터 작성 버퍼에 쓰인 값을 지움

// *A를 입력했을 때 65 65 A 13 10 출력된 이유 > 출력에 작성되어있는 \ % 와 입력할 때 쓰인 엔터키(\n)에 대한 숫자들까지 다 출력한 것*

int code = System.in.read();

  

System.out.println("출력: " + code);

System.out.printf("출력: %c\n", code);

  

code = System.in.read();

System.out.printf("출력 : %d\n", code);

System.out.printf("출력 : %c\n", code);

  

code = System.in.read();

System.out.printf("출력 : %d\n", code);

System.out.printf("출력 : %c\n", code);

  

code = System.in.read();

System.out.printf("출력 : %d\n", code);

System.out.printf("출력 : %c\n", code);

code = System.in.read();

System.out.printf("출력 : %d\n", code);

System.out.printf("출력 : %c\n", code);

code = System.in.read();

System.out.printf("출력 : %d\n", code);

System.out.printf("출력 : %c\n", code);

code = System.in.read();

System.out.printf("출력 : %d\n", code);

System.out.printf("출력 : %c\n", code);

code = System.in.read();

System.out.printf("출력 : %d\n", code);

System.out.printf("출력 : %c\n", code);

  

}

}
```
*A를 입력했을 때 65 65 A 13 10 출력된 이유 > 출력에 작성되어있는 \ % 와 입력할 때 쓰인 엔터키(\n)에 대한 숫자들까지 다 출력한 것* 