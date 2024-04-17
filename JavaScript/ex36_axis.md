# Axis 검색 
- 나를 중심으로 부모,자식,형제를 탐색 


## DOM 트리 구성요소(노드)
1. 태그 (1)
2. 속성(2)
3. PCDATA(3)
4. 주석(8)
5. 선언문(13)
...

## DOM 노드 프로퍼티 
1. nodeType : 해당 노드가 어떤 형식 
2. nodeName : 해당 노드의 이름 
	- 태그(태그명)
	- 속성(속성명)
	- PCDATA(\#text)
3. nodeValue : 해당 노드의 값 
	- 태그(null)
	- 속성(속성값)
	- PCDATA(문자열)

예시

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

  

        div {

            border: 1px solid black;

            padding: 15px;

            margin: 15px;

        }

  

        #me {

            border: 10px solid cornflowerblue;

        }

  

        .check {

            outline: 10px solid coral;

        }

  

    </style>

</head>

<body>

    <!-- ex36_axis.html -->

  

    <h1>Axis</h1>

  

    <input type="button" value="버튼" id="btn1">

    <hr>

    <div>

        할아버지

        <div>

            큰아버지

            <div>사촌</div>

        </div>

        <div>

            아버지

            <div>큰형</div>

            <div>작은형</div>

            <div id="me">

                나

                <div>자식</div>

                <div>

                    자식

                    <div>손자</div>

                </div>

                <div>자식</div>

            </div>

            <div>동생</div>

            <div>막내동생</div>

        </div>

        <div>

            작은아버지

            <div>사촌</div>

        </div>

    </div>

  

    <script>

  

        //Axis 검색

        //- 나를 중심으로 부모,자식,형제를 탐색

        document.getElementById('btn1').addEventListener('click', m2);

  

        function m1() {

  

            var me = document.getElementById('me');

  

            //<body class="check">

            //document.body.className = 'check';

  

            //자식 태그

            //- me.childNodes

            //alert(me.childNodes.length);

  

            for (var i=0; i<me.childNodes.length; i++) {

  

                //console.log(me.childNodes[i]);

                /*  

                    DOM 트리 구성요소(=노드)

                    1. 태그(1)

                    2. 속성(2)

                    3. PCDATA(3)

                    4. 주석(8)

                    5. 선언문(13)

                    6. ..

  

                    DOM 노드 프로퍼티

                    1. nodeType > 해당 노드가 어떤 형식

                    2. nodeName > 해당 노드의 이름

                                    - 태그(태그명)

                                    - 속성(속성명)

                                    - PCDATA(#text)

                    3. nodeValue > 해당 노드의 값

                                    - 태그(null)

                                    - 속성(속성값)

                                    - PCDATA(문자열)

  

                */

  

                // console.log(

                //     me.childNodes[i].nodeType,

                //     me.childNodes[i].nodeName,

                //     me.childNodes[i].nodeValue

                // );

  

                if (me.childNodes[i].nodeType == 1

                    && me.childNodes[i].nodeName == 'DIV') {

                    me.childNodes[i].className = 'check';

                }

  

            }//for

  

        }//m1

  

        function m2() {

  

            var me = document.getElementById('me');

  

            //- me.childNodes > 모든 노드

            //- me.children > 태그만

            //alert(me.children.length);

  

            // for (var i=0; i<me.children.length; i++) {

            //     me.children[i].className = 'check';

            // }

  

            //- me.childNodes

            //- me.firstChild == me.childNodes[0]

            //- me.lastChild == me.childNoes[length-1]

  

            //- me.children

            //- me.firstElementChild

            //- me.lastElementChild

  

            //me.firstElementChild.className = 'check';

            //me.children[0].className = 'check';

            //me.lastElementChild.className = 'check';

  

            //me.children[1].firstElementChild.className = 'check';

  
  

            //부모 or 조상

            //- me.parentNode

            //- me.parentElement

  

            //me.parentNode.className = 'check';

            //me.parentElement.className = 'check';

  

            //me.parentElement.parentElement.className = 'check';

  

            //me.parentElement.parentElement.parentElement.className = 'check'; //<body>

            //alert(me.parentElement.parentElement.parentElement.parentElement.nodeName);

  

            //me.parentElement.parentElement.parentElement.parentElement.className = 'check';

  

            //console.log(me.parentElement.parentElement.parentElement.parentElement.parentNode.parentNode);

  
  

            //형제 탐색

            //- me.previousSibling > 바로 위의 형제(모든 노드)

            //- me.nextSibling > 바로 밑의 형제(모든 노드)

            //- me.previousElementSibling > 태그

            //- me.nextElementSibling > 태그

  

            //me.parentElement.firstElementChild.className = 'check';

            //me.previousElementSibling.previousElementSibling.className = 'check';

  

            //me.nextElementSibling.className = 'check';

            me.nextElementSibling.nextElementSibling.className = 'check';

            //HTML

            //- id와 class 남발 > 가독성 저하, 코드 관리 열약

            //id or class > 검색 > 1개의 태그 > 상대 검색

  
  

        }//m2

  

    </script>

  

</body>

</html>

```

