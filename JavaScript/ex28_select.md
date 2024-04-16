```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <h1>셀렉트 박스</h1>

    <select name="sel1" id="" multiple size="5">

        <option value="f1">사과</option>

        <option value="f2">바나나</option>

        <option value="f3">귤</option>

        <option value="f4">망고</option>

        <option value="f5">파인애플</option>

    </select>

  

    <hr>

  

    <input type="button" value="버튼1" name="btn1">

    <input type="button" value="버튼2" name="btn2">

    <input type="button" value="버튼3" name="btn3">

    <input type="button" value="버튼4" name="btn4">

    <input type="button" value="버튼5" name="btn5">

  
  

    <hr>

  
  

    태어난 년도:

    <select name="year" id="">

    </select>

    <script>

        var sel1 = document.all.sel1;

  

        var btn1 = document.all.btn1;

        var btn2 = document.all.btn2;

        var btn3 = document.all.btn3;

        var btn4 = document.all.btn4;

        var btn5 = document.all.btn5;

  

        btn1.onclick = m1;

        btn2.onclick = m2;

        btn3.onclick = m3;

        btn4.onclick = m4;

        btn5.onclick = m5;

  

        function m1(){

            //alert(sel1.value);

            //사용자가 선택한 과일? > 모든 입력 컨트롤 값 > value

            sel1.value = 'f3';

        }

        function m2(){

            //alert(sel1.selectedIndex); //읽기

            sel1.selectedIndex = 4; //쓰기

        }

        function m3(){

            //<option> 중복 추가 방지

                for(var i=0; i<sel1.options.length; i++){

                    //alert(sel1.options[i].text);

                    if(sel1.options[i].text =='배' && sel1.options[i].value =='f6'){

                        return;

                    }

                }

            //동적으로 <option> 추가하기

  

                //<option value="f6">배</option>

  

                var op = new Option(); // <option></option>

                op.value = 'f6';       // <option value='f6'></option>

                op.text = '배';      // <option value='f6'>배</option>

  

                //<select> + <option>

                //sel1.options[5] = op;

                sel1.options.add(op);

            }

        function m4(){

            // 동적으로 <option> 삭제하기 > index shift 발생

                //sel1.options.remove(2);

  

                //사용자 선택 항목 삭제하기

                sel1.options.remove(sel1.selectedIndex);

  

            }

        function m5(){

            //단일 선택

            alert(sel1.value);

  

            //다중 선택

            //for(var i=0; i<sel1.options.length; i++){

                //alert(sel1.options[i].selected);

  

                sel1.options[1].selected = true;

                sel1.options[2].selected = true;

                sel1.options[3].selected = true;

            }

  

            document.all.year

  

            for(var i=1960; i<=2024; i++){

                var op = new Option(i,i);

                document.all.year.options.add(op);

            }

  
  

            document.all.year.value = 2010;

    </script>

</body>

</html>
```