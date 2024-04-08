```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

<style>

    #list input {

        display: block;

        margin-bottom: 5px;

        border: 1px solid #444;

        outline: none;

        padding:4px;

        background-color: #ffffff;

        color:#444;

    }

/*따로 서식을 지정해주는 방법 */

    #list input:required{

        background-color: gold;

    }

/*required의  반대 */

    #list input:optional{

        background-color: gray;

    }

/* 사용 불가능한거 표시*/

    #list input:disabled{

        background-color: red;

    }

/* disabled 반대*/

    #list input:enabled{

        background-color: aqua;

    }

/*읽기 전용 -> disable도 포함임 */

    #list input:read-only{

        background-color: lavender;

        cursor:not-allowed;

    }

/* read-only 반대 */

    #list input:read-write{

        background-color: chartreuse;

    }

  

    input[type=checkbox]{

        opacity: 0.3;

    }

  

    input[type=checkbox]:checked{

        opacity: 1;

    }

  

    #cb1:checked + div{

        display: none;

    }

  

    #item{

        border: 1px solid black;

        width: 200px;

    }

  

    #item #cb2{

        display: none;

    }

  
  

    #item label{

        font-size: 1.5rem;

        font-family: arial;

        font-variant: small-caps;

        display: block;

        padding: 10px;

        background-color: cornflowerblue;

        color: white;

        cursor: pointer;

    }

  

    #item div{

        display: none;

        border-top: 1px solid black;

        padding: 15px;

    }

  

    #item #cb2:checked + label + div{

        display: block;

    }

</style>

</head>

<body>

  

    <div id="item">

        <input type="checkbox" id="cb2">

        <label for="cb2">JavaScript</label>

        <div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur recusandae quod dignissimos voluptatibus optio et laboriosam atque impedit, eligendi, vero magnam ducimus quas distinctio quisquam quasi repudiandae nihil. Autem aliquam quibusdam molestiae quo aliquid laudantium aut nihil sed ducimus? Minus nulla iure libero velit eius laboriosam sit sequi fugit maxime!</div>

    </div>

  

    <hr>

  
  
  
  

    <label for="cb1">설명 감추기</label>

    <input type="checkbox" id="cb1">

    <div>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Unde nobis maiores quod neque laudantium voluptatibus delectus exercitationem nulla quae. Libero facere quisquam optio incidunt maxime inventore quaerat eos distinctio animi.</div>

  
  
  

    <hr>

    <div>

        <input type="checkbox">

        <input type="checkbox">

        <input type="checkbox">

    </div>

  
  

    <hr>

  

    <div id="list">

        <input type="text" value="1" required>

        <input type="text" value="2" readonly>

        <input type="text" value="3" readonly>

        <input type="text" value="4">

        <input type="text" value="5" required>

        <input type="text" value="6" disabled>

        <input type="text" value="7">

        <input type="text" value="8" disabled>

        <input type="text" value="9">

        <input type="text" value="10" required>

    </div>

</body>

</html>
```