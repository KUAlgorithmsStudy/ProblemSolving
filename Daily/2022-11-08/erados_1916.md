# 풀이
다이크스트라 썼다.

# 코드
```python
from heapq import heappush, heappop
import sys

input = sys.stdin.readline
INF = 10e9
N = int(input())
M = int(input())
graph = [[] * (N + 1) for _ in range(N + 1)]
distance = [INF] * (N + 1)
visited = [False] * (N + 1)
for _ in range(M):
    i, j, c = map(int, input().split())
    graph[i].append((c, j))

s, e = map(int, input().split())


def dijkstra():
    q = []
    heappush(q, (0, s))

    while q:
        current_distance, current_city = heappop(q)

        if not visited[current_city]:
            for dist_next_city, next_city in graph[current_city]:
                next_distance = current_distance + dist_next_city
                if next_distance < distance[next_city]:
                    distance[next_city] = next_distance
                    heappush(q, (next_distance, next_city))

        visited[current_city] = True


dijkstra()
print(distance[e])
```