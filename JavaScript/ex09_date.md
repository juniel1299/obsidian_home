# 자바스크립트의 date
내장 객체 : Date
```js
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <script>

  

        /*

        날짜 시간

        - 내장 객체 > Date

  

        현재 시각

  

        */

        //현재 시각

        var now = new Date(); // new 생성자 함수();

        console.log(now);

        console.log(now.toString());

        console.log(typeof now);

  

        //요소 추출

        //- c.get(Calendar.YEAR)

        console.log(now.getYear());         //124 > 1900년대 함수

        console.log(now.getFullYear());     //2024 > 2000년대 함수

        console.log(now.getMonth());        //2 > (0부터)

        console.log(now.getDate());         //22

        console.log(now.getDay());          //5 > (일요일이 0 ~ 토요일이 6)

        console.log(now.getHours());        //14 >

        console.log(now.getMinutes());      //6

        console.log(now.getSeconds());      //27

        console.log(now.getMilliseconds()); //382

        console.log(now.getTime());         //1711083987382 > epoch , tick

  

        //출력 %tF , %tT , %tA 없음

        console.log(now.toString());

        console.log(now.toLocaleString());

        console.log(now.toDateString());

        console.log(now.toTimeString());

  

        console.log(now.toLocaleDateString()); //2024.3.22

        console.log(now.toLocaleTimeString()); // 오후 2:11:10

  

        //특정 시각 만들기

        var christmas = new Date();

  

        christmas.setFullYear(2023);

        christmas.setMonth(11);

        christmas.setDate(25);

  

        christmas.setHours(21);

        christmas.setMinutes(0);

        christmas.setSeconds(0);

  

        console.log(christmas.toLocaleString());

        //var birthday = new Date(1995,10,10);

        var birthday = new Date(1995,10,10,12,30,0);

        console.log(birthday);

  

        //연산

        //시각 - 시각

        console.log(christmas-now); //SQL(일) , JavaScript(ms)

        console.log((christmas-now)/1000/60/60/24);

  

        //시각 + 시간

        //시각 - 시간

        var ani = new Date();

        //   console.log(ani + 10); 안됨

        ani.setTime(ani.getTime() + (100*1000*60*60*24));

        console.log(ani);

  

    </script>

</body>

</html>
```