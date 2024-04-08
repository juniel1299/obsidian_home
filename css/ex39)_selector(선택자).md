# 선택자 가상 클래스
1. :first-child
2. :last-child
3. :nth-child(n)
4. :nth-last-child(n)

n
1. 숫자 index
2. 수열 2n, even, odd 존재 

```css
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

<style>

수열 가능 

    li:nth-child(2n){
        color: blue;
    
    
    
    첫번째 자식만 선택
    li:first-child{
        color: blue;
    }

    

    
    마지막 자식만 선택
    li:last-child{
        color: red;
    }
    
    
    원하는 자식 선택 
    li:nth-child(2){
        color: green;
    }
    뒤에서 n 번째 자식
        li:nth-last-child(3){

        color:blueviolet;

    }
    
   #tbl1{

    border:1px solid gray;

    border-collapse: collapse;

}

  

#tbl1 td{

    border: 1px solid gray;

    padding: 5px 10px;

}

  
  

#tbl1 tr:first-child{

    background-color: gold;

}


  

#tbl1 tr:nth-child(2n){

    background-color: #EEE;

}

  

/* 앞에 조건 , 짝수행만 칠해짐 */

#tbl1 tr:nth-child(even) td:nth-child(odd){

    background-color: gold;

}

/* 앞에 조건 , 홀수만 칠해짐 */

#tbl1 tr:nth-child(odd) td:nth-child(evem){

    background-color: gold;

}

</style>

</head>

<body>

    <h1>목록</h1>

  

    <ul id="list1">

        <li>사과</li>

        <li>귤</li>

        <li>바나나</li>

        <li>포도</li>

        <li>참외</li>

        <li>딸기</li>

        <li>복숭아</li>

        <li>파인애플</li>

        <li>망고</li>

        <li>수박</li>

    </ul>

  

    <ul id="list2">

        <li>사과</li>

        <li>귤</li>

        <li>바나나</li>

        <li>포도</li>

        <li>참외</li>

        <li>딸기</li>

        <li>복숭아</li>

        <li>파인애플</li>

        <li>망고</li>

        <li>수박</li>

    </ul>

  

    <h1>테이블</h1>

  

    <!-- table#tbl>tr*20>td*5{data} -->

    <table id="tbl1">

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

        <tr>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

            <td>data</td>

        </tr>

    </table>

  
  

</body>

</html>


```

