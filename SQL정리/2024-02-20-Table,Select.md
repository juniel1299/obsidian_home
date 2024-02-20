# 테이블 선언 (생성)
create table 테이블이름   
(  
     컬럼선언(컬럼명 , 자료형)  뒤에 제약사항도 걸 수 있지만 그건 이후 글에서 서술 예정  
)  

예시 
```sql
create table school(
 name varchar2(10), --이름 (문자)
 korScore number,    -- 국어성적(숫자)
 graduation date     --졸업날짜 (날짜형)
);
```

![출력]()