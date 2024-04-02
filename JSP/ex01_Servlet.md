# Servlet (서블릿)

1. 서블릿 클래스 선언 > 순수 자바 사용이 아닌 서블릿 API 사용한다 

2가지 방법

1. javax.servlet.Servlet 인터페이스를 구현한다. (복잡하고 고비용임)
2. javax.servlet.http.HttpServlet 클래스를 상속 받는다 ( 단순하고 저비용임)

## doGet / doPost 메소드 선언
메소드 작성 규칙
a. 매개 변수 작성
- 