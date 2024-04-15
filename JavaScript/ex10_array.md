# 자바스크립트의 배열 
Array(외형) + ArrayList(성질-가변, object)

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

        /*

        // 배열

        // Array(외형) + ArrayList(성질-가변, Object)

        // Array 내장 객체

        */

  

        //int[] nums = new int[3];

        var nums = new Array(); //new ArrayList();

        //indexer 지원

        nums[0] = 100;

        nums[1] = 200;

        nums[2] = 300;

        //nums[3] = '홍길동'; (자료형은 하나만)

        //num[5] = 500; //건너뛰기 안 됨

  

        for(var i=0; i<nums.length; i++){

            console.log(i, nums[i]);

        }

  

        console.log(16, nums[16]);

  

        console.clear();

  

        // 초기화 리스트

        // int[] nums = new int[] {100,200,300};

        // int[] nums = {100,200,300};

  

        var nums2 = new Array(100,200,300);

        var nums3 = [100,200,300]; //배열 리터럴(Literal)***

  

        //빈 배열

        var nums4 = new Array();

        var nums5 = []; //주로 사용 ****

  
  

        //3의 배수 > 10개 > 배열 생성

        var list1 = [];

  

        for(var i=0; i<10; i++){

            list1[i] = (i+1)*3;

        }

  

        console.log(list1);

        var list2 = [];

  

        for(var i=3; i<=(3*10); i+=3){

            list2.push(i); //stack.push (값) , list.append(값)

        }

        console.log(list2);

        console.log(list2.pop());

        console.log(list2);

  

    </script>

</body>

</html>
```