# App Router (앱 라우터)
1. Page Router 와 달리 페이지 라우팅 설정 방식 변경됨
2. React 18 신규 기능 추가
3. 데이터 페칭 방식 변경
4. 레이아웃 설정 방식 변경
5. 페이지 라우팅 설정 방식 변경

네이게이팅 , 프리페칭 , 사전 렌더링 부분은 기존 페이지 라우터와 동일 ( 변경사항이 없음. )

파일명이 page 면 페이지 역할 , layout이면 layout 역할 

## 페이지 라우팅 
Page Router 에선 pages 폴더 아래에서 ~/search -> search.tsx 파일 식이지만
App Router 에선 app 폴더 아래에서 /search 폴더 아래의 page.tsx 로 작성해야 동일한 동작이 가능함. 

동적 경로의 경우
App Router는 \[id\] 폴더 아래에 page.tsx 작성하면 됨 -> book/1 , book/2 등등 .

### 페이지 라우팅 설정 
폴더명이 경로 화면은 page.tsx 로 꾸민다 .

폴더명/\[id\] -> book/id 에 해당하는 화면 ex)book/1 , book/100
폴더명/\[...id\] -> 해당 화면 뒤에 추가적으로 이어 붙일 수 있음 ex) book/1/2/3/4/5
폴더명/\[\[id\]\] -> /book 뒤에 추가 경로가 없는 경우 ex) /book

### 레이아웃 설정
폴더명이 경로 화면의 레이아웃은 layout.tsx 로 작성함 
ex ) book 폴더에 layout.tsx로 레이아웃 파일 작성 -> 하위에 폴더를 만들어도 상위 layout.tsx 적용받음.
만약 하위에는 새로운 layout을 적용하고 싶으면 하위 폴더에 layout.tsx 작성 -> 2개가 중첩으로 적용됨.

설정을 따로 하지 않으면 레이아웃 파일을 작성하면 기존 page.tsx에 있던건 화면에 뜨지 않음

