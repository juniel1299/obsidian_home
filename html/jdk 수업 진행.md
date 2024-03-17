
1. HTML
2. CSS
3. JavaScript


Web 

WWW > World Wide Web 



Network
- 2대 이상의 컴퓨터를 서로 연결해놓은 환경 
- 통신 가능한 환경 
- 관리하는 주체가 있음 


Internet
- Inter-network
- 전세계의 모든 컴퓨터를 서로 연결해놓은 환경  
- 관리하는 주체가 없음 


Web 
- 인터넷 기반
- 서로간의 정보(문서)를 주고 받은 환경 

우리의 목적
- Web 기반의 서비스 구현 


Database 서비스
- 서버 : 오라클 
- 클라이언트 : SQL Developer


Web 구성
- 웹클라이언트 <-> 웹서버
- 웹서버: 문서를 제공함  > 아파치 톰캣
- 웹클라이언트 : 문서를 요청 + 제공받음(소비) > 웹 브라우저(크롬)
	- 웹 클라이언트 (크롬)(Http Request) -> 웹 서버(톰캣)
	- 웹 클라이언트(크롬) <- (HTTP Response) 웹 서버(톰캣)


URI
- Uniform Resource Indentifier


http://www.naver.com:80/member/list.html -url


URL 
- Uniform Resource Locator
- 웹에서 주어진 자원(웹문서, 이미지, 동영상, 파일 등) 의 고유 주소 


1. http:
	- 프로토콜(Protocol) > 통신규약
	- 서로간의 데이터를 주고 받을 때 사용하는 규칙(약속)
	- HyperText(HTML) Transfer Protocol
	- https: + 보안(security)

2. www.naver.com
	- Domain Address
	- 도메인 주소
	- 서버 컴퓨터(호스트)의 주소
	- IP Address 사용

3. IP 
- 인터넷에서 호스트를 구분하는 고유 주소값 ( 전세계에서 유일한 값)
- XXX.XXX.XXX.XXX > IPv4 

4. DNS
	- Domain Name System
	- DNS Server
	- http://naver.com > (변환) > http://233.130.200.236 


5. Port Number
	- 네트워크를 사용하는 프로그램이 사용하는 통로
	- 0 ~ 65535 까지 존재
	- 독점
	- ~ 1000 : 예약 포트 넘버 
	- http: > :80 번호(기본)
	- https: > 443 번호 (기본)

6. IP:80
	- 상대방의 컴퓨터 + 프로그램 = 식별자
	- 종단점(EndPoint)


7. /member
	- 자원의 경로(폴더)

8. /list.html
	- 자원명(파일명)

9. ?name=hong&age=10&gender=f
	- Query String
	- name = hong
	- name : parameter
	- hong : Value




---
Java 개발 및 실행 환경
- 개발 : JDK
- 실행 : JRE


HTML/CSS/JavaScript 실행(개발) 환경
- 실행 : 브라우저 > 크롬 


HTML 파일 위치 src > main > webapp
- 아파치 톰캣 구조 
- 루트 폴더
- 웹사이트를 구성하는 자원들의 최상위 폴더


# HTML, Hyper Text Markup Language

- 하이퍼 텍스트 마크업 언어
- HyperText > 링크(Link)
- Markup Language > 태그(Tag)를 사용하여 문법을 표기하는 언어 
	- SGML, XML , HTML , XHTML 등등....

- 프로그래밍 언어 아님 > 표현 언어임 
- 브라우저 화면에 무언가를 출력하는 기능만 있는 언어


- http://w3.org 
- http://w3c.org
- html 1~ html 5 
- 수업은 html 4.01 + xhtml 1.0 + html 5

- HTML 4.01을 많이 씀 

XTML 1.0 = XML + HTML 




## HTML 개발환경
- 텍스트 편집기
- 1. 메모장
- 2. IDE > Eclipse , Visual Studio, Intellij 등등
- 3. SublimeText , Atom, Brackets, Visual Studio Code 등등...

- 실행 환경
1. 크롬



- HTML 1.0
- 1993년 
- 브라우저 
	- 모자익
	- 넷스케이프 네비게이터
	- MS > 인터넷 익스플로러


## DocType 선언문(문서유형) 
브라우저에게 현재 문서가 어떤 구성인지를 알려주는 역할



## html 태그

- 문서 전체를 감싸는 역할 
- 루트 태그 or  루트 엘리먼트
- <html.>의 자식 
	- head태그
	- body태그


## head 태그
- 문서의 정보
- 화면에 출력되지 않고, 브라우저에게 전달되는 용도의 데이터

## body 태그
- 문서의 내용
- 화면에 출력되는 내용(텍스트, 이미지, 동영상, 표 등등...)


