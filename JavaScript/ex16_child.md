# 자바스크립트의 상속관계

- 부모창의 텍스트박스 접근?
-  부모창의 window.document
- 부모창의 window 객체
- 예약어 > opener
```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <!-- ex16_child.html -->

    <h1>자식 페이지</h1>

  

    <form name="form1">

        <input type="text" name="txt1">

        <hr>

        <input type="button" value="부모창에 있는 텍스트박스 접근하기" name="btn1">

    </form>

  

    <script>

  

        var btn1 = window.document.form1.btn1;

  

        btn1.onclick = m1;

  

        function m1() {

            //부모창의 텍스트박스 접근?

            //- 부모창의 window.document

  

            //부모창의 window 객체

            //- 예약어 > opener

  

            opener.document.form1.txt1.value = '자식창에서 왔습니다.';

  

        }

  

    </script>

  

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

</head>

<body>

    <!-- ex16_idcheck.html -->

    <h1>아이디 중복검사</h1>

  

    <form name="form1">

        아이디: <input type="text" name="id">

        <input type="button" value="중복검사">

        <hr>

        <div>사용이 가능한 아이디입니다.</div>

        <!-- <div>이미 사용 중인 아이디입니다.</div> -->

        <hr>

        <input type="button" value="아이디 사용하기" name="btn1">

        <input type="button" value="창닫기" name="btn2">

    </form>

  

    <script>

  

        var btn1 = window.document.form1.btn1;

        var btn2 = window.document.form1.btn2;

        var id = window.document.form1.id;

        btn1.onclick = m1;

        btn2.onclick = m2;

  

        function m1(){

            //1. 자식창 아이디 > 부모창 아이디

            opener.document.form1.id.value = id.value;

            //2. 창닫기

            window.close();

        }

  

        function m2(){

            window.close();

        }

  

    </script>

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

</head>

<body>

    <!-- ex16_window.html -->

    <h1>window 객체</h1>

  

    <form name="form1">

        <fieldset>

            <legend>창 제어하기</legend>

            <input type="button" value="자식창 띄우기" name="btn1">

            <input type="button" value="자식창 닫기" name="btn2">

        </fieldset>

        <fieldset>

            <legend>자식창의 자원에 접근하기</legend>

            <input type="button" value="자식창에 있는 텍스트박스에 접근하기" name="btn3">

            <hr>

            <input type="text" name="txt1">

        </fieldset>

  

        <h2>아이디 중복검사 / 우편번호 검색하기 / 결제하기</h2>

        <fieldset>

            아이디: <input type="text" name="id" size="10">

            <input type="button" value="중복검사" name="btnCheck">

        </fieldset>

    </form>

  

    <script>

  

        var btn1 = window.document.form1.btn1;

        var btn2 = window.document.form1.btn2;

        var btn3 = window.document.form1.btn3;

        var btnCheck = window.document.form1.btnCheck;

  

        btn1.onclick = m1;

        btn2.onclick = m2;

        btn3.onclick = m3;

        btnCheck.onclick = m4;

  

        var child;

  

        function m1() {

  

            //object window.open(URL, name, options)

            //1. URL: 새창의 URL

            //2. name: 새창의 이름

            //3. options: 옵션들..

  

            //window.open('./ex16_child.html', 'child', '');

            //window.open('https://naver.com', 'naver', '');

  

            child = window.open('./ex16_child.html', 'child', 'width=500 height=300 left=0 top=0');

            console.log(child);

  

        }

  

        function m2() {

            //자식창 닫기

            //window.close();

  

            //자식창의 window 객체 접근?

            child.close(); //자식창 입장 > window.close();

  

        }

  

        function m3() {

  

            //현재 페이지의 텍스트 박스 접근?

            //window.document.form1.txt1.value = 'aaa';

  

            //자식창의 텍스트 박스 접근?

            child.document.form1.txt1.value = '부모로부터 왔습니다.';

  

        }

  

        function m4() {

            window.open('ex16_idcheck.html', 'idcheck', 'width=500 height=400');

        }

  

    </script>

  

</body>

</html>
```