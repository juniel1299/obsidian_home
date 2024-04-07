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
    뒤에서 2번째 
        li:nth-last-child(3){

        color:blueviolet;

    }
```

