# 타겟이 있는 list 찾는 문법 
```css
.list[target] > a{color: blue;}

.list > a[target=_blank]{color: blue;}

.list > a[href^='https://']{color: blue;}

.list > a[href$='.com']{color: blue;}

.list > a[href*='co']{color: blue;}


```
## 속성 선택자 
1.  선택자\[속성명\] : 해당 속성을 명시하고 있는 태그

2. 선택자\[속성명=값\] : 해당 속성과 값을 명시하고 있는 태그

3. 선택자\[속성명^=값\] : 시작 (startsWith(), like '값%')

4. 선택자\[속성명$=값\] : 끝 (endsWith(), like '%값')

5. 선택자\[속성명*=값\] : 포함 (contains(), like '%값%'')


```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

<style>
.list > a[href*='co']{color: blue;}
  

</style>

</head>

<body>

    <h1>속성 선택자</h1>

  

    <!-- img[width] -->

  

    <div class="list">

        <a href="http://naver.com" target="_self">네이버</a>

        <a href="http://yes24.com" target="_blank">예스24</a>

        <a href="https://daum.net">다음</a>

        <a href="https://11st.cokr">11번가</a>

        <a href="https://kma.go.kr" target="_blank">기상청</a>

    </div>

</body>

</html>
```

