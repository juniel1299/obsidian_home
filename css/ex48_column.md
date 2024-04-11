column-count  : 문단 
column-gap : column 사이 간격 
column-rule : 사이 구분 선 디자인


```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

<style>

    p{

        column-count: 3;

        column-gap: 20px;

        column-rule: 1px dashed gray;

        text-align: justify;

    }

</style>

</head>

<body>

    <h1>column</h1>

    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas enim qui sit rerum maxime eos consequatur magnam natus ullam corporis modi, voluptatum officia nisi in inventore alias iste dolorem eaque ipsum. Dolores debitis reprehenderit, explicabo quam velit ut. Quam fuga veritatis qui, sit, corrupti quisquam aperiam pariatur voluptate doloremque deleniti voluptas magni reiciendis architecto autem. Esse modi id repudiandae labore nemo laboriosam consequatur itaque alias rerum, delectus ex molestiae adipisci, odio vel sed quis enim sint qui neque magni. Esse sed optio maxime pariatur ipsum modi laborum consectetur praesentium, architecto eaque adipisci tempora nesciunt quaerat numquam beatae accusamus placeat similique ullam minus, eum tempore. Numquam illo, deserunt delectus nisi cupiditate eos maiores, veniam repellat odit sit voluptatum tenetur, quasi dolorum iste obcaecati natus quibusdam saepe voluptate porro! Id saepe, aliquid magnam modi numquam cumque officia similique obcaecati eligendi pariatur veritatis quibusdam magni odio perspiciatis impedit, soluta tempore quia non suscipit dignissimos neque. Quia laborum obcaecati, excepturi aspernatur amet rerum quidem veritatis ab vel sed delectus numquam eos eum harum maiores voluptatum voluptatibus quasi saepe quis. Ipsum explicabo impedit quia ex eaque voluptate cumque voluptatem sunt minus magnam, eum unde quasi omnis nihil dolores perspiciatis inventore optio quae, aut reprehenderit quod illo quaerat temporibus! Fugiat nesciunt impedit accusamus, amet esse qui repellat voluptatum praesentium. Earum totam ipsum officiis aliquid voluptate amet dolor itaque doloremque eius, voluptas cum sapiente, nostrum saepe excepturi optio vel iusto, perferendis sed laborum corporis omnis cumque! Nisi ad odio sit eaque in illum assumenda minus cupiditate omnis iusto maxime vel fugit aliquid quasi numquam possimus inventore atque, fugiat labore enim aliquam velit magni ab aperiam. Quasi ut cum suscipit, ducimus perspiciatis a, eos sed magni quisquam necessitatibus aperiam doloribus obcaecati sint earum enim sequi? Error, veniam? Corrupti voluptates natus nisi possimus non. Fugiat inventore id alias quae nisi, eum repellendus atque veritatis quisquam maxime quam omnis aut recusandae aliquam aperiam maiores illo molestiae sit laboriosam iure blanditiis. Vero, nesciunt dolor voluptas, fuga consequatur dicta nobis nostrum harum tempore est, vitae cupiditate velit qui error voluptatibus cumque molestias? Modi repudiandae est, nobis temporibus architecto culpa, maxime delectus molestias ipsa excepturi quia in sint, facere distinctio amet esse saepe deleniti labore officiis suscipit quos. Mollitia impedit sit, incidunt maiores autem illo alias laudantium quis officiis adipisci sint aspernatur quam dolorum accusamus exercitationem recusandae dolore sed hic corrupti minus quasi velit. A obcaecati quos dolorum porro, neque rem temporibus quam saepe dolores consequatur voluptas omnis totam iure. Repudiandae, voluptatibus ratione, quis odio nostrum consequatur ipsum autem quod, at aliquid dolorum. Sed, laudantium quas. Magni repudiandae aperiam iure, maiores ipsum nobis esse quae temporibus ducimus provident blanditiis facere, laborum cum delectus voluptatibus est voluptas quaerat ullam. Veniam, illo minima. Ea quas odit facilis quos voluptate quibusdam! Eligendi, ea dignissimos! Qui culpa, alias eos tempore vel cumque ex amet. Obcaecati error ab necessitatibus libero autem vero. Consequatur eius eveniet, expedita officiis eaque consequuntur nihil in mollitia illo doloribus ea ab eligendi quasi repudiandae facilis corrupti quaerat voluptas? Ratione quia numquam corporis inventore.</p>

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

        width: 800px;

        column-count: 5;

    }

  

    #list .item{

        border: 1px solid #555;

        border-radius: 3px;

        width: 150px;

        margin: 0 auto 15px auto;

        box-shadow: 3px 3px 2px #999;

        page-break-inside: avoid;

    }

  

    #list .item img{

      display: block;

      margin: 20px auto;

      box-shadow: -1px -1px 1px #555;  

    }

  

    #list .item .txt{

        margin: 0 12px 20px 12px;

    }

</style>

</head>

<body>

    <h1>Card Layout</h1>

<!--

    <div class="item">

        <img src="images/rect_icon01.png" alt="">

        <div class="txt">

            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore, ad.

        </div>

    </div> -->

  
  

    <!-- (div.item>((img[src=images/rect_icon$$.png])+(div.txt>lorem10)))*20 -->

    <div id="list">

    <div class="item">

        <img src="images/rect_icon01.png" alt="">

        <div class="txt">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ex, sunt?</div>

    </div>

    <div class="item">

        <img src="images/rect_icon02.png" alt="">

        <div class="txt">Totam at ipsa quidem, dolorum hic neque adipisci odio facilis.</div>

    </div>

    <div class="item">

        <img src="images/rect_icon03.png" alt="">

        <div class="txt">Nemo, saepe eos? Reprehenderit, culpa recusandae consequuntur porro perspiciatis pariatur.</div>

    </div>

    <div class="item">

        <img src="images/rect_icon04.png" alt="">

        <div class="txt">Distinctio asperiores fugiat quos rerum repellat repellendus molestiae aliquam ad.</div>

    </div>

    <div class="item">

        <img src="images/rect_icon05.png" alt="">

        <div class="txt">Mollitia eum explicabo voluptatem at perspiciatis nostrum officiis quis obcaecati.</div>

    </div>

    <div class="item">

        <img src="images/rect_icon06.png" alt="">

        <div class="txt">Nesciunt est temporibus aperiam officia enim ex adipisci praesentium rerum.</div>

    </div>

    <div class="item">

        <img src="images/rect_icon07.png" alt="">

        <div class="txt">Nisi sequi minus voluptatibus sit inventore asperiores hic non expedita!</div>

    </div>

    <div class="item">

        <img src="images/rect_icon08.png" alt="">

        <div class="txt">Mollitia praesentium ab alias possimus cum in totam molestias deleniti.</div>

    </div>

    <div class="item">

        <img src="images/rect_icon09.png" alt="">

        <div class="txt">Neque sint, ipsam nemo rerum nihil perferendis numquam ullam libero.</div>

    </div>

    <div class="item">

        <img src="images/rect_icon10.png" alt="">

        <div class="txt">Ipsum explicabo mollitia ea velit, minima cumque vitae quis ipsa?</div>

    </div>

    <div class="item">

        <img src="images/rect_icon11.png" alt="">

        <div class="txt">Unde, odit ea eligendi amet molestiae illo perferendis soluta facere!</div>

    </div>

    <div class="item">

        <img src="images/rect_icon12.png" alt="">

        <div class="txt">Ipsum illum veritatis dolorem exercitationem voluptatem voluptates, error asperiores odit.</div>

    </div>

    <div class="item">

        <img src="images/rect_icon13.png" alt="">

        <div class="txt">Facilis ad laboriosam voluptates quod saepe provident maxime dolore nisi.</div>

    </div>

    <div class="item">

        <img src="images/rect_icon14.png" alt="">

        <div class="txt">Laborum facilis dignissimos quas, enim adipisci vel reprehenderit aut? Iste?</div>

    </div>

    <div class="item">

        <img src="images/rect_icon15.png" alt="">

        <div class="txt">Molestiae suscipit nisi voluptatum, voluptatibus assumenda sint cum repudiandae unde?</div>

    </div>

    <div class="item">

        <img src="images/rect_icon16.png" alt="">

        <div class="txt">Est deleniti illo fuga sapiente veritatis sint quidem saepe aliquam.</div>

    </div>

    <div class="item">

        <img src="images/rect_icon17.png" alt="">

        <div class="txt">Optio praesentium minus, a laudantium illum suscipit iure inventore illo!</div>

    </div>

    <div class="item">

        <img src="images/rect_icon18.png" alt="">

        <div class="txt">Animi asperiores itaque ullam consectetur! Ullam iusto nulla ducimus distinctio.</div>

    </div>

    <div class="item">

        <img src="images/rect_icon15.png" alt="">

        <div class="txt">Aperiam eum soluta ipsa expedita voluptas, natus odio quod iusto.</div>

    </div>

    <div class="item">

        <img src="images/rect_icon13.png" alt="">

        <div class="txt">Beatae nisi amet optio id corporis consectetur sequi veritatis dolor!</div>

    </div>

</div>

</body>

</html>
```

