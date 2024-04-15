# 자바 스크립트의 키 이벤트
- onkey로 시작함 

1. onkeydown
	- 키를 눌렀을 때 발생
	- 입력된 물리키에 반응
	- 입력된 키의 대/소문자를 구분 못함
	- **모든 키에 반응한다**

2. onkeyup
	- 키를 눌렀을 때 발생
	- 문자키에 반응
	- 입력된 문자를 구분 
	- **문자가 아닌 나머지 키에 반응을 못 함**

3. onkeypress
	- 키를 눌렀을 때 발생
	- 문자키에 반응
	- 입력된 문자를 구분 
	- **문자가 아닌 나머지 키에 반응 못 함**

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

        form > * {

            display: block;

            margin-bottom: 10px;

            outline: none;

            padding: 5px;

            resize: none;

            /* width: 300px; */

        }

        textarea {

            /* height: 200px; */

        }

    </style>

</head>

<body>

    <!-- ex14_key.html -->

    <h1>키 이벤트</h1>

  

    <form name="form1">

        <input type="text" name="txt1">

        <input type="text" name="txt2">

        <textarea name="txt3"></textarea>

    </form>

  

    <script>

  
  
  

        /*

            키 이벤트

            - onkeyXXX

  

            1. onkeydown

                - 키를 눌렀을 때 발생

                - 입력된 물리키에 반응

                - 입력된 키의 대/소문자를 구분 못함

                - 모든 키에 반응(*****)

  

            2. onkeyup

                - 키를 뗏을 때 발생

  

            3. onkeypress

                - 키를 눌렀을 때 발생

                - 문자키에 반응

                - 입력된 문자를 구분

                - 문자가 아닌 나머지 키에 반응 못함(***)

  

        */

  

        var txt1 = window.document.form1.txt1;

        var txt2 = window.document.form1.txt2;

        var txt3 = window.document.form1.txt3;

  

        /*

        방금 입력한 문자를 반영해서 할 때는 up

        상관 없으면 down ㅇㅋ?

        */

        //txt1.onkeydown = m1;

        txt1.onkeyup = m1;

        //txt1.onkeypress = m3;

  

        //window.document.body.onmousemove = m4;

  

        function m4() {

            txt2.size = event.clientX / 10;

        }

  

        function m1() {

            //console.log('keydown');

            console.log(event.keyCode);

  

            //방향키

            // if (event.keyCode == 37) {

            //     txt1.size--;

            // } else if (event.keyCode == 39) {

            //     txt1.size++;

            // }

  

            // if (event.keyCode == 37) {

            //     txt3.cols--;

            // } else if (event.keyCode == 39) {

            //     txt3.cols++;

            // } else if (event.keyCode == 38) {

            //     txt3.rows--;

            // } else if (event.keyCode == 40) {

            //     txt3.rows++;

            // }

  

            txt2.value = txt1.value;

  

        }

  

        function m2() {

            console.log('keyup');

        }

  

        function m3() {

            //console.log('keypress');

            console.log(event.keyCode);

        }

  

    </script>

  

</body>

</html>
```