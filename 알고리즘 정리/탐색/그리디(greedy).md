![[그리디 알고리즘 이미지.png]]

그리디 알고리즘은 현재 상황에서 최적이라고 생각하는 해를 선택하는 방법이다.  


**단 현재 상황에서의 최적이므로 전체적 의미의 최적이 아니다**

위 이미지처럼 전체에서의 최적은 100달러이나 , 시작 지점에서의 최적인 20달러를 고르고, 이후 상황에서 최적인 30달러를 고르게 된다.  


## 정당성

1. 탐욕적 선택 속성 (greedy choice property)
탐욕적인 선택이 항상 안전하다는 것이 보장된다는 의미 


2. 최적 부분 구조 (optimal substructure)
부분 최적해들이 모여 전체 최적해를 구할 수 있는 경우이다.  
전체 문제가 여러 부분 문제로 분할되며, 단계 하나하나마다의 최적해가 도출 되어야 한다.  



### 예시 문제
신입 사원 (실버1)
https://www.acmicpc.net/problem/1946

크리스 마틴 (골드4)
https://www.acmicpc.net/problem/7977
