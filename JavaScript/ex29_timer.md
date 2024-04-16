```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

        fieldset {

            border: 1px solid gray;

            border-radius: 5px;

            width: 300px;

            margin-bottom: 10px;

        }

        fieldset input[type=text] {

            display: block;

            margin-top: 10px;

        }

    </style>

</head>

<body>

    <!-- ex29_timer.html -->

    <h1>타이머</h1>

  

    <form name="form1">

        <fieldset>

            <legend>setTimeout</legend>

            <input type="button" value="버튼" name="btn1">

            <input type="button" value="버튼" name="btn4">

            <input type="text" name="txt1">

        </fieldset>

        <fieldset>

            <legend>setInterval</legend>

            <input type="button" value="버튼" name="btn2">

            <input type="button" value="버튼" name="btn5">

            <input type="text" name="txt2">

        </fieldset>

        <fieldset>

            <legend>타이머 통제</legend>

            <input type="button" value="버튼" name="btn3">

            <input type="button" value="버튼" name="btn6">

            <input type="text" name="txt3">

        </fieldset>

    </form>

  
  

    <hr>

  

    <h2>고양이</h2>

  
  

    <img src="images/catty01.png" name="cat">

    <script>

  

        var btn1 = document.forms[0].btn1;

        var btn2 = document.forms[0].btn2;

        var btn3 = document.forms[0].btn3;

        var btn4 = document.forms[0].btn4;

        var btn5 = document.forms[0].btn5;

        var btn6 = document.forms[0].btn6;

        var btn7 = document.forms[0].btn7;

        var txt1 = document.forms[0].txt1;

        var txt2 = document.forms[0].txt2;

        var txt3 = document.forms[0].txt3;

  

        /*

            타이머, Timer

  

            1. id setTimeout(할일, 시간)

                - 1회성 타이머

  

            2. id setInterval(할일, 시간)

                - 반복 타이머

  

            3. void clearTimeout(id)

  

            4. void clearInterval(id)

  

        */

  

        var timer;

  

        btn1.onclick = m1;

        function m1() {

            timer = setTimeout(f1, 3000);

            console.log(timer);

        }

        function f1() {

            //alert('따르릉~');

            txt1.value = (new Date()).toLocaleTimeString();

        }

        btn4.onclick = m4;

        function m4() {

            clearTimeout(timer);

        }

  

        btn2.onclick = m2;

        function m2() {

            timer = setInterval(f2, 1000);

        }

        function f2() {

            txt2.value = (new Date()).toLocaleTimeString();

        }

        btn5.onclick = m5;

        function m5() {

            clearInterval(timer);

        }

  

        var n =1;

        timer =0;

        var timerList=[];

        btn3.onclick=m3;

        function m3(){

          //  if(timer == 0){

          //  setInterval(f3, 100);

       // }

       timer = setInterval(f3, 100);

       timerList.push(timer);

    }

        function f3(){

            txt3.value = n;

            n++;

        }

        btn6.onclick = m6;

  

        function m6(){

            //clearInterval(timer);

            //timer=0;

  
  

            //순차적 중지

            clearInterval(timerList.pop());

  

            //일괄적 중지

            for(var i=0; i<timerList.length; i++){

                clearInterval(timerList[i]);

            }

  

        }

  

        n=1;

        timer = 0;

        document.images['cat'].onclick = m7;

        function m7(){

            if(timer==0){

            timer = setInterval(f7,100);

        }else {

            clearInterval(timer);

            timer=0;

        }

    }

  

        function f7(){

            n++;

            if(n>9) n=1;

            document.images['cat'].src = 'images/catty0' + n + '.png';

        }

    </script>

</body>

</html>
```