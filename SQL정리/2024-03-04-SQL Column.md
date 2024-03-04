# Column (컬럼)

행렬로 치면 열에 해당하는 것을 뜻함   
컬럼은 다양한 속성을 가진다.  

ex)   

이름   직급 나이 연봉   
OOO  대리  31    4000   

이런식으로 이름 직급 나이 연봉에 해당하는 위치이다 .   


## distinct 
중복값을 제거해준다 

![출력](https://github.com/juniel1299/juniel1299.github.io/assets/62318700/1ab7c560-384f-4c8b-9292-fc42a8e01380)

기존 테이블의 값에서 
select distinct buseo from tblinsa;  

즉 부서 컬럼에 distinct를 사용하게 되면  

![출력](https://github.com/juniel1299/juniel1299.github.io/assets/62318700/fd09b66f-9612-4e50-839b-5f963377823a)

이렇게 중복되는 값을 다 없애고 출력이 된다.  

## case
SQL에서 조건문 실행을 할 수 있는 방법 중 하나이다.  

case when then end 으로 구성이 되어 있으며 
when 조건 then 반환값 의 형식이다.  

앞의 테이블을 이용해서 사용하면

```sql
select name,
case when substr(ssn,8,1) = 1 then '남자'  
	 when substr(ssn,8,1) = 2 then '여자'
     end
from tblinsa;

```


