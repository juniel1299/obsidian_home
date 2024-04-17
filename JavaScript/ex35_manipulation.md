# 자바스크립트 DOM , 동적으로 태그 생성하기
1. innerHTML
- 쉽고 작성 비용이 낮음 
- 간단한 작업에 유용함
- **모든것을 문자열로 조작한다**

2. 정석
- 복잡하다 + 작성 비용 고가 
- 복잡한 작업 


```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <!-- ex35_manipulation.html -->

    <h1>DOM 조작</h1>

  

    <input type="button" value="버튼1" id="btn1">

    <input type="button" value="버튼2" id="btn2">

    <input type="button" value="버튼3" id="btn3">

    <input type="button" value="버튼4" id="btn4">

    <hr>

    <div id="div1"></div>

  

    <script>

        document.getElementById('btn1').addEventListener('click', m1);

        document.getElementById('btn2').addEventListener('click', m2);

        document.getElementById('btn3').addEventListener('click', m3);

        document.getElementById('btn4').addEventListener('click', m4);

        var div1 = document.getElementById('div1');

  

        function m1() {


            //div1.innerHTML = '<input type="text" size="10">';

  

            //2. 정석

            //  - 복잡하다. + 작성 비용 고가

            //  - 복잡한 작업

  

            //2.1 태그 객체 생성

            var input = document.createElement('input'); //<input>

  

            //2.2 속성 추가

            //- input.type = 'text'; //BOM

            //- input.size = 10;     //BOM

  

            var type = document.createAttribute('type'); //type=""

            type.value = 'text'; //type="text"

            input.setAttributeNode(type); //<input type="text">

  

            //<input type="text" size="10">

            input.setAttribute('size', 10);

  

            div1.appendChild(input); //자식으로 추가

  

            //<p align="center">문단입니다.</p>

  

            //div1.innerHTML += '<p align="center">문단입니다.</p>';

  

            var p = document.createElement('p'); //<p></p>

  

            p.setAttribute('align', 'center'); //<p align="center"></p>

  

            var txt = document.createTextNode('문단입니다.');

            //txt.value = '문단입니다.2';

            p.appendChild(txt); //<p align="center">문단입니다.</p>

  

            p.textContent = '문단입니다.';

  

            div1.append(p);

  

        }

        function m2() {

            //태그 삭제하기

            //div1.innerHTML = '';

  

            //<input type="text" size="10"><p align="center">문단입니다.</p>

            //alert(div1.innerHTML);

  

            div1.removeChild(div1.childNodes[1]);

  

        }

        function m3() {

            //고양이 x 5 + 클릭 이벤트

            //for (var i=1; i<=5; i++) {

            //    div1.innerHTML += '<img src="images/catty0' + i + './/png" onclick="f1();">';

            //}

  

            for (var i=1; i<=5; i++) {

  

                var img = document.createElement('img');

                img.setAttribute('src', 'images/catty0' + i + '.png');

                img.addEventListener('click', f1);

  

                div1.appendChild(img);

  

            }

  

        }

        function m4() {

        }

        function f1() {

            //alert(event.target.src);

            //div1.innerHTML = '나머지 고양이만..'

            div1.removeChild(event.target);

        }

    </script>

  

</body>

</html>
```