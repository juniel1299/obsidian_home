# 자바스크립트의 자료형 
1. number 
	- 숫자형(정수,실수)

2. string 
	- 문자, 문자열

3. boolean
	- 논리형

4. object
	- 객체형
	- JavaScirpt에는 클래스가 없음 (ES6부터 추가됨)
	- 객체 기반의 언어 

5. 기타(상수)
	- null
	- undefined
	- NaN(not a number)

6. 변수, 상수(리터럴)
	- var 변수명;
	- JavaScirpt는 변수의 타입이 없다.
	- 변수는 모든 자료형의 데이터를 저장 할 수 있다. (자바의 Object 변수)

*typeof 를 통해 자료형을 확인 할 수 있다.*

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <script>
  

        var num;

        num = 10;

        console.log(num);

        num = "안녕";

        console.log(num);

        num = true;

        console.log(num);

  

        //현재 변수나 상수의 자료형을 확인 > 연산자

        console.log(typeof 100);

        console.log(typeof 3.14);

        console.log(typeof num);

        console.log(typeof "홍길동");

        console.log(typeof false);

        console.log(typeof new Date());

  
  

        // 연산자

        //자바와 같음

  

        //제어문

        //자바와 같음

  

        // Java > Strong Type

        // SQL > Weak Type

        // JavaScript > Weak Type

  

        console.log('10'+2);

        console.log('10'*2);

        console.log(2+'10');

  

        //문자 이스케이프

        //자바와 같음

  

        console.log('C:\\class\\java');

    </script>

</body>

</html>
```