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

![출력](https://github.com/juniel1299/juniel1299.github.io/assets/62318700/7a0b5e66-96a5-44ce-b1cc-ac57919f0d7e)
생성한 테이블을 이렇게 보기 위해선 
```sql
select * from school;
```

데이터를 안에 넣고 싶으면 

```sql
insert 
```