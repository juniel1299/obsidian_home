- **width 와 height는 요소 크기가 아닌 컨텐츠 영역의 크기이다.**
- 콘텐츠 크기 > 테두리와 패딩 포함 x 

- 실제 눈에 보이는 사각형의 넓이 = width + padding + border , height + padding + border 

box-sizing (영역의 크기를 지정하는 정책)
1. content-box : width/height \=\= content 영역의 크기 
2. border-box : width/height \=\= content + padding + border ,진짜로 눈에 보이는 크기는 width 와 height 이다. 



```css
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

<style>

    #bar{

        background-color: cornflowerblue;

        height: 10px;

        width: 200px;

    }

  

    #box{

        background-color: gold;
        width: 200px;

        height: 100px;

        padding: 20px;

        border: 10px solid black;

        margin: 0px;

        box-sizing: border-box;

    }

  

</style>

</head>

<body>

    <div id="bar"></div>

    <div id="box">상자</div>

  

</body>

</html>
```