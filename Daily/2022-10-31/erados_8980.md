# 풀이
다 쑤셔 넣었더니
15점 받음 ㅎㅎ

# 코드
```python
import sys
from pprint import pprint

input = sys.stdin.readline

# 마을수, 트럭 크기
N, C = map(int, input().split())

# 택배 정보 수
M = int(input())
ans = 0

# 택배 정보 저장용
# graph[0] 는 트럭에 적재된 택배 정보로 사용
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    i, j, w = map(int, input().split())
    graph[i][j] = w

for i in range(N + 1):
    ans += graph[0][i]
    graph[0][i] = 0
    for j in range(i + 1, N + 1):
        currnt_cargo = sum(graph[0])
        if currnt_cargo < C:
            graph[0][j] += min(graph[i][j], C - currnt_cargo)

print(ans)

```