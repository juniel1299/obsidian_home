# 선택자 가상 클래스
1. :first-child
2. :last-child
3. :nth-child(n)
4. :nth-last-child(n)

n
1. 숫자 index
2. 수열 2n, even, odd 존재 

```css
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
```

