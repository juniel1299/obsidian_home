```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

        .item{

            border: 1px solid #ccc;

            background-color: #eee;

            padding: 10px;

            width:400px;

            text-align: center;

            margin: 15px;

        }

        .item>input[type=button]{

            border: 1px solid #ccc;

            background-color: #fff;

            width: 100px;

            height: 60px;

            margin: 10px;

            outline: none;

        }

        .item >input[type=button]:hover{

            box-shadow: 0px 0px 3px gray;

        }

  

    </style>

</head>

<body>

    <h1>다량의 요소들의 이벤트 처리(일괄 처리)</h1>

  

    <form name="form1">

<!--        

        <div class="item">

            <input type="button" value="빨강" name="btnRed">

            <input type="button" value="노랑" name="btnYellow">

            <input type="button" value="파랑" name="btnBlue">

        </div> -->

        <!-- 정적 이벤트 -->

        <div class="item">

            <input type="button" value="빨강" name="btnRed" onclick="m1();">

            <input type="button" value="노랑" name="btnYellow" onclick="m2();">

            <input type="button" value="파랑" name="btnBlue" onclick="m3();">

        </div>

        <!-- 동적 이벤트 -->

        <div class="item">

            <input type="button" value="빨강" name="btnRed2" onclick="m1();">

            <input type="button" value="노랑" name="btnYellow2" onclick="m2();">

            <input type="button" value="파랑" name="btnBlue2" onclick="m3();">

        </div>

  

        <div class="item">

            <input type="button" value="빨강" name="btnRed3" onclick="m7('tomato');">

            <input type="button" value="노랑" name="btnYellow3" onclick="m7('gold');">

            <input type="button" value="파랑" name="btnBlue3" onclick="m7('cornflowerblue');">

        </div>

  
  

        <div class="item">

            <input type="button" value="빨강" name="btnRed4" onclick="m8(this);">

            <input type="button" value="노랑" name="btnYellow4" onclick="m8(this);">

            <input type="button" value="파랑" name="btnBlue4" onclick="m8(this);">

        </div>

  
  

        <div class="item">

            <input type="button" value="빨강" name="btnRed5" onclick="m9(this);" data-color="tomato">

            <input type="button" value="노랑" name="btnYellow5" onclick="m9(this);" data-color="gold">

            <input type="button" value="파랑" name="btnBlue5" onclick="m9(this);" data-color="cornflowerblue">

        </div>

  

        <div class="item">

            <input type="button" value="빨강" name="btnRed5" onclick="m10();" data-color="tomato">

            <input type="button" value="노랑" name="btnYellow5" onclick="m10();" data-color="gold">

            <input type="button" value="파랑" name="btnBlue5" onclick="m10();" data-color="cornflowerblue">

        </div>

  
  

        <div class="item">

            <input type="button" value="빨강" name="btnRed7" data-color="tomato">

            <input type="button" value="노랑" name="btnYellow7" data-color="gold">

            <input type="button" value="파랑" name="btnBlue7" data-color="cornflowerblue">

        </div>

  

        <div class="item">

            <input type="button" value="빨강" name="btn8" data-color="tomato">

            <input type="button" value="노랑" name="btn8" data-color="gold">

            <input type="button" value="파랑" name="btn8" data-color="cornflowerblue">

        </div>

  

        <div>

            <img src="images/cat01.jpg" name="cat" alt="">

            <img src="images/cat02.jpg" name="cat" alt="">

            <img src="images/cat03.jpg" name="cat" alt="">

        </div>

  

    </form>

  

    <script>

  

        function m1(){

            document.body.bgColor = 'tomato';

        }

  

        function m2(){

            document.body.bgColor = 'gold';

        }

  

        function m3(){

            document.body.bgColor = 'cornflowerblue';

        }

  

        document.form1.btnRed2.onclick = m4;

        document.form1.btnYellow2.onclick = m5;

        document.form1.btnBlue2.onclick = m6;

        function m4(){

            document.body.bgColor = 'tomato';

        }

  

        function m5(){

            document.body.bgColor = 'gold';

        }

  

        function m6(){

            document.body.bgColor = 'cornflowerblue';

        }

        function m7(color){

            document.body.bgColor = color;

        }

  

        function m8(obj){

            //alert(obj); 단순하게 덤프

            //console.log(obj);//자세하게 덤프

  

            //alert(obj.name); //name 값

            //alert(obj.value); // value 값

            if(obj.name == 'btnRed4'){

                document.body.bgColor = 'tomato';

            }else if(obj.name == 'btnYellow4'){

                document.body.bgColor = 'gold';

            }else if(obj.name == 'btnBlue4'){

                document.body.bgColor = 'cornflowerblue';

        }

            alert(obj.name.substr(3).substr(0,obj.name.length-4));

    }

  

    function m9(obj){

        //data-color=""

        console.log(obj.dataset['color']);

        document.body.bgColor = obj.dataset['color'];

    }

  

    function m10(){

        //어떤 버튼 클릭했는지 알 수 없음.

  

        //이벤트 발생 시킨 객체

        console.log(event.srcElement); //비표준(MS)

        console.log(event.target); //표준

        document.body.bgColor = event.target.dataset['color'];

    }

  

    document.form1.btnRed7.onclick = m11;

    document.form1.btnYellow7.onclick = m11;

    document.form1.btnBlue7.onclick = m11;

  

    function m11(){

        document.body.bgColor = event.target.dataset['color'];

  

    }

  

    //console.log(document.form1.btn8);

  

    //*****태그의 name 이 동일하면 > 배열화

  

    for(var i=0; i<document.form1.btn8.length; i++){

        document.form1.btn8[i].onclick =m12;

    }

  

    function m12(){

        document.body.bgColor = event.target.dataset['color'];

    }

  

    //console.log(document.images['cat']);

    //console.log(document.all.cat.length);

  

    for(var i=0; i<document.all.cat.length; i++){

        document.all.cat[i].onmouseover = m13;

        document.all.cat[i].onmouseout = m13;

  

    }

  

    function m13(){

        //다른 객체 > 하나의 이벤트 함수로 처리 (매개변수 or this or event.srcElement, event.target)

  

        //다른 이벤트 > 하나의 이벤트 함수로 처리

  
  

        //console.log(event.type);

        console.log(event.target.src.substr(event.target.src.length -5, 1));

        var n = event.target.src.substr(event.target.src.length -5, 1);

        if(event.type =='mouseover'){

            event.target.src = 'images/dog0' + n + '.jpg';

        }else if(event.type =='mouseout'){

            event.target.src = 'images/cat0' + n + '.jpg';

        }

    }

</script>

  

</body>

</html>
```