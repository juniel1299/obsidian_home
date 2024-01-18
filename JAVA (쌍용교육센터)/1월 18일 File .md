
# File

1. 파일 디렉토리 조작
	- 윈도우 탐색기로 하는 행동을 자바를 통해 함

1. 파일 입출력
	- 파일을 읽고 쓰거나 
	- 텍스트를 입출력하거나

자바 프로그램에서 외부 파일을 접근 
1. 외부 파일을 참조하는 객체를 생성한다 
2. 참조 객체 조작하여 실제로 파일에 적용을 한다

## File 문법

사용을 하기 위해선 import java.io.File; 필요하며 

기본적인 코드들은

```java
String path = "C:\\class\\data.txt"; //사용하고자 하는 경로가 필요합니다 (예시)


File file = new File(path); // 객체 선언 필요합니다.

//file.exists는 현재 파일이 존재하는가에 대해 물으며 존재할 시 true 없으면 false가 출력됩니다.

if (file.exists()) { 


//파일 조작

//지정한 경로 파일 이름을 알려줍니다. 
System.out.println(file.getName());  // ex) data.txt

//경로가 파일인지 폴더인지 알 수 있습니다 , true라면 파일 false면 폴더
System.out.println(file.isFile());  //ex) true

System.out.println(file.isDirectory()); //false

System.out.println(file.length()); //16 > 파일 크기(바이트)

System.out.println(file.getAbsolutePath()); //C:\class\code\java\file\data.txt

System.out.println(file.lastModified()); //1705547413588

//tick > 년월일시분초

Calendar c1 = Calendar.getInstance();

System.out.println(c1.getTimeInMillis());

c1.setTimeInMillis(file.lastModified());

System.out.printf("%tF %tT\n", c1, c1);

System.out.println(file.isHidden()); //false

System.out.println(file.canRead()); //true

System.out.println(file.canWrite()); //true

System.out.println(file.getParent()); //C:\class\code\java\file

} else {

System.out.println("해당 경로에 파일이 없습니다.");

}
```
