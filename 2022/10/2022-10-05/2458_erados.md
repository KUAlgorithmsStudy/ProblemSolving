# 풀이
- 정방향으로 가는 방법을 플로이드-워셜 로 확인하고
- 역방향으로 가는 방법은 i->j 가 가능한 경우 j->i 가 가능하므로
- 전치 행렬로 확인하였다.

# 코드
```python
import sys

input = sys.stdin.readline
INF = 501

N, M = map(int, input().split())
graph = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

cnt = 0
for i in range(N):
    for j in range(N):
        if i != j:
            if graph[i][j] != INF or graph[j][i] != INF:
                cnt += 1
print(cnt)

```