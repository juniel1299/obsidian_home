# 자바스크립트의 history 객체
- 브라우저 히스토리 영역 > 방문했던  URL을 기록하는 공간 
- 브라우저 히스토리 접근 + 조작 객체 


```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <h1>history 객체</h1>

  

    <form name="form1">

        <input type="button" value="뒤로 가기" name="btn1">

        <input type="button" value="앞으로 가기" name="btn2">

        <input type="button" value="뒤로 가기 2단계" name="btn3">

    </form>

  

    <script>


        document.form1.btn1.onclick = m1;

        document.form1.btn2.onclick = m2;

        document.form1.btn3.onclick = m3;

  

        function m1(){

            history.back(); //뒤로 가기

        }

  

        function m2(){

            history.forward(); // 앞으로 가기

        }

  

        function m3(){

            history.go(-2); // 뒤로 2칸 가기

        }

  

        //ex19  > 네이버 > 다음 > ex19 > 구글 > 카카오

    </script>

</body>

</html>
```