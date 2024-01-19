
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

폴더 또한 파일이기 때문에 폴더에서도 적용 가능합니다.

기본적인 코드들은

```java
String path = "C:\\class\\data.txt"; //사용하고자 하는 경로가 필요합니다 (예시)


File file = new File(path); // 객체 선언 필요합니다.

//file.exists는 현재 파일이 존재하는가에 대해 물으며 존재할 시 true 없으면 false가 출력됩니다.

if (file.exists()) { 


//파일 조작

//지정한 경로 파일 이름을 알려줍니다. 
System.out.println(file.getName());  // ex) data.txt

//경로가 파일인지 폴더인지 알 수 있습니다 , true라면 파일 false면 폴더입니다.
System.out.println(file.isFile());  //ex) true

//경로가 폴더인지 파일인지 알 수 있습니다. true라면 폴더 false면 파일입니다.
System.out.println(file.isDirectory()); // ex) false

//지정한 경로 파일 크기를 알 수 있습니다. 
System.out.println(file.length()); //ex) 16 > 파일 크기

//경로를 볼 수 있습니다.
System.out.println(file.getAbsolutePath()); //ex) C:\class\data.txt

//작성된 시간을 알 수 있습니다. 
//단, 1970년 1월 1일 기준으로 현재까지 흐른 Millisecond 값이 출력됨 , Calender를 통해 변환 할 수 있다.
System.out.println(file.lastModified()); //ex) 1705547413588

//tick > 년월일시분초

Calendar c1 = Calendar.getInstance();

System.out.println(c1.getTimeInMillis());

c1.setTimeInMillis(file.lastModified());

System.out.printf("%tF %tT\n", c1, c1);

//지정한 해당경로 파일이 숨김파일인지 알 수 있다
System.out.println(file.isHidden()); //true면 숨김파일 false면 숨김x 파일

//읽기가 가능한 파일인지 확인
System.out.println(file.canRead()); //읽기전용 또는 제한이 없을 경우 true , 아니면 false

//쓰기가 가능한 파일인지 확인
System.out.println(file.canWrite()); //쓰기전용 또는 제한 없을 때 true 아니면 false

//지정한 경로파일의 부모폴더를 알려줍니다.
System.out.println(file.getParent()); //ex) C:\class

} else {

System.out.println("해당 경로에 파일이 없습니다.");

}
```


근데 사실 위에서 말한 코드들을 볼 때 어차피 탐색기 속성 누르면 다 볼 수 있는 정도인데 왜 쓰는걸까  ? 


### 파일 생성

```java
String path = "C:\\class\\code\\java\\file\\score.txt";

File file = new File(path);

try {



boolean result = file.createNewFile(); //file에 들어간 경로가 존재할 시 파일 생성을합니다 // ( 경로 하나라도 빠지면 안됩니다. )

System.out.println(result); //정상적으로 동작하는지 출력 true , 없으면 false

} catch (IOException e) {

e.printStackTrace();

}

}
```

### 파일명 수정
```java
String path = "C:\\class\\code\\java\\file\\score.txt"; //기존 파일명

File file = new File(path); //기존파일명 객체선언

String path2 = "C:\\class\\code\\java\\file\\jumsu.txt"; //바꾸고 싶은 파일명

File file2 = new File(path2); //수정하고 싶은 파일명 객체 선언

boolean result = file.renameTo(file2); //renameTo를 통해 수정

System.out.println(result); //결과가 올바르면 true 아니면 false
```
### 파일 이동

```java

//이동하고 싶은 파일
String path = "C:\\class\\code\\java\\file\\score.txt;

File file = new File(path); //이동하고 싶은 파일 경로 객체선언

String path2 = "C:\\class\\code\\java\\move\\score.txt"; //이동하고자 하는 경로+파일

File file2 = new File(path2); // 이동하고자 하는 경로+파일 객체 선언

boolean result = file.renameTo(file2); //renameTo를 통해 이동

System.out.println(result); //결과가 올바르면 true 아니면 false
```
### 삭제
```java
String path = "C:\\class\\code\\java\\file\\score.txt"; //삭제 하고 싶은 파일 

File file = new File(path); //객체선언

if (file.exists()) { //파일이 있으면 동작하도록 제어문 작성


boolean result = file.delete(); //여기서 delete는 Shift + Delete 입니다; 

System.out.println(result); //결과 확인
```

### 폴더 생성
```java
String path = "C:\\class\\code\\java\\file\\bbb\\ccc\\ddd";

File dir = new File(path); ///폴더 경로 객체 생성

if (!dir.exists()) { //폴더가 없을시 (if문)

//폴더 없음

boolean result = dir.mkdirs(); //make directory

System.out.println(result); //결과

} else {

System.out.println("같은 이름의 폴더가 존재함.");

}
```

mkdir와 mkdirs 통해 폴더를 생성할 수 있음

mkdir은 경로를 정확하게 지정해야하며 중간에 하나라도 없으면 생성을 하지 않음 

mkdirs는 위의 예시 기준으로 bbb 이후 경로가 없어도 ccc 폴더를 만들고 그 안에 ddd 폴더를 생성하여 경로대로 동작한다.

이것을 응용하여 폴더를 여러개 만들수도 있다

```java
String[] member = { "홍길동", "아무개", "강아지", "고양이", "독수리" };

for (int i=0; i<member.length; i++) {

String path = String.format("C:\\class\\code\\java\\file\\회원\\[개인폴더]%s님", member[i]);

File dir = new File(path);

System.out.println(dir.mkdirs());

}

```
배열에 문자열 여러개를 담은 뒤 for문을 통해 반복하면 여러개의 폴더를 생성 할 수 있다.


또한 Calendar 를 응용할 수도 있다

```java
String[] member = { "홍길동", "아무개", "강아지", "고양이", "독수리" };

for (int i=0; i<member.length; i++) {

String path = String.format("C:\\class\\code\\java\\file\\회원\\[개인폴더]%s님", member[i]);

File dir = new File(path);

System.out.println(dir.mkdirs());

}
```
### 폴더 수정 , 이동
```java
//폴더명 수정 or 폴더 이동

//- renameTo

File dir = new File("C:\\class\\code\\java\\file\\일정");

File dir2 = new File("C:\\class\\code\\java\\file\\schedule");

System.out.println(dir.renameTo(dir2));
```
dir은 수정하고자 하는 파일
dir2는 어떻게 수정되면 되는지에 대해 작성하면 올바르게 변환이 된다.

### 폴더 삭제
```java
File dir = new File("C:\\class\\code\\java\\file\\schedule");

if (dir.exists()) {

//빈폴더만 삭제 가능(***)

System.out.println(dir.delete());

}
```

파일 삭제와 마찬가지로 delete