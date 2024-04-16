# 자바스크립트의 메세지 

- 메세지 박스(대화 상자) (Dialog box)
1. void alert(message)
2. boolean confirm(me)


```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <h1>메세지 박스</h1>

  

    <form name="form1">

        <input type="button" value="버튼1" name="btn1">

        <input type="button" value="버튼2" name="btn2">

        <input type="button" value="버튼3" name="btn3">

    </form>

  

    <script>

        document.form1.btn1.onclick = m1;

        document.form1.btn2.onclick = m2;

        document.form1.btn3.onclick = m3;

  

        /*

  

        메세지 박스, 대화 상자(Dialog box)

        1. void alert(message)

        2. boolean confirm(message)

        ----------------------------------

        3. string prompt(message, value)

  

        */

        function m1(){

            alert(100);

            alert('문자열');

        }

  

        function m2(){

           var result = confirm('메세지'); //확인 취소 버튼

           if(result){

            document.body.bgColor = 'blue';

           }else {

            document.body.bgColor = 'white';

           }

        }

  

        function m3(){

          //  prompt('메세지', '기본값'); //form 태그

            //var name = prompt('이름을 입력하세요','');

            //alert(name);

            var pw = prompt('암호를 입력하시오.','');

  

            if(pw =='1234'){

                location.href = 'https://google.com';

            }

        }

  

    </script>

</body>

</html>
```