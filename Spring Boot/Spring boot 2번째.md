JSP 설정
- build.gradle(pom.xml)
	- 의존성 정의 > configuration를
		a. compileOnly > 컴파일시에만 사용 빌드 시 jar에 포함하지 말 것, > 빌드 포함(X) > 실행 파일  용량 줄이기 
		b. runtimeOnly
		c. annotationProcessor
		d. implementation
		e. testComileOnly
		f. testRuntimeOnly
		g. test