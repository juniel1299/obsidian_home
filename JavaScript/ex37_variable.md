# JavaScript Core 변수선언하기 
1. var 
- BOM / DOM / ES6
- function-scoped
- 제어문(영역 인식 불가능)
- 중복 선언 가능
- 상수 선언 불가능 (final)

2. let
- ES6(ECMAScript 2015)
- block-scoped(함수, 제어문)
- 중복 선언 불가능
- 변수 

3. const
- ES6 (ECMAScript 2015)
- block-scoped(함수, 제어문)
- 중복 선언 불가능 
- 상수(=final 변수)

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <!-- ex37_variable.html -->

  

    <script>

        //var a = 10;

        //var a = 20;

        //console.log(a);

  

        let a = 10; //전역 변수

  

        function m1() {

            let b = 20; //지역 변수(m1)

        }

  

        m1();

        //console.log(b);

  

        if (a > 0) {

            let c = 30; //지역 변수(if)

            var d = 40; //전역 변수

        }

        //console.log(c);

        console.log(d);

  

        //Cannot redeclare block-scoped variable 'a'

        //let a = 50;

  

        const PI = 3.14;

        //PI = 5.28; //Assignment to constant variable.

  

        var list = [ 10, 20, 30, 40, 50 ];

  

        for (var i=0; i<list.length; i++) {

  

        }

  

        console.log(i);

  

        for (let j=0; j<list.length; j++) {

  

        }

  

        console.log(j);

  
  

    </script>

  

</body>

</html>
```

