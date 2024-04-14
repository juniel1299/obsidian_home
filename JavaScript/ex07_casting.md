# 내장 함수 built-in function

형변환
1. number parseInt(value) : 정수 형태를 가지는 number로 변환 
2. number parseFloat(value) : 실수 형태를 가지는 number로 변환 


```js
            var n1 = 3.14;

            console.log(parseInt(n1));

  

            var n2 = '300';

            console.log(n2,typeof n2);

            console.log(parseInt(n2), typeof parseInt(n2));

  

            var n3 = '홍길동';

            console.log(n3,typeof n3);

            console.log(parseInt(n3)); // NaN = not a number

  

            var n4 = '100점';

            console.log(parseInt(n4)); //100

  

            var n5 = '스코어90';

            console.log(parseInt(n5)); //NaN
```

**단 숫자가 먼저 나오면 숫자까지만 출력 후 문자는 다 버림**

