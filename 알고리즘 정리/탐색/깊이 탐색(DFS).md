		![[DFS 이미지.gif]]

**그래프에서 깊은 부분을 우선적으로 탐색하는 방법  
한 정점에서 시작해 다음으로 넘어가기 전 해당 경로를 우선적으로 탐색함 . **

- BFS에 비해 검색 속도가 느림 
- 모든 경우를 다 탐색할 때 사용함 
- 어떤 노드를 방문하였는지 검사를 하지 않으면 무한루프에 빠질 수 있음. 
## 구현 

```java
public class Dfs {

    public static void main(String[] args) {

        int start = 1; // 시작 노드

        dfs(start);

    }

 

    // 각 노드가 연결상태를 2차원 배열로 표현

    // 해당 graph의 인덱스번호의 배열은 해당 노드에서 연결된 노드를 갖는다.

    //                      0번  1번    2번    3번     4번    5번   6번   7번

    static int[][] graph = {{}, {2, 3}, {4}, {5, 6}, {2}, {5, 7}, {3}, {7}};

 

    // 방문처리에 사용 할 배열

    static boolean[] visited = new boolean[graph.length];

 

    static void dfs(int index) {

        // 현재 노드를 방문 처리

        visited[index] = true;

 

        // 방문 노드 출력

        System.out.print(index + " -> ");

 

        // 방문한 노드에 인접한 노드 찾기

        for (int node : graph[index]) {

            // 인접한 노드가 방문한 적이 없다면 재귀 호출

            if(!visited[node]) {

                dfs(node);

            }

        }

    }

}

```

