# 풀이
- 플로이드-워셜 로 풀었다.
- 자기 자신으로 가는 것을 고려해야한다.

# 코드
```python
import sys

input = sys.stdin.readline
last_city = None
INF = 10**5
N = int(input())
M = int(input())

graph = [[INF] * N for _ in range(N)]

for i in range(N):
    graph[i] = list(map(lambda x: int(x) if x != "0" else INF, input().split()))

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for city in map(int, input().split()):
    if last_city != None and graph[last_city][city - 1] == INF:
        if last_city == city - 1:
            continue
        print("NO")
        exit(0)
    last_city = city - 1

print("YES")

```