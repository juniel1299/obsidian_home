# BufferedReader

> System.in.read(); 는 한 글자만 되는 반면 BufferedReader의 경우 유니코드(한글) 가능
> 문장 입력 가능
> readLine은 숫자를 받아도 문자열인 String으로 동작함 (int 못 씀)

예시 
// 요구사항 ) 사용자로부터 문자 1개를 입력받아 화면에 출력

  

*도구에 대한 선언을 해야 동작 가능 , -> 패키지에 맞는 명령어 (import) 즉 라이브러리를 가져와야함.*
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

