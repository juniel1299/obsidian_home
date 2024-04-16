```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

  

        #tbl1 {

            border: 1px solid gray;

            border-collapse: collapse; margin-bottom: 10px;

        }

  

        #tbl1 td, #tbl1 th {

            border: 1px solid gray;

            padding: 5px;

        }

  

        #tbl1 th {

            background-color: #EEE;

        }

  

        input {

            outline: none;

        }

  
  

    </style>

</head>

<body>

    <!-- ex25_form.html -->

  

    <h1>회원 가입</h1>

  

    <form name="form1" action="ex25_ok.jsp">

    <table id="tbl1">

        <tr>

            <th>이름</th>

            <td><input type="text" name="txtName"></td>

        </tr>

        <tr>

            <th>나이</th>

            <td><input type="text" name="txtAge"></td>

        </tr>

        <tr>

            <th>아이디</th>

            <td><input type="text" name="txtID"></td>

        </tr>

        <tr>

            <th>암호</th>

            <td><input type="password" name="txtPw"></td>

        </tr>

        <tr>

            <th>암호확인</th>

            <td><input type="password" name="txtPwc"></td>

        </tr>

    </table>

    <input type="button" value="가입하기" name="btnRegister">

    </form>

  

    <script>

  

        var txtName = document.form1.txtName;

        var txtAge = document.form1.txtAge;

        var txtID = document.form1.txtID;

        var txtPw = document.form1.txtPw;

        var txtPwc = document.form1.txtPwc;

  

        document.form1.btnRegister.onclick = m1;

  

        function m1() {

  

            //유효성 검사

            //- 잘못된 값을 찾기!!

  

            //이름

            //- 필수값

            //- 2~5자 이내

            //- 한글만

  

            if (txtName.value.trim() == '') {

                alert('이름을 입력하세요.');

                txtName.focus();

                return;

            }

  

            if (txtName.value.length < 2 || txtName.value.length > 5) {

                alert('2~5자 이내');

                //txtName.value = '';

                //txtName.focus();

                txtName.select();

                return;

            }

  

            for (var i=0; i<txtName.value.length; i++) {

                var c = txtName.value.charAt(i);

                if (c < '가' || c > '힣') {

                    alert('한글만');

                    txtName.select();

                    return;

                }

            }

  
  

            //나이

            //1. 필수값

            //2. 숫자만

            //3. 범위 검사

            if (txtAge.value.trim() == '') {

                alert('나이를 입력하세요.');

                txtAge.focus();

                return;

            }

  

            if (isNaN(txtAge.value)) {

                alert('숫자만');

                txtAge.focus();

                return;

            }

  

            //아이디

            //1. 필수값

            //2. 4~12자 이내

            //3. 영어 + 숫자 + _

            //4. 숫자로 시작 불가

  

            //정규식 객체

  

            var regex=/^[A-Za-z_][A-Za-z0-9_]{3,11}$/;

  

           if(!regex.test(txtID.value)){

               alert('아이디가 올바르지 않습니다..');

               txtID.select();

               return;

           }

  

           if(txtPw.value != txtPwc.value){

               alert('암호가 동일하지 않습니다.');

               txtPwc.focus();

               return;

           }

  

  
  
  

            //<input type="submit"> 클릭

            //- 에뮬레이터 함수

            document.form1.submit();

  

        }//btnRegister.click

  

    </script>

  

</body>

</html>
```