# A\* 알고리즘 

A\* 알고리즘은  다익스트라 알고리즘의 연장선상으로 만들어진 알고리즘이다. 
주로 드론, 로봇 인공지능등에서 많이 사용이 된다. 

단, 다익스트라와 달리 휴리스틱 함수를 이용한다 

## 휴리스틱 함수 
f(x) = g(x) + h(x) 라는 식을 통해 A\* 알고리즘은 구성이 되어있는데,   

여기서 h(x)는 휴리스틱 함수 , g(x) 는 현재 상태의 비용이며, f(x)가 가장 최소가 되는 지점을 우선적으로 탐색한다 즉, f(x)는 작은 값부터 탐색을 진행하게 되므로, **우선순위 큐를 활용한다.**
휴리스틱 함수가 없으면 다익스트라와 동일한 알고리즘이 되므로,  휴리스틱 함수의 영향을 많이 받는 알고리즘이다. 


## 다익스트라를 안 쓰고 A\* 쓰는 이유 
위에서 언급했듯이, A\*알고리즘의 경우 로봇의 인공지능과 드론에서 많이 이용을 하는데, 

다익스트라의 경우 그냥 현재 상태에 대한 비용만 생각하기 때문에, 현실에서 적용하게 될 경우, 거리라는 개념은 다익스트라로 어찌저찌 표현이 가능 할 수 있겠지만, 그 안에서의 변수, 횡단보도라던가, 교통체증, 공사 중 등등 다양한 상황에서의 변수가 발생했을 때 현재 상태에 대한 비용만 따지기에는 현실적으로 어렵다는 판단을 하여, 휴리스틱이라는 상황에 따른 변수를 넣을 수 있는 공간을 하나 만들어 사용하는 것이다.


## 동작 
1. f(x) 를 오름차순 우선순위 큐에 노드로 삽입 
2. 우선순위 큐에서 최우선 노드를 pop
3. 해당 노드에서 이동 할 수  있는 노드를 찾는다
4. 그 노드들의 f(x)를 구한다. 
5. 그 노드들을 우선순위 큐에 삽입한다.
6. 목표 노드에 도달 할 때 까지 반복


## 구현 
```python
import heapq



# 그래프의 각 노드를 나타내는 클래스, 노드상태, 부모 노드, 시작노드로부터 
class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state  # 노드의 상태
        self.parent = parent  # 부모 노드
        self.g = g  # 시작 노드로부터 현재까지의 경로 비용
        self.h = h  # 목표 노드까지의 예상 경로 비용

    def f(self):
        return self.g + self.h  # 총 경로 비용

def astar(start_state, goal_state, neighbors, heuristic):
    start_node = Node(start_state)
    goal_node = Node(goal_state)

    open_set = []  # 열린 집합
    closed_set = set()  # 닫힌 집합

    heapq.heappush(open_set, (start_node.f(), id(start_node), start_node))

    while open_set:
        _, _, current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for neighbor_state in neighbors(current_node.state):
            if neighbor_state in closed_set:
                continue

            g = current_node.g + 1  # 간선 비용은 1로 가정
            h = heuristic(neighbor_state, goal_state)
            neighbor_node = Node(neighbor_state, current_node, g, h)
            heapq.heappush(open_set, (neighbor_node.f(), id(neighbor_node), neighbor_node))

    return None

# 예시: 그래프의 이웃 찾기
def neighbors(state):
    # 이웃을 반환하는 함수 (예시로 간단하게 구현)
    x, y = state
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

# 예시: 휴리스틱 함수 (맨해튼 거리)
def manhattan_distance(state, goal_state):
    x1, y1 = state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)

# 테스트
start_state = (0, 0)
goal_state = (4, 4)
path = astar(start_state, goal_state, neighbors, manhattan_distance)
print("최단 경로:", path)



```