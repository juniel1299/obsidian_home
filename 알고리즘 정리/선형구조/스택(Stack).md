![[스택 이미지.png]]

# 스택

스택은 큐와 자주 비교되는 구조이며, 먼저 들어간 데이터가 가장 마지막에 나오는 LIFO(Last In First Out) 후입선출의 개념을 가진 배열이다.  

대표적으로 Ctrl Z 같은게 스택의 응용으로 많이 언급이 되며, 비유는 설거지 그릇 사진 같은게 많이 나온다 ;; (먼저 들어온 접시는 맨 밑에 깔려 마지막에 설거지가 진행되어 마지막에 나가므로)  

## 스택 활용
대표적으로 
Ctrl Z 즉 되돌리기(push 새로운 페이지 pop 이전 페이지)

함수 호출

괄호 검사

계산기 (후위 표기식 계산)

미로 탐색 등에서 이용된다.  

## 장점
구조가 단순하다 -> 구현 난이도가 낮음..

데이터 조회, 저장에 대해 속도가 굉장히 빠름 

## 단점
선언시에 배열 크기를 작성하므로 크기가 모자를 경우 다시 선언하고 데이터를 옮겨야한다..


### 예시 문제
괄호(실버4)
https://www.acmicpc.net/problem/9012

쇠막대기(실버2)
https://www.acmicpc.net/problem/10799

후위 표기식(골드2)
https://www.acmicpc.net/problem/1918

문자열 폭발(골드4)
https://www.acmicpc.net/problem/9935

외계인의 기타연주 (실버1)
https://www.acmicpc.net/problem/2841

코딩은 예쁘게(골드3)
https://www.acmicpc.net/problem/2879