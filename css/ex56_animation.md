# animation
- css에서의 애니메이션 
	- transition
	- animation

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <script src="https://kit.fontawesome.com/7121714adf.js" crossorigin="anonymous"></script>

  

    <style>

    /*

        CSS 애니메이션

        1. transition

        2. animation

  

    */

  

    body{

        padding:100px;

    }

    body:hover #box{

  

        /*animation-name: key3;*/

        animation-duration: 1s;

        animation-fill-mode: forwards;

        animation-timing-function: linear;

        animation-delay: 0s;

        animation-iteration-count: 3;

        animation-direction: alternate-reverse;

    }

  

    @keyframes key1{

        from{

            width:200px;

        }to{

            width:400px;

        }

  

    }

    @keyframes key2{

        0% {width: 200px;}

        50%{width: 400px;}

        100%{width: 600px;}

    }

  

    @keyframes key3{

        0%{transform: translate(0px,0px);}

        25%{transform: translate(300px,0px);}

        50%{transform: translate(300px,300px);}

        75%{transform: translate(0px,300px);}

        100%{transform: translate(0px,0px);}

    }

    #box{

        width: 200px; height: 200px;

        background-color: gold;

     /*   transition:all 1s;*/

    }

  

/*

  

    진동 효과

  

*/

  

.effect:hover{

    animation-name: key-effect;

    animation-duration: 0.1s;

    animation-iteration-count: 5;

}

  

@keyframes key-effect {

    0%{transform: translate(0px,0px);}

    25%{transform: translate(-1px,0px);}

    50%{transform: translate(0px,0px);}

    75%{transform: translate(1px,0px);}

    100%{transform: translate(0px,0px);}

  

}

  

#effect2 > i{

    color: red;

}

  

#effect2:hover > i{

    animation-name: key-effect;

    animation-duration: 0.2s;

    animation-iteration-count: 10;

}

</style>

</head>

<body>

    <h1 id="box">상자</h1>

  

    <button class="effect">글쓰기</button>

    <button class="effect">가입하기</button>

    <button class="effect">로그인</button>

  
  

    <hr>

  

    <button id="effect2">

        <i class="fa-solid fa-right-to-bracket"></i>

        글쓰기

    </button>

</body>

</html>
```


```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <style>

#box{

    border: 20px solid black;

    width: 400px;

    height: 800px;

}

#ball{

    background-color: cornflowerblue;

    width: 50px;

    height: 50px;

    border-radius: 50%;

    margin: 0 auto;

    animation-name: key-ball;

    animation-duration: 0.3s;

    animation-iteration-count: infinite;

    animation-direction: alternate;

    animation-timing-function: ease-in;

  

}

  

@keyframes key-ball{

    from{ transform: translate(0,0);}

    to{ transform: translate(0px,750px);}

}

    </style>

</head>

<body>

    <div id="box">

        <div id="ball"></div>

    </div>

</body>

</html>
```

