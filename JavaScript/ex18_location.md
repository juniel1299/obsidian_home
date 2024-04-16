# 자바스크립트의 location
- window > location 
- 현재 창의 페이지 주소 참조 객체 > URL 조작
- console.log(location.href); // 읽기

**페이지 이동 (자바스크립트)**

- location.href = 'ex16_window.html'; //쓰기 
- location.reload(); //새로고침 
- location.assign('ex16_window.html');


## 전역 이벤트
- 어떤 상황에서 행동하던지 상관없이 > 항상 발생하는 이벤트 

```html

window.onkeydown = m2;


        function m2() {

            //alert(event.keyCode);

            //78, 71, 68

            if (event.keyCode == 78) {

                location.href = 'https://naver.com';

            } else if (event.keyCode == 71) {

                location.href = 'https://google.com';

            } else if (event.keyCode == 68) {

                location.href = 'https://daum.net';

            }

        }
```

