```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

        #box{

            border: 10px solid black;

        }

        #box .item:nth-child(1){background-color: tomato;}

        #box .item:nth-child(2){background-color: orange;}

        #box .item:nth-child(3){background-color: gold;}

        #box .item:nth-child(4){background-color: yellowgreen;}

        #box .item:nth-child(5){background-color: cornflowerblue;}

        #box .item:nth-child(6){background-color: violet;}

  
  

        #box{

            display: grid;

           /* grid-template-rows: 100px 100px;  2행*/

          /* grid-template-columns: 100px 100px 100px;  3열 */

/*

          grid-template-rows: 200px 200px;

          grid-template-columns: 100px 100px;*/

       /*   grid-template-columns: 100px 100px 100px 100px 100px 100px ;*/

   /*         grid-template-columns: repeat(3,100px);

            grid-template-rows: repeat(2,100px);

  

            grid-template-columns: 1fr 1fr 1fr;*/

            /*비율 맞춰줌 */

       /*     grid-template-columns: 120px repeat(3,1fr) 2fr 10%;*/

       grid-template-rows: 100px 100px;

       grid-template-columns: repeat(4,1fr);

    }

  

    #box .item:nth-child(1){

      /*

        grid-column-start: 1;

        grid-column-end: 3;

    */

   /* grid-column: 1/3;

    grid-row: 1/3;*/

  

   /* grid-row-start: 1;

    grid-row-end: 3;*/

  

    grid-column-end: span 2;

    grid-row-end: span 2;

    }

  

    </style>

</head>

<body>

    <h1>Grid</h1>

  
  

    <div id="box">

        <div class="item">A</div>

        <div class="item">B</div>

        <div class="item">C</div>

        <div class="item">D</div>

        <div class="item">E</div>

        <div class="item">F</div>

    </div>

</body>

</html>
```
