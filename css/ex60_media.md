# Media Query
- 반응형 웹(Responsive Web) : 해상도에 따라 다른 화면을 구현하는 CSS 기술
- 모바일 웹을 지원하기 위해 사용하기 시작 

## 미디어 유형
1. all
2. screen : 컴퓨터 모바일 (기본값)
3. print : 프린터기 화면 기준 
4. tv
5. projection

## 미디어 쿼리 연산자
1. and
2. only
3. not

## 미디어 쿼리 조건 
1. 모바일 : 화면 <=480px
2. 태블릿 : 화면 <=768px
3. 태블릿(가로) : 화면 화면 <=1024px
4. 랩탑 : 화면 <=1600px
5. 데스크탑 : 화면  > 1600px


```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>


            body{

                background-color: gold;

            }

  

            @media screen and (max-width: 800px){

                body{

                    background-color: cornflowerblue;

                }

            }

    </style>

</head>

<body>

</body>

</html>
```