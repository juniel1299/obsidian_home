background 관련 코드 대표적인거 

- background-color : 배경색
- background-image : 배경 이미지
- background-repeat : 반복 or 반복 안 함
- background-position : 위치 
- background-attachment : 배경 이미지에 대해 스크롤 여부 
- background-size : 배경 크기 


```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

<style>

    /*

    background

    1. background-color

    2. background-image

    3. background-repeat

    4. background-position

    5. background-attachment

    6. background-size

    */

    #box1{

        border: 1px solid black;

        width: 400px;

        height: 400px;

        background-image: url(images/cat05.jpg);

        background-repeat: no-repeat;

        background-position: center center;

        /*장축에 맞춘거 */

        /*background-size: 400px auto;*/

        background-size: contain;

        /*단축에 맞춘거*/

        /*background-size: auto 400px;*/

        /*background-size: cover;*/

    }

  

    #box2{

        border: 1px solid black;

        width: 600px;

        height: 400px;

        margin: 50px 0;

        /* 그레디언트 , gradient */

        /*빨간색에서 파란색 */

        /*background: linear-gradient(red,blue);*/

        /*파란색에서 빨간색 */

        /*background : linear-gradient(to top, red,blue)*/

        /*background : linear-gradient(180deg, red,blue)*/

        /*background: linear-gradient(to right, red,orange,yellow,green,blue,indigo,purple);*/

       /* background: radial-gradient(circle,red,blue);*/

        /*background: radial-gradient(red,blue,yellow,green);*/

        background-image: url(images/catty01.png), url(images/catty02.png),url(images/catty03.png);

        /*background-repeat: no-repeat, repeat-x, repeat-y;*/

        background-repeat: no-repeat;

        background-position: left top,center center,right bottom;

    }

</style>

</head>

<body>

    <div id="box1"></div>

    <div id="box2"></div>

</body>

</html>
```