REST API


1. 새 프로젝트
- Project name: "WebSocketTest"
- Templates: Spring MVC Project
- Enter a topLevelPackage: "com.test.websocket"

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

4. Lombok
- pom.xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.30</version>
    <scope>provided</scope>
</dependency>

5. WebSocket
- 웹소켓은 하나의 TCP 접속에 전이중 통신 채널을 제공하는 컴퓨터 통신 프로토콜이다.
- Socket(규격) > 네트워크상의 호스트간의 데이터를 주고 받는 규약
- WebSocket은 ws 프로토콜을 기반으로 클라이언트와 서버 사이에 지속적인 완전 양방향 연결 스트림을 만들어 주는 기술



소켓 동작
- 호스트 A, 호스트B
- 호스트 A > 소켓(전화기) 생성 + IP주소 (+포트번호) > 