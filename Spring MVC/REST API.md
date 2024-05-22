REST API


1. 새 프로젝트
- Project name: "RESTfulTest"
- Templates: Spring MVC Project
- Enter a topLevelPackage: "com.test.rest"


2. 스프링/자바 버전 변경하기
- pom.xml
- <org.springframework-version>5.0.7.RELEASE</org.springframework-version>
- <java-version>11</java-version>
- <source>11</source>
  <target>11</target>
- 패키지 탐색기 > 우클릭 > Properties > Project Facets > Java > 11


3. 서블릿/JSP 버전 변경하기
- pom.xml
<dependency>
	<groupId>javax.servlet</groupId>
	<artifactId>javax.servlet-api</artifactId>
	<version>3.1.0</version>
	<scope>provided</scope>
</dependency>
<dependency>
	<groupId>javax.servlet.jsp</groupId>
	<artifactId>javax.servlet.jsp-api</artifactId>
	<version>2.3.3</version>
	<scope>provided</scope>
</dependency>





REST API, RESTful Service
- REST, Representational State Transfer
- 웹상의 자원(문서, 이미지, 동영상, 데이터 등)을 자원명으로 표시해서 자원의 상태를 주고 받기 행위
- HTTP URI를 통해서 자원을 명시하고, HTTP Method를 통해서 자원에 대한 CRUD 처리하는 방식
- 기존에 생성하는 URL의 형식(X) > 별도의 규칙을 만족하는 URL을 생성(O)

URI 작성
1. 기존 방식
- GET	 http://localhost/member/list.do		목록보기
- POST	 http://localhost/member/add.do			추가하기
- POST	 http://localhost/member/edit.do?seq=1	수정하기
- POST	 http://localhost/member/del.do?seq=1	삭제하기
- GET	 http://localhost/member/list.do?w=검색어 검색하기

2. REST
- GET 	 http://localhost/member				목록보기
- POST	 http://localhost/member				추가하기
- PUT	 http://localhost/member/1				수정하기
- DELETE http://localhost/member/1				삭제하기
- GET	 http://localhost/member/검색어			검색하기

REST API 설계 규칙
1. URI에서 자원을 표시한다.
2. URI에 동사를 표시하지 않는다.(행동 표시(X))
3. HTTP Method를 사용해서 행동을 표시한다.
	a. GET: 	리소스 요청
	b. POST: 	데이터 전달 + 서버측 생성
	c. PUT: 	데이터 전달 + 서버측 수정(전체 수정)
	d. PATCH: 	데이터 전달 + 서버측 수정(일부 수정)
	e. DELETE: 	데이터 삭제
4. URI + HTTP Method = 완성
5. 구분자는 '/'를 사용한다.
6. URI의 마지막에 '/'를 적지 않는다.
7. '-' > 사용 가능(가독성)
8. '_' > 사용 비권장(가독성)
9. 확장자를 사용하지 않는다.
10. REST API의 요청 결과(반환값)는 순수 데이터만 반환한다.
	- 기본 방식: 페이지를 반환 > 브라우저 출력
	- REST 방식: 순수 데이터를 반환 > 다양한 클라이언트들이 제각기 목적과 상황에 맞게 데이터를 사용



REST API 구현 서비스
1. Ajax 용
2. Open API 












