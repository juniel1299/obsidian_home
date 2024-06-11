# OAuth 2.0

- 인증 프로토콜
- 제 3자 애플리케이션(네이버 구글 카카오 등등)이 사용자를 대신해서 HTTP 서비스를 이용할 수 있는 권한을 부여하는 기능을 제공


2. 데이터베이스 의존성 주석
- build.gradle

3. 파일 생성
- com.test.oauth2.controller  > MainController.java
						> MyController.java
- templates    > index.html
			> my.html
			> inc > header.html
			



- 인증 필터가 동작하는 주소(관습)
	- 처음 요청하는 로그인 시도 URL
	  - OAuth2AuthorizationRequestRedirectFilter
		  - /oauth2/authorization/서비스명