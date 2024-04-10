
테두리 코드는 대표적으로 
- border 
- outline 
두개가 존재  

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

        .box { width: 200px; height: 200px; box-sizing: content-box; margin-left: 50px;}

        #box1 { background-color: tomato; }

        #box2 { background-color: gold; }

        #box3 { background-color: cornflowerblue; }

  

        /*

            테두리

            1. border

            2. outline

        */

        body:hover #box2 {

            /* border: 20px solid black; */

            outline: 20px solid black;

        }

  

        .txt {

            display: block;

            margin-bottom:3px;

            font-size: 2rem;

            outline:none;

        }

  

        .txt:focus{

            /*border: 3px solid blue;*/

        outline: 3px solid blue;

        }

  

    </style>

</head>

<body>

    <!-- ex47_outline.html -->

    <div id="box1" class="box"></div>

    <div id="box2" class="box"></div>

    <div id="box3" class="box"></div>

  

    <hr>

  

    <input type="text" class="txt">

    <input type="text" class="txt">

    <input type="text" class="txt">

    <input type="text" class="txt">

    <input type="text" class="txt">

    <input type="text" class="txt">

    <input type="text" class="txt">

    <input type="text" class="txt">

    <input type="text" class="txt">

    <input type="text" class="txt">

  

</body>

</html>

```