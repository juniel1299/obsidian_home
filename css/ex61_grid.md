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

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

<link rel="stylesheet" href="css/ex62.css">

</head>

<body>

    <main>

        <div id="menu">

            <h1>Study</h1>

            <ul>

                <li>Java</li>

                <li>Oracle</li>

                <li>HTML</li>

                <li>CSS</li>

                <li>JavaScript</li>

            </ul>

            <hr>

            <ul>

                <li>Class</li>

                <li>Method</li>

                <li>Interface</li>

                <li>Property</li>

                <li>Attiribute</li>

            </ul>

            <hr>

            <div>

                &copy;Copyright test.com <br>

                All rights reserved.

            </div>

        </div>

        <div id="search">

            <input type="text">

            <button>Search</button>

        </div>

        <div id="banner">

            <img src="images/gimbal.jpg" alt="">

        </div>

        <div id="content">

            <!-- <div>

                <img src="images/rect_icon01.png" alt="">

                <div>text</div>

            </div> -->

        <!-- (div>(img[src=images/rect_icon$$.png])+(div>lorem))*6 -->

        <div>

            <img src="images/rect_icon01.png" alt="">

            <div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci earum quidem mollitia quisquam officia assumenda tempora maxime autem nihil eos ut repellendus eaque, beatae est alias repellat consequuntur nulla illo.</div>

        </div>

        <div>

            <img src="images/rect_icon02.png" alt="">

            <div>Excepturi cupiditate voluptates est aspernatur at quae. Sequi, minima. Unde et, dolores tempore accusantium a fugiat nulla quisquam veritatis ea quo temporibus sit quas officiis repellendus dignissimos repudiandae fuga incidunt!</div>

        </div>

        <div>

            <img src="images/rect_icon03.png" alt="">

            <div>Consequatur corrupti doloremque veniam perferendis rerum repellat nihil, reiciendis maxime a sapiente cum doloribus fugiat deserunt recusandae, sequi delectus vel iure. Delectus quasi amet autem ab consequatur, nesciunt molestias. Placeat.</div>

        </div>

        <div>

            <img src="images/rect_icon04.png" alt="">

            <div>Fugiat a cumque sint repellat quos nostrum assumenda nemo. Autem, omnis! In praesentium tenetur mollitia eius ratione, accusantium delectus. Molestiae minus delectus non nemo nam qui officia culpa reiciendis magni!</div>

        </div>

        <div>

            <img src="images/rect_icon05.png" alt="">

            <div>Blanditiis doloribus adipisci quidem debitis ab, aliquam dolorum magnam iste sint beatae quasi provident possimus architecto minima ea reiciendis laudantium recusandae ut ratione vero repellat soluta temporibus nemo? Illo, dicta.</div>

        </div>

        <div>

            <img src="images/rect_icon06.png" alt="">

            <div>Iusto nulla eveniet beatae? Aliquid, quasi accusamus! Eum molestias voluptates quidem sunt minima dolorum numquam iure ea delectus labore dolore ut dolorem aperiam sit dicta, reprehenderit porro, fuga repellendus accusantium.</div>

        </div>

        </div>

    </main>

</body>

</html>
```

