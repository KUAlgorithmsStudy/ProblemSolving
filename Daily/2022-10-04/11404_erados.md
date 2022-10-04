# 풀이
- 플로이드-워셜 을 썼다.
- 거리가 0 인 경우를 핸들링 하느라 로직이 복잡해졌다.
- 이건 마지막에 프린트 할 때 필터링 하는 편이 낫다.

# 코드
```python
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[0] * N for _ in range(N)]

for _ in range(M):
    i, j, c = map(int, input().split())
    graph[i - 1][j - 1] = min(graph[i - 1][j - 1], c) if graph[i - 1][j - 1] else c

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j:
                if graph[i][j] and graph[i][k] and graph[k][j]:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                elif graph[i][k] and graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


print("\n".join(" ".join(map(str, row)) for row in graph))

```