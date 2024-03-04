
# Aggregation Function (집계 함수)

그냥 자바로 치면 count,sum,max,min,average 임..  

SQL에선 count() , sum() , avg() , max(), min() 그냥 똑같음...  


## count()
컬럼의 데이터 수를 세야 할 때 사용 (단 null은 카운트 하지 않음)  

```sql

select count(*) from tblInsa;
```
이렇게 모든 직원의 수를 구할 수 있다.  
![출력](https://github.com/juniel1299/juniel1299.github.io/assets/62318700/5dd449e0-2d6c-4997-a29b-4831289b5149)

앞에 있었던 distinct와 섞어서 부서 종류가 몇개인지 구한다던지 활용 방법이 많아 자주 쓰인다.  

