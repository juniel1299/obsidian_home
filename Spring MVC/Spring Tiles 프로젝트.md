Spring Tiles
- Layout 기술


1. 새 프로젝트
- Project name : NonTilesTest
- Templates : Spring MVC Project
- Enter a topLevelPackage : "com.test.nontiles"

1. 새 프로젝트
- Project name : TilesTest
- Templates : Spring MVC Project
- Enter a topLevelPackage : "com.test.nontiles"

구현 기능 
- 메인 (index.do)


- 회원
	- 회원정보(member/info.do)
	- 활동내역(member/history.do)
	- 즐겨찾기(member/favorite.do)



- 관리자 
	- 로그(admin/log.do)
	- 환경설정(admin/setting.do)

파일 생성
- com.test.nontiles.controller \> MainController.java 
						> MemberController.java
						> AdminController.java
						

- views \> index.jsp
		> member > info.jsp
				> history.jsp
				> favorite.jsp
				
- views > admin > log.jsp
			  > setting.jsp
			  







