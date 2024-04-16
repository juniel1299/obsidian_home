1. BOM 
	- Browser Object Model
		- 트리 구조 
		- 일부 태그
		- 기능 부족

2. DOM
	- Document Object Model
		- 트리 구조 
		- 모든 태그 조작 
		- 기능 풍부 


## DOM
- BOM 기능 + 확장 기능 
- BOM > name 식별자 사용 가능 
- DOM > name , id , class 등 ... > 태그 검색이 더 쉬워짐 
- CSS > 


```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

        .txts{

            display: block;

            margin-bottom: 5px;

        }

    </style>

</head>

<body>

    <h1>DOM</h1>

  

    <form name="form1">

        <h2 id="title">controls</h2>

        <div>

            <input type="text" name="txt1" id="txt1" class="txts">

            <input type="text" name="txt2" id="txt2" class="txts">

            <input type="text" name="txt3" id="txt3" class="txts">

            <input type="button" value="버튼" name="btn1">

        </div>

        <script>

            /*

                자바스크립트 > 어떤 시각 > HTML

  

                1.BOM

                    - Browser Object Model

                        - 트리 구조

                        - 일부 태그

                        - 기능 부족

  

                2.DOM

                    - Document Object Model

                        - 트리 구조

                        - 모든 태그 조작

                        - 기능 풍부

  

                DOM

                - BOM 기능 + 확장 기능

                - BOM > name 식별자 사용 가능

                - DOM > name, id, class 등.... > 태그 검색하기가 좋아짐.

                - CSS 조작 가능(BOM 불가능)

                - DOM Level 1 > DOM Level 2 > DOM Level 3

  

                BOM의 최상위 객체 > window

                DOM의 최상위 객체 > document

  

                DOM에서 제공하는 태그 검색 도구(함수) > 1,2,5 많이 씀

                1. id 검색 > document.getElementById("id")

                2. class 검색 > document.getElementsByClassName("class")

                3. name 검색 > document.getElementsByName("name")

                4. tag 검색 > document.getElementsByTagName("tag")

                5. CSS 선택자 검색

                    - ES6 추가(2014년) > 이전에는 개발자가 직접 만들거나, 각종 라이브러리에서 제공함

                    - document.querySelector() > 단수

                    - document.querySelectorAll() > 복수

            */

  

            //<input type="text" name="txt1" id="txt1" class="txts">

  

            //BOM

            //document.form1.txt1.value = 'BOM';

  

            //DOM

            //id

            //document.getElementById('txt1').value = 'DOM';

            //*** 검색된 결과는 동일한 객체다.

            //console.log(document.form1.txt1 === document.getElementById('txt1'));

  

            //class

            var txts = document.getElementsByClassName('txts');

            console.log(txts.length);   //배열임;

            console.log(typeof txts); //object

  

            //for( var i=0; i<txts.length; i++){

           //     txts[i].value = i;

           // }

  
  
  

           //name > DOM에서는 name 검색을 잘 안함.

           document.getElementsByName('txt1')[0].value = '홍길동'; //배열이라 elements임

  

            //tag name > 검색을 잘 안함

            //var list = document.getElementsByTagName('input');

            //console.log(list.length);

  

            //태그 검색

            //document.querySelector('#txt1').value = 100;

           console.log(document.querySelectorAll('.txts:nth-child(odd)').length); //복수 > 2개

            //document.querySelector('.txts:nth-child(odd)').value=100; //단수 > 1개

        </script>

    </form>

</body>

</html>
```