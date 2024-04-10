border 대표적인 코드 

border : 1px solid black; (테두리 굵기, 타입, 색깔)
border-radius : 모서리 둥글기 (px단위 또는 % )



```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

  

    <script src="https://kit.fontawesome.com/7121714adf.js" crossorigin="anonymous"></script>

  

    <style>

        #box1 {

            border: 1px solid black;

            width: 300px;

            height: 200px;

            margin: 50px;

  

            /*

                모서리 둥글기(px, %)

                - 최대값 = 단축의 1/2

            */

            /* border-radius: 50%; */

  

            border-top-left-radius: 30px;

            border-bottom-right-radius: 30px;

            border-top-right-radius: 100px;

            border-bottom-left-radius: 100px;

  

        }

  

        /* input[type=text] {

            border: 1px solid black;

            border-radius: 50%;

            outline: none;

            padding-left: 10px;

            padding-right: 10px;

        } */

  

        body {

            margin-bottom: 300px;

        }

  

        img {

            border-radius: 50%;

        }

        img:hover {

            box-shadow: 0px 7px 5px gray;

        }

  
  

        .input {

            width: 190px;

        }

  

        .input > input[type=text] {

            float: left;

            border: 1px solid #444;

            border-right: 0;

            width: 150px;

            outline: none;

            padding: 3px;

            border-top-left-radius: 3px;

            border-bottom-left-radius: 3px;

        }

        .input > button {

            float: left;

            border: 1px solid #444;

            width: 30px;

            padding: 3px;

            border-top-right-radius: 3px;

            border-bottom-right-radius: 3px;

        }

  

        .input::after {

            content: '';

            display: block;

            clear: both;

        }

  

        #tbl1 {

            /* border: 1px solid black; */

            /* border-collapse: collapse; */

            border-radius: 10px;

            border-spacing: 1px

        }

  

        #tbl1 td {

            border: 1px solid black;

            width: 50px;

            height: 50px;

            /* border-radius: 10px; */

        }

  

        #tbl1 tr:nth-child(1) td:nth-child(1) {

            border-top-left-radius: 10px;

        }

        #tbl1 tr:nth-child(1) td:nth-last-child(1) {

            border-top-right-radius: 10px;

        }

        #tbl1 tr:nth-last-child(1) td:nth-child(1) {

            border-bottom-left-radius: 10px;

        }

        #tbl1 tr:nth-last-child(1) td:nth-last-child(1) {

            border-bottom-right-radius: 10px;

        }

  

    </style>

</head>

<body>

    <!-- ex46_border.html -->

    <div id="box1"></div>

  

    <input type="text">

  

    <hr>

  

    <img src="images/dog01.jpg">

    <img src="images/dog02.jpg">

    <img src="images/dog03.jpg">

    <img src="images/dog04.jpg">

    <img src="images/dog05.jpg">

  

    <hr>

  

    <div class="input">

        <input type="text">

        <button type="button">

            <i class="fa-solid fa-magnifying-glass"></i>

        </button>

    </div>

  

    <div class="input">

        <input type="text">

        <button type="button">

            <i class="fa-solid fa-right-to-bracket"></i>

        </button>

    </div>

  

    <hr>

  

    <table id="tbl1">

        <tr>

            <td></td>

            <td></td>

            <td></td>

        </tr>

        <tr>

            <td></td>

            <td></td>

            <td></td>

        </tr>

        <tr>

            <td></td>

            <td></td>

            <td></td>

        </tr>

    </table>

  

</body>

</html>
```