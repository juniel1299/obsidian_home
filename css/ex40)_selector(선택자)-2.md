# 타겟이 있는 list 찾는 문법 
```css
.list[target] > a{color: blue;}

.list > a[target=_blank]{color: blue;}

.list > a[href^='https://']{color: blue;}

.list > a[href$='.com']{color: blue;}

.list > a[href*='co']{color: blue;}


```
## 속성 선택자 
1.  선택자[속성명] : 해당 속성을 명시하고 있는 태그

2. 선택자[속성명=값] : 해당 속성과 값을 명시하고 있는 태그

3. 선택자[속성명^=값] : 시작 (startsWith(), like '값%')

4. 선택자[속성명$=값] : 끝 (endsWith(), like '%값')

5. 선택자[속성명*=값] : 포함 (contains(), like '%값%'')


