# transform 변형, 
- 요소의 위치 크기 회전 , 비틀기(왜곡)
- transform : 값;  
- 값에 해당하는 코드 
	- 1. translate() : 위치 변형 
	- 2. scale() 크기(배율) 변형
	- 3. rotate() 회전 변형
	- 4. skew() 왜곡 변형
	- 5. matrix() 행렬
- position : 레이아웃
- transform : 인터페이스(사용법)

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <link rel="stylesheet" href="css/box.css">

<style>

  

    /*

    변형, transform

    - 요소의 위치, 크기, 회전, 비틀기(왜곡)

    - transform: 값;

  

    값(함수)

    1.translate() > 위치 변형

    2.scale() > 크기(배율) 변형

    3.rotate() > 회전 변형

    4.skew() > 왜곡 변형

    5.matrix() > x(행렬)

  
  
  
  
  

    1. position : 레이아웃

    2. transform: 인터페이스(사용법)

    */

  
  

    #box2{

        /*transform: translate(100px, 100px);*/

       /* transform: scale(-0.5,1);

        margin-left: 300px;

        */

        /*transform: rotate(110deg);*/

        transform: skew(89deg, 89deg);

    }

  

    /*#cat img:hover{

        transform: translate(0px, -15px);

    }*/

  

    /* #cat:hover img{

        transform: translate(0px,-15px);

    }*/

  

    /*

    #cat img:hover ~ img{

        transform: translate(0px,-15px);

    }

    */

   /* #cat:hover img:nth-child(even){

        transform: translate(0px,-15px);

    }*/

  

    #cat img:hover{

     /*   transform: translate(0px,-55px) scale(1.4,-1.4);*/

  

     transform: rotate(20deg);

    }

  
  

    #txt1{

        margin: 50px;

        font-size: 2rem;

        padding: 10px;

     /*   transform: scale(-1,-1); */

       /* transform: rotate(45deg);*/

    }

  

    body{

    }

</style>

  

</head>

<body>

    <div id="box1" class="box bgcolor-red border10"></div>

    <div id="box2" class="box bgcolor-yellow border10">dd</div>

    <div id="box3" class="box bgcolor-blue border10"></div>

  

    <input type="text" class="bgcolor-blue">

  

    <h1>고양이</h1>

    <div id="cat">

        <img src="images/catty01.png" alt="">

        <img src="images/catty02.png" alt="">

        <img src="images/catty03.png" alt="">

        <img src="images/catty04.png" alt="">

        <img src="images/catty05.png" alt="">

    </div>

  

    <div>

        <input type="text" id="txt1">

    </div>

</body>

</html>
```


## 인접한 인라인 태그 사이에 공백 없애는 법 
1. 직접 지우기 (안 씀)
2. font-size : 0 ; (추가 코드 발생(내부 컨텐츠 글꼴 크기 재정의))
3. float (추가 코드 발생(clear))
4. flex (추가 코드 발생 없음)


