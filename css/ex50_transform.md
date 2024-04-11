# transform 변형, 
- 요소의 위치 크기 회전 , 비틀기(왜곡)
- transform : 값;  
- 값에 해당하는 코드 
	- 1. translate() : 위치 변형 
	- 2. scale() 크기(배율) 변형
	- 3. rotate() 회전 변형
	- 4. skew() 왜곡 변형
	- 5. matrix() 행렬
- position : 레이아웃
- transform : 인터페이스(사용법)

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

    <link rel="stylesheet" href="css/box.css">

<style>

  

    /*

    변형, transform

    - 요소의 위치, 크기, 회전, 비틀기(왜곡)

    - transform: 값;

  

    값(함수)

    1.translate() > 위치 변형

    2.scale() > 크기(배율) 변형

    3.rotate() > 회전 변형

    4.skew() > 왜곡 변형

    5.matrix() > x(행렬)

  
  
  
  
  

    1. position : 레이아웃

    2. transform: 인터페이스(사용법)

    */

  
  

    #box2{

        /*transform: translate(100px, 100px);*/

       /* transform: scale(-0.5,1);

        margin-left: 300px;

        */

        /*transform: rotate(110deg);*/

        transform: skew(89deg, 89deg);

    }

  

    /*#cat img:hover{

        transform: translate(0px, -15px);

    }*/

  

    /* #cat:hover img{

        transform: translate(0px,-15px);

    }*/

  

    /*

    #cat img:hover ~ img{

        transform: translate(0px,-15px);

    }

    */

   /* #cat:hover img:nth-child(even){

        transform: translate(0px,-15px);

    }*/

  

    #cat img:hover{

     /*   transform: translate(0px,-55px) scale(1.4,-1.4);*/

  

     transform: rotate(20deg);

    }

  
  

    #txt1{

        margin: 50px;

        font-size: 2rem;

        padding: 10px;

     /*   transform: scale(-1,-1); */

       /* transform: rotate(45deg);*/

    }

  

    body{

    }

</style>

  

</head>

<body>

    <div id="box1" class="box bgcolor-red border10"></div>

    <div id="box2" class="box bgcolor-yellow border10">dd</div>

    <div id="box3" class="box bgcolor-blue border10"></div>

  

    <input type="text" class="bgcolor-blue">

  

    <h1>고양이</h1>

    <div id="cat">

        <img src="images/catty01.png" alt="">

        <img src="images/catty02.png" alt="">

        <img src="images/catty03.png" alt="">

        <img src="images/catty04.png" alt="">

        <img src="images/catty05.png" alt="">

    </div>

  

    <div>

        <input type="text" id="txt1">

    </div>

</body>

</html>
```


## 인접한 인라인 태그 사이에 공백 없애는 법 
1. 직접 지우기 (안 씀)
2. font-size : 0 ; (추가 코드 발생(내부 컨텐츠 글꼴 크기 재정의))
3. float (추가 코드 발생(clear))
4. flex (추가 코드 발생 없음)


```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

<style>

/*

  

    인접한 인라인 태그 사이의 공백을 없애는 방법

    1. 직접 공백을 지운다 > 사용x

    2. font-size : 0; > 추가 코드 발생(내부 컨텐츠 글꼴 크기 재정의)

    3. float > 추가 코드 발생(clear)

    4. flex > 추가 코드 발생(X)

*/

  
  

#menu{

    font-size: 0;

    width: 630px;

    margin: 0 auto;

    transform: translate(0px,-100px);

}

  
  

#menu > img:hover{

    transform: translate(0px,80px);

}

  

#sub-menu{

    font-size: 0;

    width: 126px;

    transform: translate(-110px,0px);

}

  

#menu > img{

    transition: all .7s;

}

  

#sub-menu > img{

    transition: all .7s;

}

  

#sub-menu > img:hover{

    transform: translate(90px,0px);

}

  
  
  

</style>

</head>

<body>

    <nav id="menu">

        <!-- img[src=images/rect_icon$$.png]*5 -->

        <img src="images/rect_icon01.png" alt="">

        <img src="images/rect_icon02.png" alt="">

        <img src="images/rect_icon03.png" alt="">

        <img src="images/rect_icon04.png" alt="">

        <img src="images/rect_icon05.png" alt="">

    </nav>

  

    <nav id="sub-menu">

        <img src="images/rect_icon01.png" alt="">

        <img src="images/rect_icon02.png" alt="">

        <img src="images/rect_icon03.png" alt="">

        <img src="images/rect_icon04.png" alt="">

        <img src="images/rect_icon05.png" alt="">

    </nav>

  
  

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

        border: 1px solid black;

        width: 200px; height: 200px;

        background-color: gold;

        margin:100px;

        transition: all 3s;

    }

  

    body:hover #box{

        transform: rotate(45deg);

        /*  변화 중심 축*/

        /*transform-origin: 0px 400px;*/

    }

  

    body{

        padding-bottom: 500px;

    }

  

</style>

</head>

<body>

    <h1>text</h1>

    <div id="box">상자</div>

</body>

</html>
```

## 전환 transition
- 객체의 속성(값)이 변화되는 과정을 시간 순으로 보여주는 기술
- 수치형 속성 값에 한하여 

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

<style>

  

    #box{

        border: 1px solid black;

        width: 200px; height: 200px;

        background-color: gold;

        margin:100px;

    }

  

    body:hover #box{

        /*  변화 중심 축*/

        /*transform-origin: 0px 400px;*/

     /*   width:400px;

        height: 400px;

        font-size: 5rem;

        font-family: '궁서체';*/

        /*opacity: 0;*/

        background-color: whitesmoke;

        border-width: 100px;

        border-radius: 50%;

        margin-left:300px;

        box-shadow: 10px 10px 5px #555;

        transform: rotate(360deg);

    }

  

    body{

        padding-bottom: 500px;

    }

  

/*

  

    전환, transition

    - 객체의 속성(값)이 변화되는 과정을 시간 순으로 보여주는 기술

    - 수치형 속성값에 한해서...

  

*/

#box{

    /*transition-property: width, height, font-size;*/

    transition-property: all;

    transition-duration: 1s;

}

  
  

</style>

</head>

<body>

    <div id="box">상자</div>

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

    body{

        margin: 0;

    }

  

    #menu{

        position:fixed;

        top:0;

        width: 100%;

        height: 120px;

        background-color: #FFF;

        border-bottom: 1px solid #ccc;

        box-shadow: 0px 2px 2px #DDD;

        cursor:pointer;

        transform : translate(0px,-80px);

        transition: all 0.7s;

    }

  

    #menu:hover{

        transform: translate(0px,0px);

    }

  
  

    #menu > span{

        font-weight: bold;

        font-variant: small-caps;

        position: absolute;

        right: 20px;

        bottom: 10px;

    }

  

    section{

        width:800px;

        margin:0 auto;

        margin-top:60px;

    }

</style>

</head>

<body>

    <!-- 상단 붙박이 메뉴 + 슬라이딩 -->

  

    <nav id="menu">

        <span>Menu</span>

    </nav>

  

    <section>

        <h1>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Atque error doloribus laborum accusamus temporibus, nulla quae voluptate quod, ab minima rerum libero nihil amet id ea! Pariatur fugiat ab porro!</h1>

        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus eveniet natus quae repudiandae perferendis error deleniti, corrupti illum! Accusantium, amet. Officiis hic rem numquam cum omnis itaque consequatur aliquam quis.</p>

        <p>Atque quas debitis ad, sed placeat nam qui dolor, eveniet explicabo nemo sint rem repudiandae accusamus? Voluptatum temporibus iste culpa veniam nam ea laudantium quaerat maiores, atque modi, repellat repellendus!</p>

        <p>Id, optio. Amet dicta adipisci dolore. Magnam nobis veritatis ad at voluptates repellat harum est dolor perspiciatis, commodi officiis qui amet labore nihil quasi, temporibus recusandae possimus hic consequuntur omnis?</p>

        <p>Neque quisquam placeat saepe accusamus deleniti nobis in maxime voluptatem omnis, corporis temporibus modi, culpa ut nisi illum repudiandae necessitatibus fugit ipsam eaque? Sed porro dolores, cum dolorem quidem necessitatibus?</p>

        <p>Enim nobis nulla, molestias necessitatibus dolorum quo, ea ex, nihil fugit quisquam esse maiores autem praesentium quibusdam deleniti ratione assumenda eaque. Quibusdam dolorum mollitia alias molestiae excepturi illum, perferendis adipisci.</p>

        <p>Deserunt voluptatum, pariatur inventore minima necessitatibus enim totam labore quaerat, rem laudantium culpa consectetur! Id illo magni, quasi temporibus est sint suscipit doloribus aliquid consectetur quia, voluptatem odit explicabo harum!</p>

        <p>Commodi laborum necessitatibus excepturi porro laboriosam molestias dicta recusandae dolores vel, quidem enim nisi eligendi accusamus dolore alias ipsum. Architecto deleniti porro expedita similique eveniet dolores nobis corporis nihil eligendi!</p>

        <p>Non excepturi nostrum veniam impedit magnam porro eum perferendis dolores. Rerum, omnis voluptatum quam nostrum velit aperiam recusandae. Reiciendis temporibus nisi nesciunt asperiores repellat repudiandae dolorum eum maiores pariatur suscipit.</p>

        <p>Rerum veniam delectus accusantium repudiandae quisquam, minima facilis maxime reprehenderit, temporibus optio, dolor perspiciatis dolorum quas numquam porro eaque. Exercitationem sapiente minima aliquid ut tempore perspiciatis magnam quos excepturi accusamus.</p>

        <p>Dolor voluptatum omnis ab? Temporibus, numquam explicabo commodi ipsam, laudantium maxime earum exercitationem iusto dolorem consequuntur excepturi delectus! Quos deserunt modi suscipit enim id sunt cupiditate eum quam voluptatem ea?</p>

        <p>Iure modi, natus quas reprehenderit vitae error, a optio, nihil saepe dignissimos adipisci ad. Quam tenetur, laborum natus, a aspernatur et ex exercitationem esse nihil voluptatem, blanditiis repellendus ullam quisquam!</p>

        <p>Dolores expedita alias in non, quasi ullam? Earum dolorum deserunt consequatur officia blanditiis suscipit, aliquam dolores commodi cupiditate exercitationem minima veritatis laboriosam. Optio, nam? In quas obcaecati labore odit cum?</p>

        <p>Dolore tenetur minima natus voluptates explicabo. Nisi asperiores error recusandae quod explicabo! Sit fuga eos expedita, dolorum optio architecto facilis repellendus quibusdam totam consequuntur eveniet dolore. Dicta ipsa neque quae.</p>

        <p>Beatae accusamus consequatur explicabo amet totam debitis sapiente, nesciunt omnis reprehenderit ducimus natus illo error porro eum labore hic ullam aperiam maiores quis animi voluptas maxime, necessitatibus molestiae nemo? Possimus.</p>

        <p>Saepe accusamus quod unde perferendis eveniet officiis mollitia pariatur consequuntur fugiat doloremque magnam, neque sit dolor totam quibusdam cupiditate soluta numquam. Id qui nobis, ea repellendus quibusdam laudantium dolores dignissimos.</p>

        <p>Dolor nisi doloribus dolorum fuga accusamus temporibus modi suscipit eum, inventore necessitatibus consequatur assumenda perferendis. Sed fuga commodi ut? Delectus quaerat dolore dignissimos repellat ipsam esse aut, error ut odio.</p>

        <p>Qui, atque delectus architecto cupiditate libero nulla incidunt, et quidem iste pariatur modi doloribus. Labore voluptatum iste itaque numquam obcaecati, odit tempore, totam doloribus sint, quidem officia cupiditate asperiores! Tempore.</p>

        <p>Nesciunt architecto nostrum rerum at culpa assumenda? Incidunt sapiente nobis saepe iusto labore asperiores porro dolore nisi in eos exercitationem nostrum odio tempora expedita cum facere, magni rem suscipit quo.</p>

        <p>Esse facilis corrupti odio, est amet enim illo recusandae eius beatae saepe nobis soluta quos. Necessitatibus distinctio iusto neque non cum? Ad provident, aut ipsum esse eaque numquam facilis eveniet.</p>

        <p>Ipsum esse assumenda, optio ad, nemo, nam quas quia consectetur beatae cum aperiam rem voluptates quae atque sint dignissimos eveniet aliquam debitis. Eligendi accusantium laboriosam pariatur commodi sunt iste deleniti?</p>

        <p>Ullam quaerat quod culpa animi ipsam necessitatibus impedit modi odit qui? Fugiat reiciendis vel nostrum blanditiis eius officia nihil, repudiandae iste animi at voluptates, quam, ducimus odio maxime aliquid mollitia!</p>

        <p>Obcaecati iste aperiam quae eum labore ipsa rem. Sapiente vitae accusantium labore sed nemo molestiae quibusdam hic rem corrupti consequatur pariatur eveniet modi quaerat adipisci iusto quo expedita, soluta officia.</p>

        <p>Ex fuga atque temporibus est quia quam nemo exercitationem, aperiam incidunt at perspiciatis aut? Rerum, a inventore. Aliquam aspernatur dicta perferendis, atque dignissimos soluta sapiente delectus rerum, ipsa facere facilis.</p>

        <p>Ullam neque beatae optio, id iusto, quo quis cumque officiis magnam soluta vitae voluptatem possimus labore sit necessitatibus eveniet nobis dolor placeat, nihil rem eaque! Magnam exercitationem sequi deleniti alias?</p>

        <p>Nesciunt, cum. Officiis architecto quibusdam harum veniam facere, delectus nisi dolore et ipsa eius perferendis vero quos optio ex sit, debitis placeat iste atque ullam repellendus? Necessitatibus libero quia veritatis.</p>

        <p>Voluptatum repellendus nisi debitis harum quod nihil consectetur earum soluta aspernatur reiciendis ipsum doloribus officia consequuntur, saepe eos eveniet illo impedit magnam facilis nobis nostrum adipisci voluptates iste! Obcaecati, minus!</p>

        <p>Similique iste mollitia voluptate odit possimus veritatis cupiditate fugit dicta atque non, inventore eum sit totam quibusdam, nemo veniam eveniet tempore dolore id aut assumenda quasi quidem praesentium. Voluptates, maiores.</p>

        <p>Saepe adipisci tempore fugit? Eveniet error harum voluptas sit quia quo suscipit placeat nostrum laboriosam sint, itaque dolore libero, quae facere doloribus quod expedita maiores, nobis ea voluptates commodi optio?</p>

        <p>Officia vero perferendis, quia nisi adipisci molestias, eveniet earum iste corporis voluptatum atque consectetur praesentium eos autem expedita voluptatibus fugit ab nam ipsa aspernatur vitae. Amet, hic? Eaque, harum nemo!</p>

        <p>Aliquam, voluptatem. Aperiam ex, dolorum velit at voluptatum ea quos quia porro a modi ipsum debitis ipsa, labore consequatur voluptates deleniti, sapiente dignissimos tempora consectetur distinctio vero iusto! Iure, non?</p>

        <p>Reprehenderit doloremque doloribus rerum cupiditate repellendus unde, fugiat amet nemo quis nulla dolore a commodi autem voluptas praesentium nisi quod excepturi ratione magnam aliquam voluptates id. Nam sit modi sint.</p>

        <p>Enim aliquam pariatur saepe reprehenderit suscipit amet cum adipisci necessitatibus assumenda ducimus ut, dolore architecto voluptate? Minima eaque tempore culpa molestiae numquam sit minus vero reiciendis. Reprehenderit beatae sit modi.</p>

        <p>Tempora corporis a sunt repudiandae sed quidem accusantium amet labore expedita. Aperiam facere quaerat aliquid optio praesentium. Aliquid repellat tempore, optio impedit natus assumenda, recusandae corporis molestias neque atque dolorem.</p>

        <p>Esse laborum earum accusamus et atque commodi laboriosam deleniti officia consectetur, aspernatur harum eaque totam dicta ratione non alias ipsam illum perferendis sint molestias! Omnis repudiandae aliquid cupiditate rem dolores!</p>

        <p>Repudiandae nisi quia qui, sit quae eos quisquam dignissimos non saepe quasi quis eum quibusdam voluptatem consequuntur. Deserunt culpa est molestias repellendus officia, perferendis cum libero. Ex vitae earum animi!</p>

        <p>Consequuntur, provident velit? Incidunt maxime ab, in fugit perspiciatis accusamus, illo facere neque reprehenderit ad pariatur molestias eum a atque illum excepturi cum eius. Voluptatum sit earum iusto eos blanditiis!</p>

        <p>Dolore maxime doloremque corrupti rem corporis blanditiis nostrum, eos officia alias facilis iusto sapiente consectetur eaque hic? Architecto, sequi placeat consequatur eligendi nisi magnam asperiores dolore animi, aperiam esse saepe.</p>

        <p>Deleniti, enim voluptate! Temporibus accusamus quaerat voluptate iure reiciendis facere, sapiente beatae labore nesciunt est repellendus dolorem deserunt corrupti nemo in. Impedit fugiat reprehenderit quibusdam odio error placeat consectetur! Quod.</p>

        <p>Quas beatae inventore ipsam consequuntur libero? Minima assumenda, hic quia asperiores, labore et dicta quam repellat, doloremque a possimus maiores necessitatibus architecto aliquam voluptas magnam voluptates illo quae laborum libero!</p>

        <p>Consectetur, aliquid ipsa minus a perferendis eligendi. Voluptate laboriosam amet rem libero, ut accusamus sunt quaerat vero suscipit. Maiores laboriosam molestias et rem, itaque cum quis atque dolorum culpa porro?</p>

        <p>Nostrum aliquid praesentium sunt minima accusantium ex similique hic repellat veritatis tenetur ad mollitia aliquam minus voluptate, illum ea, voluptatum repudiandae provident voluptatem magnam necessitatibus suscipit laborum! Iure, culpa quidem.</p>

        <p>Dolor quasi minus omnis vel amet distinctio accusamus voluptatum. Vero reiciendis facilis blanditiis ullam reprehenderit aliquid quam accusantium sunt tempore, magni repellat id voluptates eos vitae saepe mollitia modi fugit?</p>

        <p>Adipisci inventore distinctio facere dignissimos amet, cum magnam deserunt unde atque. Voluptatum, cumque molestiae earum ratione, sapiente quae iste corporis asperiores mollitia vitae obcaecati sed deserunt ducimus ex iure excepturi!</p>

        <p>Nemo a deleniti facilis veniam, ea magnam consectetur explicabo iusto ex natus, in dolore id neque ab architecto inventore? Quaerat delectus porro dolorum maiores vel expedita explicabo quos ipsum accusantium?</p>

        <p>Beatae quo deserunt ullam facilis nobis! Alias nobis, delectus inventore autem, ullam adipisci nesciunt accusantium eaque harum rerum dolorum dicta officia laborum voluptas error? Fuga eius amet doloribus voluptatibus deleniti.</p>

        <p>Maiores optio ea tempora sequi, voluptate veniam recusandae corporis facere nihil est debitis tempore deleniti, animi voluptatum culpa, quia eum odit? Repellendus, iste unde esse voluptas laborum placeat inventore doloribus.</p>

        <p>Eveniet quasi optio facere doloribus praesentium quo, alias, delectus in consequatur adipisci saepe aperiam. Quidem recusandae natus incidunt quod tenetur fuga rerum. Numquam, eveniet similique? Ipsam, delectus porro. Dolores, modi!</p>

        <p>Ipsam iusto commodi fugiat necessitatibus atque praesentium cumque minima enim, officia maxime voluptatibus vitae amet dolore dolorem. Possimus dolore ducimus perferendis voluptate architecto laboriosam odit dolor quia aliquid. Esse, nulla!</p>

        <p>Necessitatibus porro eum corrupti tempora totam qui, quisquam vero soluta veritatis, quia, ipsum dolorem ducimus nam pariatur dignissimos? Molestias ipsam, mollitia maiores modi est illum placeat nam ea dolore voluptates.</p>

        <p>Ea labore cum perferendis, veritatis omnis ipsum tempore corrupti impedit, voluptates beatae repellendus deserunt minus blanditiis similique rem, distinctio repudiandae porro officia quasi molestias quo corporis maiores! Labore, error. A?</p>

        <p>Totam dolores vero architecto voluptas quaerat adipisci aliquam aut maiores, id recusandae, repellendus ipsum nisi omnis maxime. Repellendus distinctio, delectus consequuntur perferendis iste similique nobis ipsa architecto perspiciatis, obcaecati iure.</p>

        <p>Praesentium sint quo dignissimos architecto. Sint debitis laudantium, ipsum autem velit illo modi repellat iste quisquam ex voluptatum sequi ratione, voluptatem excepturi perferendis suscipit, dolorum id repellendus deserunt amet nostrum!</p>

        <p>Reprehenderit voluptatem cum ipsam vel est aperiam illum molestiae laboriosam eligendi cupiditate magni aliquid voluptatibus, illo impedit laborum, eaque blanditiis reiciendis enim esse deleniti laudantium cumque at? Nemo, dolorum natus!</p>

        <p>Nam iusto rerum, porro sint commodi, officiis, ipsa suscipit voluptas magni veniam non eveniet id repudiandae quaerat! Quia eos similique quam, nisi vero in voluptatem facilis illo vitae minima dolor?</p>

        <p>Recusandae sit eveniet earum quaerat vitae quidem tempora quia ratione quas? In, expedita mollitia tempore, veritatis illum soluta quisquam odio, temporibus accusamus dolorum adipisci dicta neque suscipit commodi quae corporis!</p>

        <p>Rem voluptatum eos voluptas. Sapiente soluta maxime, excepturi magnam assumenda consequatur odio ipsa accusantium esse ducimus enim quam vero nam molestiae natus at distinctio, quis ab quos. Dolor, atque fugit?</p>

        <p>Minima perferendis tenetur excepturi facilis eligendi natus autem laboriosam pariatur eum aperiam officiis consequatur, quia ab sed obcaecati dicta itaque enim inventore molestias? Obcaecati explicabo quis velit vel quos deleniti?</p>

        <p>Odio officia eum adipisci a accusantium autem accusamus ullam maiores sequi ex, natus consequatur quis illum quod est dignissimos saepe aliquam perferendis mollitia id? Tempore dolorem odio accusamus iusto dignissimos.</p>

        <p>Nulla ipsa in numquam tempore quos sapiente, incidunt deleniti iure illo. Reiciendis dignissimos eaque quasi, aut quod pariatur provident placeat possimus optio hic minima architecto at, aliquam fugiat eius soluta.</p>

        <p>Atque sunt excepturi, totam nisi, doloribus est mollitia voluptas odio doloremque possimus repellat officia quo accusantium enim corporis eligendi saepe. Aliquam recusandae blanditiis magnam accusantium nobis, deserunt voluptatibus tempora a!</p>

        <p>Consequatur, odit! Harum laudantium quae asperiores sapiente minus enim possimus impedit eius quam dicta repellendus expedita, placeat doloremque corrupti maxime alias molestiae assumenda excepturi ipsam fugiat vel dignissimos esse nisi!</p>

        <p>Enim nesciunt repellat dolor libero et ea nobis accusamus beatae commodi perspiciatis at eos culpa nulla, laborum ullam obcaecati blanditiis nemo deleniti quidem. Nesciunt neque, commodi debitis qui dolore necessitatibus.</p>

        <p>Consequatur temporibus cumque, incidunt libero, ipsum, nesciunt voluptate quam beatae id fugit magni eos labore maxime natus? Assumenda voluptatum voluptate consequatur eius, alias obcaecati expedita veniam enim laudantium id repellendus.</p>

        <p>Placeat, voluptatum ducimus! Dolor accusamus architecto corporis expedita commodi impedit error aspernatur optio facilis maxime ipsum, minima ipsa similique ex dolores hic aut, ratione magnam esse cumque distinctio iusto molestiae!</p>

        <p>Explicabo odio a eveniet vitae hic sed tenetur, possimus natus, ipsum soluta iste doloremque accusamus at aperiam voluptas fuga rerum quisquam inventore quasi, quam ea corporis aut amet? Neque, aliquam?</p>

        <p>Esse aperiam facilis odio assumenda tempora ipsam ut consequatur. Eligendi suscipit cupiditate delectus veniam, sint illo temporibus! Molestiae, voluptatem consequuntur! Nemo, voluptatem similique nobis iste temporibus ea quis labore quas.</p>

        <p>Vitae incidunt sunt natus est dolore dicta? Quam perspiciatis natus tempore illum earum, minima distinctio incidunt veritatis nam ad nobis ipsa quos pariatur modi, tenetur, aut dolor dolorem. Non, quae.</p>

        <p>Officia, architecto est culpa provident blanditiis excepturi, reiciendis accusantium praesentium temporibus fuga assumenda aut sint animi soluta molestias rem enim? Reprehenderit a excepturi quisquam incidunt. Quas officia accusamus rerum in.</p>

        <p>Labore asperiores animi laudantium omnis mollitia numquam consectetur molestias velit eius blanditiis veritatis nostrum, quisquam cupiditate quaerat sequi voluptates consequuntur rem laborum. Cupiditate nihil iste quisquam deserunt. Atque, optio enim.</p>

        <p>Laudantium cum deleniti error facilis totam, similique officiis. Laboriosam praesentium similique aperiam tempora eius magnam, at rem consequuntur a assumenda corporis consequatur, asperiores error sapiente quis voluptatibus illo laborum repudiandae.</p>

        <p>Excepturi incidunt quisquam eum, hic adipisci assumenda laboriosam suscipit eius perferendis in veniam? Minus itaque veniam distinctio. Non magnam veniam expedita odio a, iste deserunt quisquam, ducimus qui minima cupiditate.</p>

        <p>Nesciunt accusamus distinctio officiis doloremque praesentium dolores optio reiciendis quam perferendis pariatur? Atque, facilis a fugit ratione suscipit, voluptatibus dignissimos impedit voluptates dolores, obcaecati eius error eaque? Ipsa, veniam beatae.</p>

        <p>Laboriosam, velit excepturi consequatur sequi amet dolor ratione, eaque dolores laudantium eligendi quibusdam aperiam officiis ex! Aspernatur, excepturi? Veritatis, optio impedit. Voluptatibus possimus culpa reiciendis quasi nobis suscipit asperiores dignissimos.</p>

        <p>Voluptates, natus aut quisquam at consequatur quos consequuntur similique molestias modi nemo quae voluptatem maiores illo error recusandae corporis distinctio placeat. Maiores assumenda laborum architecto, eos blanditiis maxime! Soluta, aliquid.</p>

        <p>Assumenda ea nam minus obcaecati voluptatibus odio voluptates quidem illo dolorum aspernatur alias commodi ipsa accusamus dicta, nulla iste doloribus ratione itaque vel et error officiis eveniet? Odit, excepturi facere!</p>

        <p>Sequi praesentium provident culpa, sunt itaque vel quasi dicta magni ex eligendi nemo porro quae totam. Est voluptate similique odio doloremque, id sequi, officia neque repellendus possimus perspiciatis quidem voluptatum?</p>

        <p>Pariatur incidunt voluptatum deserunt in veniam commodi voluptate repellat reprehenderit iure obcaecati distinctio expedita alias quo, velit impedit tenetur inventore mollitia ipsum dolore! Quas itaque, excepturi odio dolorem sit quae.</p>

        <p>Repudiandae, tempora animi voluptate quidem libero consectetur tenetur. In atque repellendus amet quas, ea dignissimos recusandae sapiente cumque neque voluptatibus, ullam natus, et saepe repellat quibusdam laboriosam reiciendis nemo molestiae.</p>

        <p>Praesentium in placeat assumenda, iure aperiam repellat mollitia! Nostrum similique nulla ducimus deserunt amet beatae, sint tenetur ad praesentium ut laboriosam impedit commodi exercitationem! Id praesentium veritatis ipsum perspiciatis facilis!</p>

        <p>Sed tempora error illum voluptates impedit consectetur quod non odio, autem numquam ipsa pariatur repudiandae ullam maiores magni perferendis exercitationem recusandae vitae! Laboriosam hic vero suscipit? Nobis mollitia maxime asperiores?</p>

        <p>Voluptas magnam, deserunt nulla ut, suscipit nesciunt, exercitationem a culpa dolores aut odit praesentium saepe sunt quisquam nisi. Molestiae veritatis tenetur vero consequatur corporis dolore fugit dolor ullam ad quia.</p>

        <p>Quas consequuntur sed ea veniam voluptas consectetur nesciunt saepe ipsum cumque doloremque delectus inventore nostrum maxime quibusdam soluta, rem, ratione assumenda vitae numquam fugit excepturi? Dicta consequuntur deserunt adipisci at?</p>

        <p>Doloribus, consequuntur dignissimos eligendi sed maxime, eaque amet reiciendis voluptas voluptatum omnis quasi! Iste cupiditate tenetur itaque repellendus? Reiciendis facilis voluptas velit repellendus architecto unde, error soluta dicta. Asperiores, minus.</p>

        <p>Quia deleniti iste architecto fugit facilis exercitationem, quis numquam officiis repellat, officia expedita veritatis quisquam, odio laborum dolore molestiae aliquam soluta assumenda. Ipsa accusantium dolor assumenda magnam repellat, sequi nihil?</p>

        <p>Officiis quisquam consequatur asperiores esse, cumque earum similique provident iusto suscipit! Fugit facere porro, ipsa molestias dolorem illo nostrum rerum dolorum excepturi magnam, iusto ab! Doloribus quam exercitationem distinctio commodi!</p>

        <p>Consectetur suscipit doloribus ut illo officiis temporibus vel soluta. Est maiores sunt in quod molestiae nesciunt quidem, aut esse magni assumenda, accusamus veritatis blanditiis sed. Dignissimos repellat vitae fugiat architecto.</p>

        <p>Molestiae velit iste placeat dolores dolorem, magnam itaque maiores laudantium ipsa? Sed, quaerat. Nisi aperiam aliquid maiores eveniet minus ab. Cumque consequatur iusto laboriosam praesentium assumenda sequi doloribus aliquid hic!</p>

        <p>Quis error, fugiat blanditiis aspernatur possimus pariatur tempore ab, odio eaque magnam maiores nulla. Quod rerum fugit sint deserunt soluta officiis voluptatem commodi porro praesentium itaque! Libero veniam esse expedita.</p>

        <p>Omnis, enim! Inventore similique iusto accusamus aliquam! Sequi earum, cupiditate iste alias laboriosam tempore eveniet repellat nobis minus? Perferendis provident sed dolores suscipit delectus distinctio placeat eum aspernatur tempore nulla.</p>

        <p>Animi quia sint laboriosam ab quo sunt distinctio a hic autem atque odio laudantium molestias quaerat placeat repellat ipsa necessitatibus sequi impedit quisquam magni, earum fugit repellendus suscipit exercitationem. Ipsa.</p>

        <p>A deleniti omnis nesciunt expedita? Doloremque repellendus maxime assumenda molestiae pariatur esse ipsum culpa harum nostrum odit natus vitae provident asperiores blanditiis quos ducimus veritatis, repellat suscipit atque, nobis reiciendis.</p>

        <p>Saepe eaque sunt illum, sed amet esse nulla assumenda voluptates velit odit obcaecati aliquid asperiores dolorum, necessitatibus ex minus possimus delectus quis facilis in autem voluptas! Sit voluptatum minus mollitia!</p>

        <p>Delectus, asperiores unde? Reiciendis nihil aliquam maiores natus deleniti illum enim voluptatum, porro exercitationem? Id alias praesentium dolor. Pariatur numquam molestiae ipsam corrupti. Vel excepturi quae autem. Iste, quae nam?</p>

        <p>Provident veniam laudantium at, minus magni dicta, sunt neque facilis voluptatum eveniet vel, doloribus ducimus fugit excepturi debitis. Omnis atque est mollitia ullam cum corrupti. Laboriosam earum nam tenetur illum?</p>

        <p>Voluptatem labore accusamus sunt adipisci neque aliquid alias atque sequi corrupti qui laudantium praesentium unde culpa magni, explicabo consectetur quisquam impedit quae beatae est. Tempore, vel nam? Enim, veniam placeat.</p>

        <p>Illum praesentium saepe expedita nemo, non dolor assumenda veritatis vel, unde iure ratione nam! Animi autem ipsa, mollitia eius numquam nobis quasi in, impedit nemo maiores eveniet id sapiente iste.</p>

        <p>Natus fugit illum enim autem incidunt ipsam quod ab voluptatum quidem corporis. Dolorum nobis velit tempore cupiditate ipsum, tempora, illum exercitationem aspernatur obcaecati quaerat iure similique ducimus aperiam eligendi necessitatibus.</p>

        <p>Veniam saepe cumque ducimus dicta quis iusto, doloremque sed. Dignissimos, asperiores. Minima consequatur repellat temporibus hic dicta similique excepturi id esse provident, aperiam laboriosam! Quam expedita beatae at. Minima, velit?</p>

        <p>Tenetur nihil maiores, aut laborum sequi hic et in adipisci sit eius. A in perspiciatis rem pariatur porro temporibus? Magni voluptate ducimus cum voluptas minus, perspiciatis mollitia dolorum ad sunt.</p>

        <p>Itaque reiciendis esse dignissimos reprehenderit nam aperiam libero. Optio similique fuga qui ipsum accusantium autem eius dolor saepe quas in voluptate molestiae, at obcaecati deleniti quidem hic nihil sunt quia!</p>

        <p>Ipsa, repellat animi dicta vel quam, non aliquam iure earum nemo soluta excepturi maiores ea itaque laboriosam eos temporibus iste. Officiis soluta, accusamus modi blanditiis itaque provident id explicabo fugit.</p>

        <p>Explicabo vel dolor neque dolorum delectus repellendus eius? Sapiente aliquam molestias aspernatur voluptatum in culpa iusto repudiandae? Cupiditate mollitia nobis voluptatum porro, laborum, alias molestiae et tenetur odio id consequatur.</p>

        <p>Earum officiis unde obcaecati, accusamus ea libero perspiciatis provident ducimus eligendi necessitatibus sunt, voluptatibus est quam fugiat inventore illo modi aliquid omnis iusto? Dolore explicabo fuga culpa id accusamus deserunt!</p>

        <p>Maxime asperiores nam, illo officiis velit facere voluptatum nesciunt? Similique debitis, nobis dignissimos nihil cumque esse quibusdam perferendis aliquam quasi ullam aspernatur nesciunt facere ut odit ex odio illo iste?</p>

        <p>Quas voluptatem laboriosam officiis accusantium recusandae earum ullam, fuga iusto soluta? Eum eos illo dolores alias repudiandae, maxime magnam in recusandae eligendi, atque debitis veritatis ducimus culpa aspernatur eveniet. Cupiditate!</p>

        <p>Debitis, at dolore nostrum veritatis sapiente magnam quidem libero repellendus. Totam dicta, eius quo neque aspernatur repellat iure esse ullam quod porro eos corrupti voluptatum laudantium aut suscipit? At, iste.</p>

        <p>Esse perferendis modi dicta minima facere sapiente perspiciatis. Maiores laudantium minus quidem ullam, accusantium blanditiis fugit, quo expedita dolore quia repellat eius nihil earum accusamus dolores praesentium. Distinctio, architecto nobis.</p>

        <p>Impedit magni eius officiis suscipit asperiores quaerat atque sunt quibusdam inventore aliquid eos optio cum nesciunt nostrum doloremque accusamus id, sequi quas amet vel in vero dolor ratione nisi! Totam.</p>

        <p>Distinctio expedita qui cum recusandae atque veniam fugiat minus quos modi accusamus deserunt, vitae dolores totam quidem explicabo quis ipsam corrupti! Eum eius veniam quod accusamus, nostrum dolorem eveniet doloremque.</p>

        <p>Sint aspernatur, laborum, fugit dignissimos delectus molestiae deleniti nesciunt libero ipsa provident asperiores. Id quasi enim in porro ullam doloremque quas, similique accusamus quo ad architecto cumque officiis! Odio, nam.</p>

        <p>Nemo fuga molestias eligendi corrupti harum ab voluptatem assumenda atque sapiente in eius nisi possimus nihil omnis enim illum, veniam sequi dolores iure consequatur, qui ratione earum beatae autem? Voluptatem.</p>

        <p>Cumque incidunt ad mollitia id maxime? Repellat ad tempore reprehenderit sunt neque debitis non cum ullam. Facere aspernatur dignissimos optio ullam recusandae, temporibus deleniti veniam ipsam praesentium, amet mollitia. Reprehenderit.</p>

        <p>In mollitia modi minus suscipit dolorum enim, quisquam quam ullam veritatis libero quas dolore magni distinctio rerum doloribus ab facere ad illum eius temporibus ipsa maxime. Sapiente tempora deleniti reiciendis?</p>

        <p>Officia, reprehenderit obcaecati inventore amet quasi corrupti quam enim molestias neque voluptatem. Exercitationem quaerat expedita quos molestias, ut, inventore alias voluptates neque ducimus veritatis recusandae dolor amet nihil quod eum.</p>

        <p>Odit, distinctio praesentium omnis explicabo necessitatibus alias sint. Nesciunt, quasi vero quaerat quod eos repellendus commodi itaque quae ipsam sunt omnis repudiandae sapiente, qui illo adipisci, cumque nemo accusamus minima?</p>

        <p>Iste, explicabo alias rerum quidem non commodi repellendus laboriosam quam illo. Obcaecati voluptatum id dolore! Excepturi beatae dolorum illum quibusdam. Rem animi, tempore magni libero dolor provident ratione sit et?</p>

        <p>Rerum placeat architecto eligendi harum ut suscipit rem magnam illum, atque dolore vitae similique facere, dolor animi explicabo recusandae nostrum. Doloremque accusamus delectus nisi enim vitae odit soluta iste quia.</p>

        <p>Delectus cupiditate sapiente nam fugiat suscipit. Adipisci numquam fugiat expedita illum. Tempore, quis veniam hic officia asperiores dolores dolorum, sapiente sint in voluptatem nulla temporibus, cumque rem esse facilis rerum.</p>

        <p>Fugit unde labore debitis, placeat possimus vel nostrum saepe obcaecati nihil. Corporis id error quaerat in repellendus. Ratione libero, molestiae omnis neque dicta beatae labore quidem id hic reiciendis voluptatem?</p>

        <p>Repellat vitae nisi, sunt ipsa nam repudiandae qui voluptate, debitis fuga delectus modi dolor unde? Labore animi cumque magni! Sequi dicta nobis odio dolore aliquam eveniet reprehenderit aut, nisi excepturi!</p>

        <p>Harum, illo excepturi sunt voluptatem sit repudiandae natus ullam provident expedita quam a suscipit ipsa eveniet inventore odio nam minima velit laudantium magnam modi! Voluptatem, nisi tempora? Quasi, vitae accusamus!</p>

        <p>Ullam rerum reprehenderit beatae repellat fugiat mollitia doloremque corporis, voluptas, et quas ipsam sit molestias culpa illo dolorum alias? Iste similique nulla deleniti tempore eligendi sunt commodi libero voluptate autem.</p>

        <p>Saepe voluptate consequatur atque sequi officia! Aliquid similique facere sint ad modi quibusdam molestias distinctio dolorum, placeat facilis est aliquam enim atque obcaecati saepe iure tempore. Omnis itaque culpa beatae?</p>

        <p>Ratione molestiae libero sunt veritatis voluptatibus reiciendis quod, tempora, cumque corrupti sed eaque alias iusto maxime eius cum repellat dignissimos doloribus nulla aliquam asperiores magnam culpa illo! Itaque, sapiente illo!</p>

        <p>Omnis minima a architecto ratione blanditiis beatae unde cupiditate, quia accusamus eum, officiis laborum, quis dolores eius dolor soluta. Voluptates iusto hic aliquam quidem officia sed magnam explicabo accusamus suscipit!</p>

        <p>Fuga deserunt quo tempora sit commodi iste quae nisi. Veniam eligendi nulla consectetur eum iusto vitae odit molestiae saepe ab molestias non laboriosam tempora deserunt similique, maiores in. Inventore, dolorum!</p>

        <p>Omnis excepturi, tempore hic modi id vitae labore exercitationem quia officiis doloribus quod sunt soluta odit, ducimus accusantium dolor natus reiciendis veniam, maiores dolorem adipisci provident a! Accusamus, libero maiores.</p>

        <p>Ex vero accusamus totam itaque consectetur praesentium ullam incidunt quis illo dolorem velit neque impedit, beatae ab, aperiam necessitatibus cumque veritatis laboriosam unde. Recusandae illo, iusto dolor fuga porro praesentium?</p>

        <p>Officia, eius soluta. Quos adipisci quas praesentium eaque aperiam rem dolor voluptatem optio temporibus ipsa natus laboriosam nemo provident veritatis magni at corrupti quod nihil, sapiente incidunt esse veniam quam.</p>

        <p>Nihil quas, tempora nam aliquam dolore, eos beatae voluptate quisquam deserunt minima dolorum earum vero debitis ipsum sunt qui ducimus unde. Beatae expedita, ea labore alias magnam eligendi eaque eveniet.</p>

        <p>Vel nostrum odit neque quod tenetur. Voluptate error aspernatur, quibusdam odio nesciunt suscipit numquam quisquam beatae ducimus quos, qui ullam voluptatum iste illum a cumque. Explicabo libero tempore quisquam distinctio!</p>

        <p>Perferendis sit expedita dolores! Quae temporibus culpa fuga tenetur deleniti reiciendis veniam accusamus fugit perspiciatis cupiditate. Temporibus vero harum odio recusandae. Dignissimos facere hic sint autem aliquid totam fugit provident.</p>

        <p>Quo non accusantium cupiditate quam hic! Repellendus, voluptatibus. Odit quas iusto praesentium nisi facilis explicabo reprehenderit cupiditate repudiandae animi voluptates error quibusdam ipsam obcaecati aliquam ullam neque, inventore dignissimos. Inventore.</p>

        <p>Obcaecati voluptas impedit sunt dolor aspernatur nam quos enim, non error dignissimos reiciendis iste, illo nihil dicta soluta architecto cupiditate officia nostrum neque sint sit, distinctio culpa? Pariatur, ullam adipisci.</p>

        <p>Repellendus odit autem non nobis veritatis voluptatibus hic delectus ut eaque aperiam. Assumenda placeat dolores, aspernatur quasi dolorum vel ad modi tenetur incidunt magnam quisquam libero fugiat aperiam et ab.</p>

        <p>Dolorum quidem incidunt illum aliquam sint porro, provident repellat expedita placeat aperiam nesciunt illo optio cupiditate. Aperiam libero ea iure asperiores, minima laudantium fugiat sapiente, voluptatum unde impedit odio cupiditate.</p>

        <p>Ullam ratione, error, tempore modi impedit vitae nobis deleniti quibusdam repudiandae aliquid similique rem sit suscipit voluptatum aliquam? Doloremque reiciendis beatae repudiandae. Sunt quod blanditiis natus qui nisi. Itaque, delectus!</p>

        <p>Labore commodi vitae corrupti accusantium voluptatem totam veniam voluptatum repudiandae ea nam reprehenderit, qui, distinctio iusto sequi est dignissimos et molestiae, dolorem repellat? Et, sint qui aspernatur non nostrum hic.</p>

        <p>Fugiat architecto quam, repellat, rem nostrum excepturi animi cupiditate repudiandae doloremque nisi rerum optio voluptas distinctio possimus accusantium eum obcaecati? Accusantium blanditiis eveniet magni autem voluptates et ad dolorem est.</p>

        <p>Similique necessitatibus saepe ex eius repellat natus laborum quas facilis inventore voluptas repudiandae sequi ullam omnis, magnam nulla minima, velit debitis autem sapiente repellendus. Quae accusantium ut dolorem maxime laudantium?</p>

        <p>Sed omnis iusto corrupti voluptatum. Hic, debitis perferendis tempora incidunt adipisci nulla iste ut ipsum culpa. Assumenda quibusdam delectus quod amet dolor. A aperiam dignissimos provident assumenda laborum reiciendis tempore.</p>

        <p>Fugiat eius maiores excepturi maxime amet qui, id aperiam sit eveniet reprehenderit non nulla quisquam, quia autem? Architecto corporis pariatur error reiciendis esse, corrupti ut, atque officia dignissimos earum soluta?</p>

        <p>Repellendus fugit at dolores sint odio eligendi rerum aliquam quisquam neque atque sequi ratione voluptatibus, vel impedit iste, provident asperiores voluptates nulla accusamus! Voluptates deserunt recusandae inventore optio, illum voluptatum.</p>

        <p>Minima, dolores! Quisquam aliquid autem similique unde delectus alias voluptatum placeat quae. Quibusdam dolores quod tempore. Dolor error, architecto facere excepturi ratione necessitatibus expedita sit a perspiciatis, soluta, sint repellat.</p>

        <p>Facere reiciendis dolorum alias atque necessitatibus labore laborum, ex quos magnam distinctio omnis dolorem placeat accusantium quae, possimus quasi aspernatur ut dolore maiores quaerat nobis consequuntur nulla eius aperiam? Quas.</p>

        <p>Magnam recusandae vitae ipsa adipisci optio autem nobis quaerat eaque, exercitationem, eveniet, dicta incidunt. Dolor, illo omnis. Autem, eveniet laborum. Omnis et vero rerum dolorum quam eligendi eos voluptatibus nam?</p>

        <p>Quo deleniti praesentium voluptatum in! Nemo eligendi dolorum, at amet odit inventore reiciendis minus. Aspernatur adipisci perspiciatis voluptatibus, eveniet libero nesciunt alias corporis odio nulla! Adipisci nemo cumque qui consectetur?</p>

        <p>Libero voluptas voluptates impedit cumque maxime est nesciunt, excepturi dignissimos. Assumenda est odit similique iusto, numquam molestias expedita neque cupiditate earum natus totam cum exercitationem facilis beatae corporis? Dicta, quod!</p>

        <p>Assumenda consequuntur aliquam nisi quae veniam ducimus! Atque laborum quod temporibus nam, nesciunt earum quam odio vitae. Dolorem ratione esse nihil eveniet, consequuntur sapiente, similique doloribus voluptatem neque nesciunt suscipit!</p>

        <p>Alias qui molestias vitae consequuntur et perferendis. Minima reprehenderit amet cupiditate aut magni hic nulla quaerat fugit eum distinctio consequatur ratione facilis sunt nobis officiis expedita, est culpa quae officia.</p>

        <p>Exercitationem laudantium debitis non laboriosam fuga expedita vel eveniet odio tempore quibusdam dolores tempora rerum ratione porro, facere dignissimos accusantium alias itaque? Iste, corrupti rerum amet necessitatibus fugiat facilis dignissimos.</p>

        <p>Id voluptatum quibusdam, assumenda aperiam doloremque ipsam odit unde at nesciunt, repellendus iure voluptatem voluptatibus fugit debitis ab mollitia? Error iure eveniet eius odio aspernatur quo ipsa quibusdam quis provident.</p>

        <p>Quia aspernatur, neque, doloremque consequuntur accusamus voluptatem voluptates maiores delectus, laboriosam laudantium porro nulla unde tempora exercitationem eum voluptate totam autem quo fugit. Tempore, totam accusamus? Soluta hic molestias eaque!</p>

        <p>Placeat dolor fugit illum quisquam quibusdam optio dolorum deserunt inventore! Laboriosam, cumque accusantium? Aut, et? Autem dolor porro rem, alias labore quod architecto incidunt, tenetur cum fugit numquam quam quas.</p>

        <p>Beatae expedita perferendis temporibus mollitia ex aperiam exercitationem quasi eum obcaecati quis dolor, quas cumque facere natus. Suscipit illum necessitatibus recusandae neque, velit id in, iste dicta, eligendi corporis aliquam!</p>

        <p>Odit unde quaerat nihil est omnis nisi dolor sequi quisquam labore exercitationem. Cum corporis ipsum maxime tempore laudantium quam, minima numquam libero ipsa porro odit nisi, nostrum magnam. Dolor, vero?</p>

        <p>Minima fugit officia tempore laudantium consequuntur in eius libero totam obcaecati saepe voluptates nihil inventore enim cum, commodi autem mollitia nisi temporibus sit ex! Quidem commodi repudiandae inventore accusamus tempore.</p>

        <p>Libero odit quasi, molestias aliquam dolor quod necessitatibus, hic distinctio dignissimos quidem quaerat vero laboriosam dolore aliquid ut, numquam nemo laudantium amet quas adipisci doloribus rerum. Alias facilis inventore et!</p>

        <p>Adipisci, assumenda? Cum, quisquam maiores vitae est cupiditate quis perspiciatis non nobis laborum culpa excepturi nulla, rem aspernatur id laudantium. Non minima reprehenderit nesciunt explicabo sequi veritatis doloribus doloremque corrupti!</p>

        <p>Labore rem illo neque libero, delectus illum dolore quidem quos eum provident magni repellendus impedit deleniti autem at voluptate esse quia, asperiores eius id corrupti numquam, harum et culpa! Eos?</p>

        <p>Delectus laboriosam esse velit magni unde enim at, tempora iure blanditiis sed, eum consectetur! Mollitia dicta obcaecati ab rem voluptatum animi nam error cumque quisquam, nobis modi aliquid dolore ratione.</p>

        <p>Iste, nemo! Incidunt perspiciatis facere dicta nostrum optio dolor, consequatur, voluptas velit sapiente ad saepe? Suscipit tempora sint, saepe voluptates, adipisci exercitationem veniam eveniet illo ex facere deleniti eum velit!</p>

        <p>Provident aliquam optio doloremque ipsa, vero quam aliquid? Impedit eos corporis culpa labore praesentium. Ipsa consectetur modi quas repellat voluptatem, dolorem deserunt laborum? Excepturi officia beatae dolores facilis tempore vel?</p>

        <p>Omnis, esse alias harum architecto consectetur temporibus facere tenetur, minus quos numquam, earum est officiis voluptas corporis dolorum a excepturi accusamus vero ab maxime? Quae architecto error numquam aliquam in.</p>

        <p>Corporis distinctio, aliquam est odit repellendus similique numquam quas incidunt explicabo optio enim dolorum pariatur dignissimos ipsam necessitatibus, voluptas veritatis veniam perspiciatis, in minus. Unde sunt eius numquam deserunt repellat?</p>

        <p>Omnis ex praesentium possimus impedit debitis enim pariatur, veniam suscipit voluptas aliquid mollitia id, nostrum quia rem esse, distinctio libero officiis dolor fuga a assumenda labore tenetur eaque amet. Magnam!</p>

        <p>Veniam id consequatur aut nemo odio adipisci omnis quod delectus, sint illo, possimus eligendi ex unde sit iste neque! At porro aperiam officia excepturi. Quod recusandae non aspernatur alias veritatis!</p>

        <p>A, magni consectetur dolorem recusandae harum repudiandae quis optio dicta velit neque autem placeat maiores nihil mollitia nulla officiis, iure eaque odio adipisci libero? Animi nemo obcaecati sunt sit quas.</p>

        <p>Accusantium impedit eos cum. Veritatis expedita provident magnam corrupti delectus quae recusandae, eius maiores dolor dolorem libero exercitationem neque beatae pariatur dolores nemo repellendus assumenda esse doloribus, cumque fugit porro!</p>

        <p>Ducimus, eos. Repellat iure dolor porro tempore esse sint earum vel magnam quae possimus illo quas iusto aspernatur placeat voluptatum consectetur nobis doloribus odit repellendus nihil maxime, inventore saepe totam.</p>

        <p>Voluptates ab dolores, laboriosam modi sint, nobis doloribus dignissimos mollitia quis beatae ea quos fugiat incidunt est nesciunt iusto autem quaerat et impedit dicta consectetur! Illum consequuntur temporibus dolorum eaque!</p>

        <p>Earum sequi consequatur ipsa dolorem hic fugiat. Harum possimus porro eum repellendus inventore quam, nemo voluptatum laudantium aliquam at vel, id dolorum illo neque sint quae minus totam mollitia. Dolore!</p>

        <p>Obcaecati ipsam voluptatibus dolore minus quod non ducimus quasi veniam iusto nesciunt earum, dolorem quisquam doloremque aliquam laboriosam magni deleniti, numquam odit corrupti sint consectetur repudiandae totam distinctio suscipit. Soluta.</p>

        <p>Dolorem fuga sapiente illo ex dolores sequi qui! Adipisci cum ullam autem inventore eius unde, excepturi itaque vero perferendis nesciunt earum soluta numquam modi non, natus molestiae delectus. Maiores, eius.</p>

        <p>Debitis explicabo ducimus ullam adipisci numquam. Cum at voluptatum dolorem sit culpa libero veniam, soluta, distinctio voluptatem, ducimus repudiandae! Obcaecati voluptas, harum neque vitae possimus maxime eum facilis labore ad.</p>

        <p>Earum, et. Eum tenetur quo possimus assumenda quam eius beatae vitae doloribus, soluta obcaecati laudantium, laborum provident placeat dolorum ducimus deserunt, doloremque similique quod? Illum aperiam rerum nulla officia ratione.</p>

        <p>Quae eligendi odio pariatur provident, rerum eos dignissimos ipsa, sapiente culpa assumenda ipsum dicta nobis vero? Quod earum, dolore incidunt impedit est sed officia tempore adipisci voluptas, in beatae cupiditate.</p>

        <p>Consequatur quidem tempore sunt laboriosam obcaecati, voluptatem in minima! Nam et animi nisi totam ut excepturi beatae adipisci amet, reiciendis quas voluptates, molestias asperiores eum dolorum, at exercitationem reprehenderit ratione?</p>

        <p>Tenetur, temporibus dolorem quaerat eum blanditiis fugit doloremque reiciendis beatae alias aperiam molestias sequi laboriosam enim. Laboriosam illo fugiat, ad repellendus tempora voluptatibus amet dolores sapiente ipsa nulla quae facere!</p>

        <p>Modi quisquam fugit culpa dolore adipisci, non aspernatur quo doloribus, praesentium tenetur illum alias mollitia. Sint tempore molestiae vitae, quia nostrum consequatur est dolorem, delectus quo alias quis ratione repellendus.</p>

        <p>Optio fuga totam quo incidunt perspiciatis consequuntur praesentium sapiente eligendi corrupti error. Recusandae, magni tenetur explicabo mollitia totam alias obcaecati similique reiciendis iste aperiam minus aspernatur, sunt beatae pariatur debitis.</p>

        <p>Quis ipsum quidem repellendus nesciunt minus quasi id pariatur voluptatibus quo facilis quia architecto molestias culpa beatae atque recusandae eligendi officia quod corrupti nihil voluptates illum, repudiandae doloremque. Eveniet, assumenda.</p>

        <p>Eveniet est magnam quos reprehenderit dolores, beatae omnis alias delectus nemo modi rem eos placeat sapiente maiores ducimus quibusdam repellat, totam nisi quod dolor sint, vero optio fugiat suscipit? Mollitia.</p>

        <p>Molestias, labore. Iste deleniti suscipit autem! Excepturi assumenda cum magnam corrupti, beatae provident rem quia omnis voluptates laudantium dolor consectetur, voluptatibus quasi culpa eveniet minima sint tenetur atque. Labore, illum.</p>

        <p>Autem culpa quia ad praesentium voluptatibus vel in. Dolore, obcaecati rem. Ducimus temporibus deserunt ipsa, magnam, nemo voluptate, perferendis quibusdam labore dolorem veniam atque quis explicabo beatae architecto? Minus, debitis.</p>

        <p>Cupiditate maiores quae aliquid nulla voluptatum, totam excepturi porro hic voluptates similique. Quisquam cupiditate, sint asperiores quod minima perferendis dolor, vero consectetur nisi voluptatibus nihil, similique reprehenderit impedit velit delectus!</p>

        <p>Tenetur sequi voluptatibus quod doloremque quasi. Dolor veritatis ex ut, nemo sapiente eligendi non esse nam saepe nihil quibusdam quasi minima nesciunt? Vitae impedit sit, eum sed doloremque ipsum saepe!</p>

        <p>Aspernatur perferendis incidunt reiciendis totam corrupti quasi id similique maxime sequi velit asperiores voluptas deleniti eaque iure rerum, ullam numquam repellat saepe laboriosam excepturi error. Mollitia odit ipsa dignissimos? Corporis.</p>

        <p>Eligendi placeat architecto quia labore, facilis aliquam maxime ad perspiciatis cumque molestiae nam sed eius inventore dolor alias nesciunt. Rem voluptatibus dolorem consequatur, velit animi provident deserunt cum at quisquam?</p>

        <p>Modi, non ratione eos ad expedita quae quo et officiis necessitatibus consequuntur fuga officia architecto facere qui. Odit amet animi quibusdam! Distinctio ullam veniam fugiat odit, a maiores minus cupiditate?</p>

        <p>Recusandae quis iste architecto quidem velit quam debitis quia minima ullam nisi quo, asperiores accusamus soluta repudiandae laborum vero reiciendis. Reiciendis, aliquam sit deleniti a laboriosam ad perferendis eligendi quas!</p>

        <p>Dicta, nesciunt rem natus quis quo possimus inventore consequatur cum corporis dolores nulla eligendi sint placeat aliquid labore nihil dolor facere perspiciatis iusto, assumenda sit obcaecati ullam doloribus? Explicabo, nesciunt.</p>

        <p>Possimus quaerat labore delectus sed esse libero iste, aut aspernatur officia mollitia, sapiente fuga dolorem aliquam qui, reiciendis quia sequi illum a temporibus? Doloremque suscipit, necessitatibus consectetur incidunt animi eligendi.</p>

        <p>Laudantium aut, doloribus iste excepturi expedita cumque dolorem atque quibusdam, voluptate beatae quaerat ad voluptas impedit itaque quam culpa. Incidunt voluptas rem aut harum accusantium repudiandae et veniam temporibus qui.</p>

        <p>Qui eius tenetur sunt, debitis error sit harum atque ea unde quam odit quod iure laudantium impedit reprehenderit? Accusamus asperiores est distinctio labore sequi veniam, corporis natus sed. Odit, nostrum.</p>

        <p>Quibusdam temporibus vitae eum atque aperiam ut accusamus dolores ad assumenda tempora, rerum pariatur veniam dolorum mollitia tempore doloremque maxime architecto? Autem dicta odio nam quos praesentium corrupti aut ex!</p>

        <p>Numquam veritatis porro vero nulla repellendus fuga, illo itaque corporis molestias delectus animi facere exercitationem, libero vitae! Deleniti corrupti totam consequatur consectetur, tempora numquam doloribus voluptates tenetur ad molestiae accusantium!</p>

        <p>Nemo, voluptatibus quisquam similique corrupti itaque nisi minima consectetur earum dolorem quidem deleniti sunt. Illo quibusdam similique asperiores reprehenderit et illum? Alias nulla iusto veritatis laboriosam hic voluptatum totam incidunt?</p>

        <p>Quibusdam voluptatum esse maxime maiores magni, magnam fugiat aspernatur nemo, blanditiis nobis veritatis aliquam nisi sunt corrupti reiciendis distinctio animi, ea illo officiis nulla sit perferendis commodi nihil! Saepe, numquam.</p>

        <p>Harum non labore, deserunt dignissimos esse quae. Quo velit harum consequuntur, porro ipsam unde repellat natus eos eligendi praesentium maiores dolor molestias impedit. Dolorum, odio at minus maiores officia est?</p>

    </section>

  
  

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

  

    #list{

        border:1px solid black;

        width: 1000px;

    }

    #list .box{

        width: 100px;

        height: 50px;

        margin: 15px 0;

        transition-property: all;

        transition-duration: 5s;

    }

  

    #box1{

        /*transition-timing-function: linear;*/

        background-color: tomato;

        transition-delay: 0;

    }

    #box2{

        /*transition-timing-function: ease;*/

        background-color: gold;

        transition-delay: 0.5s;

    }

    #box3{

        /*transition-timing-function: ease-in;*/

        background-color: cornflowerblue;

        transition-delay: 1s;

    }

    #box4{

       /* transition-timing-function: ease-out;*/

        background-color: greenyellow;

        transition-delay: 1.5s;

    }

    #box5{

       /* transition-timing-function: ease-in-out;*/

        background-color: pink;

        transition-delay: 2s;

    }

  
  

    #list:hover .box{

        transform: translate(900px, 0px);

    }

</style>

</head>

<body>

    <div id="list">

        <!-- div#box$.box*5 -->

        <div id="box1" class="box">linear</div>

        <div id="box2" class="box">ease(default)</div>

        <div id="box3" class="box">ease-in</div>

        <div id="box4" class="box">ease-out</div>

        <div id="box5" class="box">ease-in-out</div>

    </div>

</body>

</html>

```

