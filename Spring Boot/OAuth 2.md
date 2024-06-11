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


- 인증 서버 > 코드를 반환받아 돌아오는 URL
	- OAuth2LoginAuthenticationFilter
		- /login/oauth2/code/서비스명


5. 소셜 로그인 > 변수 설정
- application.yml


8. OAuth2UserService 응답 받기
- 인증 토큰 받은 뒤 리소스 서버로부터 개인 정보를 받는다
- com.test.oauth2.service > CustomOAuth2UserService
- com.test.oauth2.dto > 


9. 로그인 완료 처리 
-  com.test.oauth2.dto > UserDTO.java
					> CustomOAuth2User.java
					

10. 유저 정보 > DB 저장 
- com.test.oauth2.entity > UserEntity.java
- com.test.oauth2.repository > UserRepository.java

