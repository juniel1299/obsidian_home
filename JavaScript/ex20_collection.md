# 자바스크립트의 컬렉션
- 내장 배열 (컬렉션)
	1. 문서 내용(작성된 HTML)을 기반으로 자동 생성되는 배열을 제공 
	2. 태그 접근할 때 사용 + 조작 

1. window.document.images
2. window.document.links
3. window.document.anchors
4. window.document.forms
5. window.document.forms\[index\].elements
6. window.document.all (비표준 , MS)

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <h1>이미지</h1>

    <img src="./images/catty01.png" alt="">

    <img src="./images/catty02.png" alt="">

    <img src="./images/catty03.png" alt="">

    <img src="./images/catty04.png" alt="">

    <img src="./images/catty05.png" alt="">

  

    <h1>링크</h1>

    <a href="https://naver.com">네이버</a>

    <a href="https://google.com">구글</a>

    <a href="https://daum.net">다음</a>

  

    <h1>앵커</h1>

    <a name="a1">앵커1</a>

    <a name="a2">앵커2</a>

  

    <h1>폼</h1>

    <form>

        <input type="text" name="" id="">

        <input type="text" name="" id="">

        <input type="text" name="" id="">

    </form>

    <form>

        <input type="checkbox" name="" id="">

        <input type="radio" name="" id="">

    </form>

  

    <script>

        console.log(document.images.length); //이미지 개수 -> 5

        console.log(document.images[0].src); //이미지 링크

  

        for(var i=0; i<5; i++){

            console.log(document.images[i].src);

        }

        console.clear();

  
  

        console.log(document.links); // a 태그 개수 -> 3

        console.log(document.anchors); // 앵커 개수 -> 2

        console.log(document.forms); // 폼 개수 -> 2

  

        console.log(document.forms[0].elements); //폼 안에 들어있는 개수(컨트롤만) -> 3

        console.log(document.forms[1].elements); //폼 안에 들어있는 개수(컨트롤만) -> 2

  

        console.log(document.all); //문서에 존재하는 모든 것을 다 나타냄

    </script>

</body>

</html>
```
