![[BFS 이미지.gif]]

**한 정점에서 가장 인접한 노드를 먼저 넓게 탐색하면서 깊이 내려가는 형태의 탐색**

- 재귀적으로 동작하지 않는다.
- 노드 방문 여부를 검사합니다 (DFS와 동일)
- 큐를 활용하여 방문한 노드를 정리합니다.  
- 추후 최단경로 알고리즘 관련에 사용됩니다..  


## 구현 

```java
import java.util.LinkedList;

import java.util.Queue;

 

public class Bfs {

    public static void main(String[] args) {

        // 각 노드가 연결상태를 2차원 배열로 표현

        int[][] graph = {{}, {2, 3}, {4}, {5, 6}, {2}, {5, 7}, {3}, {7}};

 

        // 방문처리에 사용 할 배열

        boolean[] visited = new boolean[graph.length];

 

        // 시작 노드

        int start = 1;

 

        // 큐 생성

        Queue<Integer> queue = new LinkedList<>();

        queue.add(start);

 

        // 현재 노드를 방문 처리

        visited[start] = true;

 

        // 큐가 비었을 때 까지 반복

        while (!queue.isEmpty()) {

            // 큐에서 하나의 원소를 뽑아 출력

            int node = queue.poll();

            System.out.print(node + " -> ");

 

            // 인접한 노드 중 아직 방문하지 않은 원소들을 큐에 삽입

            for (int index : graph[node]) {

                if (!visited[index]) {

                    queue.add(index);

                    visited[index] = true;

                }

            }

        }

    }

}
```
### 예시 문제
Puyo Puyo (골드4)
https://www.acmicpc.net/problem/11559

인성 문제 있어? (골드4)
https://www.acmicpc.net/problem/19952

숨바꼭질 (실버1)
https://www.acmicpc.net/problem/6118

[[BFS 예시 문제]]