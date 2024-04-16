```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <!-- ex26_checkbox.html -->

    <h1>체크 박스</h1>

  

    <form name="form1">

        <input type="checkbox" name="cb1">

        <input type="button" value="버튼" name="btn1">

    </form>

  

    <hr>

  

    <h2>회원 가입</h2>

  

    <p>회원 약관..</p>

  

    <label><input type="checkbox" name="cbAgree"> 약관에 동의합니다.</label>

    <input type="button" value="다음으로" name="btnNext" disabled>

  
  

    <hr>

  

    <h2>장바구니</h2>

  

    <table border width="500">

        <tr>

            <th><input type="checkbox" name="cbAll"></th>

            <th>상품명</th>

            <th>수량</th>

            <th>가격</th>

        </tr>

        <tr>

            <td><input type="checkbox" name="cbItem"></td>

            <td>노트북</td>

            <td>1</td>

            <td>2,000,000원</td>

        </tr>

        <tr>

            <td><input type="checkbox" name="cbItem"></td>

            <td>노트북</td>

            <td>1</td>

            <td>2,000,000원</td>

        </tr>

        <tr>

            <td><input type="checkbox" name="cbItem"></td>

            <td>노트북</td>

            <td>1</td>

            <td>2,000,000원</td>

        </tr>

        <tr>

            <td><input type="checkbox" name="cbItem"></td>

            <td>노트북</td>

            <td>1</td>

            <td>2,000,000원</td>

        </tr>

        <tr>

            <td><input type="checkbox" name="cbItem"></td>

            <td>노트북</td>

            <td>1</td>

            <td>2,000,000원</td>

        </tr>

        <tr>

            <td><input type="checkbox" name="cbItem"></td>

            <td>노트북</td>

            <td>1</td>

            <td>2,000,000원</td>

        </tr>

        <tr>

            <td><input type="checkbox" name="cbItem"></td>

            <td>노트북</td>

            <td>1</td>

            <td>2,000,000원</td>

        </tr>

        <tr>

            <td><input type="checkbox" name="cbItem"></td>

            <td>노트북</td>

            <td>1</td>

            <td>2,000,000원</td>

        </tr>

        <tr>

            <td><input type="checkbox" name="cbItem"></td>

            <td>노트북</td>

            <td>1</td>

            <td>2,000,000원</td>

        </tr>

    </table>

  

    <script>

        var cb1 = document.form1.cb1;

        var btn1 = document.form1.btn1;

        var cbAgree = document.all.cbAgree;

        var btnNext = document.all.btnNext;

  

        btn1.onclick = m1;

  

        function m1() {

            //cb1.checked = true;

            cb1.checked = !cb1.checked;

        }

  
  

        //cbAgree.onclick = m2;

        cbAgree.onchange = m2;

  

        function m2() {

            //alert(cbAgree.checked);

            if (cbAgree.checked) {

                btnNext.disabled = false;

            } else {

                btnNext.disabled = true;

            }

        }

  
  

        document.all.cbAll.onchange = m3;

  

        function m3() {

  

            // if (event.target.checked) {

  

            //     for (var i=0; i<document.all.cbItem.length; i++) {

            //         document.all.cbItem[i].checked = true;

            //     }

  

            // } else {

  

            //     for (var i=0; i<document.all.cbItem.length; i++) {

            //         document.all.cbItem[i].checked = false;

            //     }

  

            // }

  
  

            for (var i=0; i<document.all.cbItem.length; i++) {

                document.all.cbItem[i].checked = event.target.checked;

            }

  

        }

  

    </script>

  

</body>

</html>
```