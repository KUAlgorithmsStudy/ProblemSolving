# 풀이
- 플로이드-워셜 로 풀었다.
- 주의할 점은 왕복이 가능하다는 점이다.
- 그리고 자기 자신과의 거리가 INF 이므로 계산시 자기 자신을 따로 더해줘야한다.

# 코드
```python
import sys

input = sys.stdin.readline
INF = 16
N, M, R = map(int, input().split())

scores = list(map(int, input().split()))
graph = [[INF] * N for _ in range(N)]

for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a - 1][b - 1] = l
    graph[b - 1][a - 1] = l # 왕복 !

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
print(
    max(
        [
            sum(
                [scores[j] if graph[i][j] <= M else 0 for j in range(len(graph[i]))]
                + [scores[i]]
            )
            for i in range(len(graph))
        ]
    )
)

```