
# Aggregation Function (집계 함수)

그냥 자바로 치면 count,sum,max,min,average 임..  

SQL에선 count() , sum() , avg() , max(), min() 그냥 똑같음...  


## count()
컬럼의 데이터 수를 세야 할 때 사용 (단 null은 카운트 하지 않음)  

```sql

select count(*) from tblInsa;
```
이렇게 모든 직원의 수를 구할 수 있다.  
