# Servlet (서블릿)

1. 서블릿 클래스 선언 > 순수 자바 사용이 아닌 서블릿 API 사용한다 

2가지 방법

1. javax.servlet.Servlet 인터페이스를 구현한다. (복잡하고 고비용임)
2. javax.servlet.http.HttpServlet 클래스를 상속 받는다 ( 단순하고 저비용임)

## doGet / doPost 메소드 선언
메소드 작성 규칙
a.매개 변수 작성
- java.servlet.http.HttpServletRequest
- java.servlet.http.HttpServletResponse

b. 예외 미루기
- java.io.IOException
- java.servlet.ServletException

## 동적 HTML 페이지 작성
- FileWriter / BufferedWriter
- 브라우저가 보게 될 페이지 \=\= HTML 페이지 > 내용이 HTML

```java
import java.io.IOException;

import java.io.PrintWriter;
import javax.servlet.ServletException;

import javax.servlet.http.HttpServlet;

import javax.servlet.http.HttpServletRequest;

import javax.servlet.http.HttpServletResponse;

public class Ex01 extends HttpServlet {

public void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException, ServletException {

PrintWriter writer = resp.getWriter();

writer.println("<html>");

writer.println("<body>");

writer.println("<h1>Hello Servlet</h1>");''

writer.println("<p>Hello~ Hong!!! aaaaaa</p>");

writer.println("</body>");

writer.println("</html>");

writer.close();
	}
}
```