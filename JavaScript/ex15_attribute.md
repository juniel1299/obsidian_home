# JavaScript 이용해서 html속성 제어 

1. HTML 대부분의 속성은 Javascript에서 동일한 이름의 프로퍼티를 제공함 . 
2. HTML 속성명이 복합어 > Javascript에선 캐멀 표기법으로 표기함 
3. HTML 속성값이 플래그 타입 > boolean 조작 
4. HTML 속성값이 열거형이거나, 색상일 경우 > 문자열 조작 


```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <h1>JavaScript로 태그의 속성을 제어하기</h1>

    <form name="form1">

        <input type="text" name="txt1">

        <input type="button" value="끄기" name="btn1">

    </form>

  

    <script>

  

        var txt1 = window.document.form1.txt1;

        var btn1 = window.document.form1.btn1;

  

        btn1.onclick = m1;

  

        function m1(){

                //txt1.value = '홍길동';

                //alert(txt1.value);

                // txt1.size++;

                //txt1.maxLength = 5;

                //txt1.readOnly = true;

                //txt1.type = 'radio'; 버튼 바꾸기 ㄴㄴ

                //txt1.name = 'txt2'; 식별자 변경 ㄴㄴ



                // 토글 버튼 (Toggle Button)

                // 혼자서 On/Off

                if(window.document.body.bgColor != 'black'){

                window.document.body.bgColor = 'black';

                btn1.value = '켜기';

                }else{

                    window.document.body.bgColor = 'white';

                    btn1.value='끄기';

                }

  
  

            }//btn1.click

  

    </script>

</body>

</html>
```