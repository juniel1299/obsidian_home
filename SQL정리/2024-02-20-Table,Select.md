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

데이터를 안에 넣고 싶을땐 insert into를 이용한다

```sql
insert into school (name) values('신짱구');
insert into school (korScore) values(70);
insert into school (graduation) values('2024-02-21');

insert into school
values('훈이',90,'2024-02-23'); 
```
![출력](https://github.com/juniel1299/juniel1299.github.io/assets/62318700/a508af30-ed93-4696-9961-087fc75934ad)

처음 코드처럼 따로따로 넣으면 이렇게 하나만 들어가고 null이라고 뜬다   
null은 oracle SQL에서 작성해준 것이지 실제로 null이 들어간게 아니라 빈칸이다.  

그냥 데이터가 없다라는 내용이다.  

그러므로 insert into 선언시에는 한번에 해야하며 순서는 테이블 선언 순서와 동일하다 .  


# 테이블 데이터 가져오기 
Select 를 통해 진행하는데   

Select * from 테이블명; 으로 진행하게 된다    

우선 코드 동작 순서가 중요한데 아직 2개밖에 없으니 (select , from)    

우선 From이 실행되고 Select가 실행된다 알면 된다 .    

즉 테이블을 가져오고 Select 동작하는데   
 우선 * 은 import 가져올 때 * 과 동일하다 모두 선언을 의미하며 만약 위에 테이블에서 이름만 보고 싶으면   
select name from school; 작성하면 이름만 출력이 되며,  

select 
name,
graduation
from schoo; 작성하면 이름과 졸업년도만 나오게 하도록 할 수 있다.  
