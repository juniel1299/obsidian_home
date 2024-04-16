# 자바스크립트의 상속관계

            //부모창의 텍스트박스 접근?

 - 부모창의 window.document

  
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