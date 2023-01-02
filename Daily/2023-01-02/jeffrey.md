핵심 : 
1. dist 를 따로 관리하며 이를 통해 pruning 결정할 지 판단하기
2. 초기화 조건. visited[N] = 1 , dist[N] = 0

```python
"""
요약
N->K 까지 가는 최단경로를 구하고, 그 경로의 수를 구하는 문제
1. 2가지 방법 중 하나 택하며

설계
BFS

주의점
0< N, K < 10만

1. N>K 일때는 N-K

"""
import math
from collections import deque

N, K = map(int, input().split())
visited = [0] * 200001
dist = [math.inf] * 200001
queue = deque([(N, 0)])

dist[N] = 0
visited[N] = 1

while queue:
    cur, cnt = queue.popleft()

    # 종료 조건
    if visited[K] and cnt > dist[K]:
        break

    # 1. 2가지 방법 중 하나 택하며
    for next in [cur - 1, cur + 1, cur * 2]:
        if 0 <= next < 200001 and cnt + 1 <= dist[next]:  # TODO : 14만 이면 충분
            visited[next] += 1
            dist[next] = cnt + 1
            queue.append((next, cnt + 1))

print(dist[K])
print(visited[K])

```