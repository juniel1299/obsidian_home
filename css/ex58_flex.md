```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

        #box { border: 10px solid black; }

        #box .item:nth-child(5n+1) { background-color: tomato;}

        #box .item:nth-child(5n+2) { background-color: orange; }

        #box .item:nth-child(5n+3) { background-color: gold; }

        #box .item:nth-child(5n+4) { background-color: greenyellow; }

        #box .item:nth-child(5n+5) { background-color: dodgerblue; }

        #box .item { display: inline; }

  

        /* #box {

            font-size: 0;

        }

        #box .item {

            display: inline;

            font-size: 1rem;

        } */

  

        /* #box::after {

            content: '';

            display: block;

            clear: both;

        }

        #box .item {

            float: left;

        } */

  

        /*  

            display: flex;

            - flex box, flexiable box

            - 레이아웃 작성 > 요소 배치에 사용

        */

  

        #box {

            width: 600px;

            height: 300px;

            display: flex;

  

            /*  

                기본 상태

                - 메인축(아이템을 나열하는 방향): 가로(좌>우)

                - 수직축(메인축의 직각 방향): 세로(상>하)

                - 아이템 너비: 내용물만큼

                - 아이템 높이: 부모만큼

            */

  

            /*

                flex-direction

                - 아이템 배치 방향

                1. row: 행을 메인축으로

                2. column: 열을 메인축으로

            */

            /* flex-direction: row; */

            /* flex-direction: column; */

            /* flex-direction: row-reverse; */

            /* flex-direction: column-reverse; */

  

            /*  

                flex-wrap

                - 자동 줄바꿈

            */

            /* flex-wrap: wrap-reverse; */

  

            /*  

                flex 관련 속명

                1. justify-

                    : 메인축 방향과 관련된 속성

                2. align-

                    : 수직축 방향과 관련된 속성

            */

  

            /*  

                justify-content

                - 메인축 방향 + 아이템 정렬

            */

            /* flex-direction: row-reverse; */

            /* justify-content: flex-start; */

            /* justify-content: flex-end; */

            /* justify-content: center; */

            /* justify-content: space-between; */

            /* justify-content: space-around; */

            /* justify-content: space-evenly; */

  

            /*  

                align-items

                - 수직축 방향 + 아이템 정렬

            */

  

            /* align-items: stretch; */

            /* align-items: flex-start; */

            /* align-items: flex-end; */

            /* align-items: center; */

  

            justify-content: center;

            align-items: center;

  

        }

  

        /* #box {

            text-align: center;

            line-height: 300px;

        } */

  

        /* #box {

            text-align: center;

            padding-top: 140px;

            height: 160px;

        } */

        /* #box .item {

            margin-top: 100px;

        } */

  

        /* #box {

            display: table;

        }

  

        #box .item {

            display: table-cell;

            text-align: center;

            vertical-align: middle;

        } */

  

        #title1, #title2{

            font-variant: small-caps;

            color:#333;

            font-family: arial;

            letter-spacing:-1px;

            border-bottom: 1px dashed #999;

            width: 600px;

        }

  

        #title1 small {

            font-size: 1rem;

            float: right;

            margin-top: 14px;

        }

  

        #title2{

            display: flex;

            justify-content: space-between;

            align-items: flex-end;

        }

        #title2 small{

            font-size: 1rem;

            margin-bottom: 3px;

            /*background-color: gold;*/

  

        }

  
  
  

    </style>

</head>

<body>

    <!-- ex58_flex.html -->

    <h1>Flex</h1>

  

    <div id="box">

        <div class="item">1.딸기</div>

        <div class="item">2.바나나</div>

        <div class="item">3.귤</div>

        <div class="item">4.망고</div>

        <div class="item">5.바이올렛스위트루비</div>

        <div class="item">1.딸기</div>

        <div class="item">2.바나나</div>

        <div class="item">3.귤</div>

        <div class="item">4.망고</div>

        <div class="item">5.바이올렛스위트루비</div>

        <div class="item">1.딸기</div>

        <div class="item">2.바나나</div>

        <div class="item">3.귤</div>

        <div class="item">4.망고</div>

        <div class="item">5.바이올렛스위트루비</div>

        <div class="item">1.딸기</div>

        <div class="item">2.바나나</div>

        <div class="item">3.귤</div>

        <div class="item">4.망고</div>

        <div class="item">5.바이올렛스위트루비</div>

    </div>

  

    <hr>

  

    <h1 id="title1">Main Title<small>Sub Title</small></h1>

  

    <hr>

  

    <h1 id="title2">Main Title<small>Sub Title</small></h1>

  

    <hr>

  

</body>

</html>
```

