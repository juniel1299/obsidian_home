# Spring Boot
- Spring Project 중 하나 
- 기존 스프링 생성 + 설정 > 단순화 > 초기 진입 장벽 낮춘 기술 
- 개발 환경에 독립 실행 가능한 톰캣 내장 > 배포 용이
- Spring Initialzr


실행
- com.test.bootbegin > bootbegin + application > BootBeginApplication.java

Spring Boot 프로젝트 구조 
- src/main/java 
	- 이전과 동일 > 자바 소스 폴더 > 패키지 + 소스(.java)
	- BootBeginApplication.java > 메인 클래스 (main() 소유) , 시작점

- src/main/resources 
	- static
		- 정적 웹 자원(HTML,CSS,JavaScript,이미지 등)
		- 루트 컨텍스트 밑에 바로 적으면 됨 
	- templates
		- 이전의 views 폴더 
		- 뷰 파일 저장 
	- application.properties + Java Configuration
		- 스프링 부트의 대부분 설정
		- application.properties
		- application.yml

- src/test/java
	- 단위 테스트
	- 단위 테스트를 위한 설정이 이미 완료

- build.gradle
	- Gradle 빌드 도구의 설정 파일
	- pom.xml 과 같은 역할  