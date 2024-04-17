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
