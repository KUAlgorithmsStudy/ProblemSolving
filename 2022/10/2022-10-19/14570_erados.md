# 풀이
몰겠당..

# 코드
```python
import sys

input = sys.stdin.readline

N = int(input())
leaves = []
graph = [[] for _ in range(N + 1)]

# 그래프 생성
for i in range(1, N + 1):
    graph[i] = list(map(int, input().split()))


def dfs(n, depth):
    if graph[n] == [-1, -1]:
        leaves.append((n, depth))
    else:
        for i in graph[n]:
            if i != -1:
                dfs(i, depth + 1)


dfs(1, 0)

print(leaves)

```