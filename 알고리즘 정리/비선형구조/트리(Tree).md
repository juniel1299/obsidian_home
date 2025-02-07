![[트리 이미지.webp]]
- 루트 : 위에 아무것도 없는 노트 (시작점)
- 노드 : 트리의 구성요소
- 서브트리 : 하나의 노드와 그 노드의 자손으로 이루어진 트리
- 레벨 : 위에서부터 1~n까지의 번호를 부여(위치 설명)
- 높이 : 루트부터 단말까지 총 수 (단, 루트는 레벨0 이므로 포함하지 않는다.) 
- 차수 : 노드 밑에 있는 노드 갯수
**위 그림을 예시로 들면 A 기준으로 높이는 3을 가지며, 트리의 깊이는 3 가진다. **

1. 트리는 계층적인 구조를 나타내는 자료구조이다.
2. 개념상 비선형 구조이다.
3. 저장은 배열 + 연결기법으로 구현된다.

응용 : 계층적 조직 표현 , 파일 시스템, 인공지능 결정 트리

## 완전 이진 트리
![[완전이진트리.png]]

마지막 레벨을 제외하고 자식을 2개씩 가지고 있어야 합니다 그리고 노드는 왼쪽에서 오른쪽 방향으로 채워져야 합니다. 즉 사진 기준으로 2 , 3 이 자식을 2개씩 가지며 왼쪽에 우선 자식을 가지기 때문에 완전 이진 트리가 성립합니다. 

노드 개수  n은

2^(높이-1)-1 <= n <= 2^높이-1 이다.  



## 포화 이진 트리 
![[포화이진트리.png]]

말단 부분을 제외하고 모두가 자식을 2개씩 가지는 경우를 의미한다.  

노드 개수 n= 2^(높이) - 1 이다.


## 이진 힙 
![[이진힙 이미지.jpg]]

이진 힙(Binary Heap)은 노드의 값이 특정한 순서를 가지고 있는 완전 이진 트리 (Complete Binary Tree)이다.  

이진 힙은 부모 노드 값이 자식 노드 값보다 큰지 작은지를 통해 최대 힙 또는 최소 힙으로 나뉘어 불린다.  

부모가 크면 최대 힙 , 자식이 크면 최소 힙으로 부른다 . 

## 전위/ 후위/ 중위/ 순회
![[전위중위후위 이미지.jpg]]

트리에서의 탐색 방법은 전위/중위/후위 그리고 DFS BFS가 존재한다 . 

전위 순회의 경우 루트 - 왼쪽 - 오른쪽

중위 순회의 경우 왼쪽 - 루트 - 오른쪽

후위 순회의 경우 왼쪽 - 오른쪽 - 루트 로 진행된다. 

