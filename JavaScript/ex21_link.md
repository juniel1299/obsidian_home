```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <h1>링크</h1>

  

    <a href="https://naver.com" name="link1">네이버</a>

  

    <hr>

  

    <input type="button" value="버튼" name="btn1">

  

    <script>

  

        var list = ['강아지','고양이','팬더','병아리','닭'];

  

        console.log(list[0]);

  

        document.all['btn1'].onclick =m1;

  

        function m1(){

            //document.all['link1']

            //document.links[0]

            //document.links['link1']

  
  

            //BOM 영역

            //alert(document.links['link1'].href) 읽기

            document.links['link1'].href = 'https://google.com'; //버튼 누르면 구글로 바꾸기

            document.links['link1'].target = '_blank';        //새창에서 띄우기    

            document.links['link1'].title = '구글로 이동합니다.';

            //DOM 영역

            document.links['link1'].innerText='구글'; //네이버라 써있던 글자를 구글로 바꿈

        }

  
  

        //document.all[]

  

    </script>

</body>

</html>
```

