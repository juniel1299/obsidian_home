# body 태그
- 모든 출력 내용을 관리하는 컨테이너 

##  body 속성
1. bgcolor
	- 문서 배경색


2. background
	- 문서 배경 이미지


## HTML의 색상 표현법 \*\*\*\*\*
1. 색상명
	- Named Color
	- Well-known Color
	- 미리 약속된 몇가지 색상명 (140여가지)
	- Web Color name


2. RGB컬러
	- Red + Green + Blue = 조합
	- 각 색상의 단계 : 256단계 지원 (0~255 > 0x00 부터 0xFF까지)
	- 256^3 = 16777216
	- 16진수 표기 
	- 00 00 00 (검정색) , FF FF FF (흰색)
	- \#FF0000 > 빨간색
픽픽


## HTML 경로 표현법
- 웹 페이지에서 자원의 경로를 표기하는 방법 > URL 표기법 

ClientTest > src > main > webapp > html > images 폴더
- jpg(jpeg), gif, png


```html
<body background="images/he.jpg">


```


### 경로 구분자 

1. \\ 
	- 자바
	- D:\class\code\java


2. /
	- 웹
	- images/dog


### 경로 표현 방식
1. 상대 경로
	-  . 으로 시작
	-  . : 웹페이지가 있는 현재 폴더
	- .. : 부모 폴더
	- background="./images/dog.jpg"

2. 절대 경로
	- 기준점이 불변
	- 경로를 /로 시작함
	- / : 웹 루트폴더(webapp)
	- / client ==  webapp
```html

<body background="/client/html/images/dog.jpg">

```
3. 로컬 경로
	-  자바 경로
```html
<body background="C:\class\code\FrontClient\Client\ClientTest\src\main\webapp\html\images\dog.jpg">


```
- 못 씀
1. 외부 경로
	-  다른 서버에 있는 자원의 URL
```html
<body background="이미지URL">

```





