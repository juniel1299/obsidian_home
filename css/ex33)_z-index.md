
z index는 기존에 있는 물체 위에 입체적으로 올릴 수 있도록 도와주는 코드이다 . 

```css

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

        .box{

            border: 1px solid black;

            width:150px; height:150px;

            /*display: inline-block;*/

        }

       #box1{

            background-color: red;

            position: absolute;

            left: 100px;

            top: 100px;

            z-index: 1;

        }

        #box2{

            background-color: orange;

            position: absolute;

            left: 120px;

            top: 120px;

            z-index: 3;

        }

        #box3{

            background-color: yellow;

            position: absolute;

            left:150px;

            top:150px;

            z-index: 2;

        }

    </style>

</head>

<body>

    <h1>Position</h1>

  

    <div id="box1" class="box">상자1</div>

    <div id="box2" class="box">상자2</div>

    <div id="box3" class="box">상자3</div>

</body>

</html>
```