스프링 + 웹 프로젝트 + MyBatis > Spring MVC Project

[코드 조각 관리 게시판]

1. 새 프로젝트
- Project name: "Code"
- Templates: Spring MVC Project
- Enter a topLevelPackage: "com.test.code"

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
- pom.xml
\<dependency>
\	<groupId>junit</groupId>
\	<artifactId>junit</artifactId>
\	<version>4.13.2</version>
\	<scope>test</scope>
\</dependency>
\<dependency>
\	<groupId>org.springframework</groupId>
\	<artifactId>spring-test</artifactId>
\	<version>${org.springframework-version}</version>
\</dependency>

5. Lombok
- pom.xml
\<dependency>
\    <groupId>org.projectlombok</groupId>
\    <artifactId>lombok</artifactId>
\    <version>1.18.30</version>
\    <scope>provided</scope>
\</dependency>

6. MyBatis 의존성 추가
\<dependency>
\	<groupId>org.mybatis</groupId>
\	<artifactId>mybatis</artifactId>
\	<version>3.5.2</version>
\</dependency>
\<dependency>
\	<groupId>org.mybatis</groupId>
\	<artifactId>mybatis-spring</artifactId>
\	<version>1.3.2</version>
\</dependency>

\<dependency>
\	<groupId>org.springframework</groupId>
\	<artifactId>spring-tx</artifactId>
\	<version>${org.springframework-version}</version>
\</dependency>
\<dependency>
	\<groupId>org.springframework</groupId>
\	<artifactId>spring-jdbc</artifactId>
\	<version>${org.springframework-version}</version>
\</dependency>

ojdbc8.jar
- 직접 참조

7. HikariCP
- pom.xml
\<dependency>
	\<groupId>com.zaxxer</groupId>
	\<artifactId>HikariCP</artifactId>
	\<version>2.7.4</version>
\</dependency>



8. Log4j
- 로깅 라이브러리
- Log4j \>  Logback \> Log4j2 

- pom.xml \> 기존 log4j 의존성 제거  
- pom.xml > log4j2 의존성을 추가한다.

Log4j2 
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




