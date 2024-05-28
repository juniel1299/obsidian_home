JSP 설정
- build.gradle(pom.xml)
	- 의존성 정의 > configuration를
		a. compileOnly > 컴파일시에만 사용 빌드 시 jar에 포함하지 말 것, > 빌드 포함(X) > 실행 파일  용량 줄이기 
		b. runtimeOnly >런타임에만 사용 , 컴파일엔 안 씀 , 코드 작성 시 참조 불가능 
		c. annotationProcessor > 어노테이션 프로세서 사용하는 라이브러리 
		d. implementation > 컴파일 사용 + 런타임 사용 
		e. testCompileOnly > 테스트 코드 컴파일 할 때만 사용
		f. testRuntimeOnly > 테스트 런타임 할 때만 사용
		g. testImplementation > 테스트 코드 컴파일 + 런타임 사용
		h. developmentOnly