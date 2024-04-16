```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <h1>라디오 버튼</h1>

  

    <label for=""><input type="radio" name="rb" id="" value="white">흰색</label>

    <label for=""><input type="radio" name="rb" id="" value="black">검은색</label>

    <label for=""><input type="radio" name="rb" id="" value="gold">노랑</label>

    <label for=""><input type="radio" name="rb" id="" value="tomato">빨강</label>

    <label for=""><input type="radio" name="rb" id="" value="cornflowerblue">파랑</label>

  

    <script>

  

        var rb = document.all.rb;

  

        for(var i=0; i<rb.length; i++){

            rb[i].onchange = m1;

        }

  

        function m1(){

            //alert(event.target.value);

            document.body.bgColor = event.target.value;

            if(event.target.value == 'black'){

                document.body.text = 'white';

            }else {

                document.body.text = 'black';

            }

        }

    </script>

</body>

</html>
```