
Spring Security
- 인증, 허가
- 동작 방식 > 서블릿 필터와 스프링 인터셉터를 사용해서 처리


1. 새 프로젝트
- Project name: "SecurityTest"
- Templates: Spring MVC Project
- Enter a topLevelPackage: "com.test.security"

기본 설정
- MyBatis(HikariCP)
- Log4j2
- JUnit

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

4. jUnit
<!-- Test -->
<dependency>
	<groupId>junit</groupId>
	<artifactId>junit</artifactId>
	<version>4.13.2</version>
	<scope>test</scope>
</dependency>
<dependency>
	<groupId>org.springframework</groupId>
	<artifactId>spring-test</artifactId>
	<version>${org.springframework-version}</version>
</dependency>

5. Lombok
- pom.xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.30</version>
    <scope>provided</scope>
</dependency>

6. MyBatis 의존성 추가
<dependency>
	<groupId>org.mybatis</groupId>
	<artifactId>mybatis</artifactId>
	<version>3.5.2</version>
</dependency>
<dependency>
	<groupId>org.mybatis</groupId>
	<artifactId>mybatis-spring</artifactId>
	<version>1.3.2</version>
</dependency>

<dependency>
	<groupId>org.springframework</groupId>
	<artifactId>spring-tx</artifactId>
	<version>${org.springframework-version}</version>
</dependency>
<dependency>
	<groupId>org.springframework</groupId>
	<artifactId>spring-jdbc</artifactId>
	<version>${org.springframework-version}</version>
</dependency>

7. ojdbc8.jar

8. HikariCP
- pom.xml
<dependency>
	<groupId>com.zaxxer</groupId>
	<artifactId>HikariCP</artifactId>
	<version>2.7.4</version>
</dependency>

9. Log4j2
- 로깅 라이브러리
- Log4j > Logback > Log4j2

- pom.xml > 기존의 log4j 의존성을 제거한다.
- pom.xml > log4j2 의존성을 추가한다.
<dependency>
	<groupId>org.apache.logging.log4j</groupId>
	<artifactId>log4j-api</artifactId>
	<version>2.23.1</version>
</dependency>
<dependency>
	<groupId>org.apache.logging.log4j</groupId>
	<artifactId>log4j-core</artifactId>
	<version>2.23.1</version>
</dependency>
<dependency>
	<groupId>org.apache.logging.log4j</groupId>
	<artifactId>log4j-slf4j-impl</artifactId>
	<version>2.23.1</version>
	<scope>test</scope>
</dependency>
<dependency>
	<groupId>org.bgee.log4jdbc-log4j2</groupId>
	<artifactId>log4jdbc-log4j2-jdbc4</artifactId>
	<version>1.16</version>
</dependency>

- src/main/resources > log4j.xml(삭제) > log4j2.xml
- src/main/resources > log4jdbc.log4j2.properties


10. web.xml
- 필터 추가

11. root-context.xml
- HikariCP
- MyBatis

12. 테스트
- src/test/java > com.test.security > "MapperTest.java"
- "com.test.security.mapper" > "TestMapper.java"(I)


13. Spring Security Dependency 추가
- 4개
<dependency>
	<groupId>org.springframework.security</groupId>
	<artifactId>spring-security-core</artifactId>
	<version>${org.springframework-version}</version>
</dependency>
<dependency>
	<groupId>org.springframework.security</groupId>
	<artifactId>spring-security-config</artifactId>
	<version>${org.springframework-version}</version>
</dependency>
<dependency>
	<groupId>org.springframework.security</groupId>
	<artifactId>spring-security-web</artifactId>
	<version>${org.springframework-version}</version>
</dependency>
<dependency>
	<groupId>org.springframework.security</groupId>
	<artifactId>spring-security-taglibs</artifactId>
	<version>${org.springframework-version}</version>
</dependency>


14. security-context.xml
- "/webapp/WEB-INF/spring/security-context.xml"
- root-context.xml, servlet-context.xml 동일한 설정 파일
- 기존 컨텍스트와 분리해서 구성 추천
- New > Spring Bean Configuration File


15. Security Filter 등록
- web.xml
- 스프링 시큐리티가 스프링 MVC에서 동작할 수 있도록..


16. 실행
- 프로젝트 > Run AS > Run on Server
- 에러 발생 > No bean named 'springSecurityFilterChain' available
- 해결 > web.xml > contextConfigLocation > security-context.xml 등록

- security-context.xml 기본 구문 작성
<security:http>
	<security:form-login/>
</security:http>

<security:authentication-manager>

</security:authentication-manager>

- 다시 실행



17. Security 테스트가 필요한 URI 설계
- "/index.do"	> 인증(O), 인증(X) > 모든 사용자 접근 가능
- "/member.do"  > 인증(O) > 인증받은 사용자(회원)만 접근 가능
- "/admin.do"   > 인증(O) > 인증받은 사용자 중 관리자 권한이 있는 사용자만 접근 가능


18. 파일 추가
- "com.test.security.controller" > "TestController.java"
- views > "index.jsp"
        > "member.jsp"
        > "admin.jsp"
- views > "inc" > "header.jsp"


19. Security 구성 요소
- 인증(Authentication), 허가(Authorization)

- AuthenticationManager
	- 인증 매니저
	- 중심 역할
	- 인증을 담당한다.
	- AuthenticationManager <- ProviderManager <-> AuthenticationProvider
	
- AuthenticationProvider
	- 인증 제공자
	- 실제로 인증 작접을 진행

- UserDetailsService
	- 사용자 정보 + 사용자 권한 > 관리
	- AuthenticationManager <- ProviderManager <-> AuthenticationProvider <-> UserDetailsService


20. 로그인, 로그아웃 + 인증
- security-context.xml 수정

<security:http>
	<security:intercept-url pattern="/index.do" access="permitAll" />
	<security:intercept-url pattern="/member.do" access="hasRole('ROLE_MEMBER')" />
	<security:form-login/>
</security:http>

- pattern: 접근하려는 URI
- access: 허가 처리

- 실행
	- index.do
	- member.do


21. 단순 로그인 처리
- /security/login 자동 생성 로그인 페이지 사용
- 계정 > XML 정의(security-context.xml) > 인 메모리 방식 > 운영(X), 테스트용(O)
- security-context.xml 수정

**** 스프링 시큐리티에서는 username의 의미 > id 개념
- 일반 시스템(userid) == 스프링 시큐리티(username)
- <security:user name="hong" password="1111">

- 실행
- /member.do 로그인 시도
- 오류 발생 > There is no PasswordEncoder mapped for the id "null"
- 스프링 시큐리티 4까지 PasswordEncoder 선택 사항
- 스프링 시큐리티 5까지 PasswordEncoder 필수 사항
- 우선 테스트를 위해서 임시로 PasswordEncoder 무시하게 설정 > password="{noop}1111"

- 다시 실행
- /member.do 시도

- 로그아웃
	- 개발자 도구 > Application > Cookies > JSESSIONID > 삭제



22. 관리자 추가
- security-context.xml
- 관리자 계정 추가
	- <security:user name="admin" password="{noop}1111" authorities="ROLE_ADMIN"/>
- 관리자 허가 설정

- 실행
- 비회원 > member.do, admin.do
- 회원 로그인 > member.do, admin.do
- 관리자 로그인 > member.do, admin.do

- 관리자가 member.do 접근 불가 > 허용


23. 접근 권한 페이지 처리
- 로그인을 안 한 상태에서 접근 불가능한 URI 접근 > 로그인 페이지로 이동
- 로그인을 한 상태에서 접근 불가능한 URI 접근 > 에러발생(403)

23.1 access-denied-handler URI 지정
or
23.2 AccessDeniedHandler를 직접 구현

23.1
- 접근 권한 페이지 추가
	- com.test.security.controller > "AuthController.java"
	- views > "auth" > "accesserror.jsp"

- 위의 URI를 403 오류와 연결하기
	- security-context.xml 수정
	
- 실행

23.2
- "com.test.security.auth" > "CustomAccessDeniedHandler.java"

- 실행


24. 커스텀 로그인 페이지
- 접근 제한 페이지처럼 직접 만든 로그인 페이지의 URI을 지정할 수 있다.

- AuthController.java > URI 추가
- views > auth > "customlogin.jsp"

- <input name="username">, <input name="password"> : name 속성이 예약어
- <form method="POST" action="/security/login"> : POST + URI(예약)

- security-context.xml > 커스텀 로그인 페이지 연결

- 실행 > 실패

- 실패 이유 > CSRF

CSRF, Cross-site request forgery
- <securty:csrf disabled="true" />

- customlogin.jsp > CSRF 토큰 추가
	- <input type="hidden" name="${_csrf.parameterName}" value="${_csrf.token}">


25. 로그인 성공 > 후속 동작 처리
- 로그인을 성공한 후에 특정한 동작을 하고 싶을 때 > Handler 구현
- com.test.security.auth > "CustomLoginSuccessHandler.java"
- security-context.xml > 커스텀 핸들러 연결


26. 로그아웃
- 로그인("/login")의 예약된 URI 처럼 > 로그아웃도 이미 구현된 예약 URI가 있다. > "/logout"
- 커스텀 핸들러 구현
- AuthController.java > URI 추가
- views > auth > "customlogout.jsp"
- security-context.xml 설정 추가





27. 계정 정보
- InMemoryUserDetailsManager 방식
	- \<security:user name="hong" password+"{noop}1111" authorities="ROLE_MEMBER"/\>

- JDBC 기반의 계정 정보
	- 미리 정해진 구조의 스키마 사용 > 편함 + 제약 발생
	- 사용자가 직접 만든 구조의 스키마 사용 > 직접 구현


- SecurityTest > "script.sql"



28. 미리 정해진 구조의 스키마 사용 
	- script.sql > 테이블 생성 + 계정 생성
	- security-context.xml > JDBC 기반의 인증 작업 설정 


29. PasswordEnder 문제 해결 
- 스프링 시큐리티 5 부터 PasswordEnder 사용이 필수
- 위의 상황은 임시로 '{noop}' 붙여서 문제를 잠시 무시
- 데이터베이스를 사용하려면 반드시 PasswordEncoder를 사용해야 한다.
- PasswordEncoder > 암호화 작업 

30. 사용자가 직접 만든 구조의 스키마 사용


31. 사용자 계정 생성하기 
- member + member_auth > 계정 추가 


32. 회원 가입


33. UserDetailsService > 커스텀 
- 