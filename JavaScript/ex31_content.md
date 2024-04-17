# BOM vs DOM 태그 조작 
1. 태그 검색 (BOM,DOM)
2. 속성 조작 (BOM,DOM)
3. *콘텐츠 조작(DOM)  BOM 못 함* 
4. 이벤트 조작 (DOM , BOM)

# Content 
- 시작 태그와 끝 태그 사이의 내용 (PCDATA , Element) 조작 
1. innerText
	- 시작 태그와 끝 태그 사이의 내용 읽기/쓰기
	- 비표준(MS)
	- 문자열 인식

2. innerHTML
	- 시작 태그와 끝 태그 사이의 내용을 읽기/쓰기 
	- 문자열 + 태그 인식

3. textContent 
	- 시작 태그와 끝 태그 사이의 내용을 읽기/쓰기
	- 표준
	- 문자열 인식

이외에도 outerText , outerHTML 존재 .



예시

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <h1>Content</h1>

  

    <input type="button" value="버튼1" id="btn1">

    <input type="button" value="버튼2" id="btn2">

  

    <hr>

  

    <div id="div1">홍<b>길동</b></div>

  

    <script>

  

        


        document.getElementById('btn1').onclick = m1;

  

        function m1(){

            var div1 = document.getElementById('div1');

            //읽기

            //alert(div1.innerText); //텍스트만 나옴

            //alert(div1.innerHTML); //코드 그대로 나옴

            //alert(div1.textContent);

            //div1.innerText = '아<i>무</i>개'; // 덮어쓰기 , 쓸 땐 다 나옴;;

            //div1.innerHTML = '아<i>무</i>개'; //덮어쓰기 , 태그를 이해하므로 정상적용됨

  


    }

  

    document.getElementById('btn2').onclick = m2;

    function m2(){


        document.getElementById('div1').innerHTML = '';

    }

    </script>

</body>

</html>

```

예시
```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

        fieldset {

            border: 1px solid #777;

            width: 200px;

        }

  

        fieldset > label {

            display: block;

            margin-bottom: 10px;

        }

  

        #tbl1{

            border: 1px solid gray;

            border-collapse: collapse;

            margin-top: 20px;

        }

        #tbl1 td{

            border:  1px solid gray;

            width: 50px;

            height: 50px;

        }

  

    </style>

</head>

<body>

    <h1>테이블 생성하기</h1>

  

    <fieldset>

        <legend>행x열</legend>

        <label>행: <select id="selRow"></select></label>

        <label>열: <select id="selColumn"></select></label>

        <input type="button" value="생성하기" id="btn1">

    </fieldset>

  

    <table id="tbl1"></table>

  

    <script>

        var selRow = document.getElementById('selRow');

        var selColumn = document.getElementById('selColumn');

        var btn1 = document.getElementById('btn1');

        var tbl1 = document.getElementById('tbl1');

  

        for(var i=1; i<=10; i++){

            //var op = new Option(i,i);

            selRow.options.add(new Option(i,i));

            selColumn.options.add(new Option(i,i));

        }

  

        selRow.selectedIndex = 4;

        selColumn.selectedIndex = 4;

  

        btn1.onclick = m1;

        function m1(){

            //<tr>,<td> 동적 생성하기

                var temp = ''; //누적 변수

  

                //tbl1.innerHTML = '<tr></tr>';

                for(var i=0; i<selRow.value; i++){

                    temp += '<tr>';

                    for(var j=0; j<selColumn.value; j++){

                        temp += '<td>';

                        temp +=(i+','+j);

                        temp +='</td>';

                    }

                    temp += '</tr>';

                }

                //<table><tr> -> 중간에 tbody 없음

                tbl1.innerHTML = temp;

            }

    </script>

</body>

</html>
```

예시
```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

        #tbl1 {

            border: 1px solid black;

            border-collapse: collapse;

        }

        #tbl1 td {

            border: 1px solid black;

            width: 126px;

            height: 126px;

            /* font-size: 0; */

        }

        #tbl1 td img {

            display: block;

        }

    </style>

</head>

<body oncontextmenu="return false;">

    <!-- ex33_content.html -->

    <table id="tbl1">

        <tr>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

        </tr>

        <tr>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

        </tr>

        <tr>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

        </tr>

        <tr>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

        </tr>

        <tr>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

        </tr>

    </table>

  

    <script>

  

        //<td> x 25 이벤트 추가

        //document.getElementsByTagName('td')

        var list = document.querySelectorAll('#tbl1 td');

  

        //alert(list.length);

        for (var i=0; i<list.length; i++) {

            //list[i].onclick = m1;

            list[i].onmousedown = m1;

        }

  

        function m1() {

            //alert();

            //어떤 <td>를 클릭?

            //event.target.bgColor = 'gold';

            //event.target.innerText = 'click';

            //alert(event.buttons);

  

            if (event.buttons == 1) {

                event.target.innerHTML = '<img src="images/rect_icon01.png">';

            } else if (event.buttons == 2) {

                event.target.innerHTML = '<img src="images/rect_icon02.png">';

            }

        }

  
  

    </script>

  

</body>

</html>
```