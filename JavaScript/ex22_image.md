```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <!-- ex22_image.html -->

    <h1>이미지</h1>

  

    <input type="button" value="버튼" name="btn1">

    <hr>

  

    <img src="images/cat01.jpg" name="cat1">

    <hr>

  

    <img src="images/cat01.jpg" name="cat2">

    <hr>

  

    <img src="images/switch_on.png" name="sw">

    <hr>

  

    <img src="images/rect_icon01.png" name="icon">

    <hr>

  

    <img src="images/dog01.jpg" name="dog">

    <hr>

  

    <img src="images/0.png" name="number">

    <hr>

  

    <script>

  

        document.all['btn1'].onclick = m1;

  

        function m1() {

            //document.images['cat1'].width = 500;

            document.images['cat1'].src = 'images/cat02.jpg';

        }

  

        document.images['cat2'].onmouseover = m2;

        document.images['cat2'].onmouseout = m3;

  

        //롤오버 이미지 효과

        function m2() {

            document.images['cat2'].src = 'images/cat02.jpg';

        }

        function m3() {

            document.images['cat2'].src = 'images/cat01.jpg';

        }

  
  

        document.images['sw'].onclick = m4;

        function m4() {

  

            //http://192.168.10.30:5500/javascript/images/switch_on.png

            //alert(document.images['sw'].src);

  

            if (document.images['sw'].src.endsWith('switch_on.png')) {

                document.images['sw'].src = 'images/switch_off.png';

                document.body.bgColor = 'black';

            } else {

                document.images['sw'].src = 'images/switch_on.png';

                document.body.bgColor = 'white';

            }

  

        }

  

        var n = 1;

        document.images['icon'].onclick = m5;

        function m5() {

  

            n++;

            if (n > 18) {

                n = 1;

            }

  

            document.images['icon'].src = 'images/rect_icon'

                            + (n + '').padStart(2, '0') + '.png';

  

        }

  
  

        var no = 1;

        window.onkeydown = m6;

        function m6() {

            if (event.keyCode == 37) {

                //이전 이미지

                no--;

                if (no < 1) {

                    //alert('처음 이미지입니다.');

                    //no++;

                    //return;

                    no = 5;

                }

            } else if (event.keyCode == 39) {

                //다음 이미지

                no++;

                if (no > 5) {

                    //alert('마지막 이미지입니다.');

                    //no--;

                    //return;

                    no = 1;

                }

            }

            document.images['dog'].src

                = 'images/dog0' + no + '.jpg';

        }

  

        window.onkeydown = m7;

        function m7() {

            //상단 숫자키: 0(48)~9(57)

            //좌측 키패드: 0(??)~9(??)

            //alert(event.keyCode);

            if (event.keyCode >= 48 && event.keyCode <= 57) {

                document.images['number'].src

                    = 'images/' + (event.keyCode - 48) + '.png';

            }

        }

  
  

    </script>

  

</body>

</html>
```