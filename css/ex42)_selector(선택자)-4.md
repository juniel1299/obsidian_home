# CSS 선택자
1. :first-child 
	- 가상 클래스 

2. before
	- 가상 요소

## 전후 선택자 
- 선택자 요소의 앞이나 뒤에 (자식으로) 내용을 추가하는 역할 , 즉 컨텐츠를 생성해냄. 


1. ::bofore
	- before

2. ::after 
	- after


```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <script src="https://kit.fontawesome.com/5a4fce9032.js" crossorigin="anonymous"></script>

    <i class="fa-solid fa-car"></i>

    <style>

 

  
  
  

p > span{color:coral;}

  

/* span 태그 앞에 글자를 넣어라 */

p > span::before{

    content: '문자열';

    color:blue;

    font-size: 2rem;

}

  
/* span 태그 뒤에 글자를 넣어라 */  

p>span::after{

    content: '문자열';

    content: '홍길동';

    color:tomato;

    font-style: italic;

}

  



  
  

p > span::before{

    font-family: "FontAwesome";

    font-weight: 400;

    content: "\e07b";

    margin-right: 5px;

}

i{

    font-size: 10rem;

    color: greenyellow;

}

</style>

</head>

<body>

    <p>Lorem ipsum dolor sit <span>amet</span> consectetur adipisicing elit. Eum corporis <span> laborum</span> ea ad architecto <span> ipsa,</span> libero unde voluptatem quod est veniam nihil recusandae cupiditate quidem consequatur aperiam veritatis nemo odio!</p>

</body>

</html>
```