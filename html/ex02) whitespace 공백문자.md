# WhiteSpace
- 스페이스, 탭, 개행문자 
- HTML 페이지 소스상에 존재하는 모든 공백 문자는 실행기(브라우저)에 의해서 처리되는 규칙 
- 모든 브라우저들을 소스상의 종류와 상관없는 1개 이상의 연속된 공백 문자를 만나면 딱 1개의 스페이스로 치환해서 출력한다 \***



## 공백을 원하는 모습으로 출력하는 방법

1. 스페이스 출력 
	- 공백 문자 1개 > 엔티티 1개 사용 
	- &nbsp; > non break space
	- &엔티티명;
2. 개행 문자 출력 
	- .<br/> 태그 사용
	- line-break 
3. 탭문자 출력
	- 없음