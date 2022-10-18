# 풀이
- LCS 랑 비슷하게 풀었으나 틀림 !

# 코드
```python
import sys

input = sys.stdin.readline

N = int(input())
graph = [[1] * N for _ in range(N)]

A = list(map(int, input().split()))


for y in range(1, N):
    for x in range(1, N):
        graph[y][x] = max(
            graph[y - 1][x],
            graph[y][x - 1],
            graph[y - 1][x - 1] + 1 if A[x - 1] < A[x] else graph[y - 1][x - 1],
        )


print(graph[N - 1][N - 1])

for i in range(N):
    if i == 0 or A[i] > A[i - 1]:
        print(A[i], end=" ")
```