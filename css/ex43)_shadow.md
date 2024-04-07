# shadow 그림자 
1. text-shadow : x, y, blur, color 
2. box-shadow:  x, y, blur, color


```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

<style>
    #box1:hover{

        text-shadow: 1px 1px 3px gray;

        box-shadow: 1px 1px 3px gray;

    }

  

    #box1{

        text-shadow: 1px 1px 3px gray;

    }

</style>

</head>

<body>

    <div id="box1">상자입니다..</div>

</body>

</html>
```