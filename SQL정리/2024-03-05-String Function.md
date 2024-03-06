# String Function (문자열 함수)

문자열에 대한 함수들의 모음이다..  

## 대소문자 변환


- upper(컬럼명) : 모든 영어를 대문자로
- lower(컬럼명) : 모든 영어를 소문자로
- initcap(컬럼명) : 맨 앞 영어 스펠링만 대문자로   

## substr () 문자열 추출

- substr(컬럼명,시작위치,몇개의 글자를 가져올지)   
ex) tel 컬럼에 데이터 010-1234-5678 이 있을 때   
substr(tel,5,9) 하게 되면 1234-5678이 출력 된다  

## length ()  문자열 길이
자바 문자열 함수 length와 똑같이 길이를 반환한다.    

ex) Oracle 이라는 데이터가 들은 컬럼 a 검색시   

length(a) 하면 6이 나온다 ..  

## instr() 문자열 검색

java로 치면 indexof랑 똑같은 것이다.  

instr(컬럼명,검색어)