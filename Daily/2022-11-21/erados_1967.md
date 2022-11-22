# 풀이

# 코드
```python
import sys
from collections import defaultdict

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
graph = defaultdict(list)
ans = 0

N = int(input())

for _ in range(N - 1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))


def dfs(start, weight):
    global ans
    temp = []
    if graph[start] == []:
        return weight

    for node, w in graph[start]:
        temp.append(dfs(node, w))
    temp.sort()
    ans = max(ans, sum(temp[-2:]))

    return temp[-1] + weight


dfs(1, 0)

print(ans)
```