# 풀이
원리는 잘 모른다. 찾아보고 추가하겠음.

# 코드
```python
import sys

input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

graph = [[0] * len(B) for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            graph[i][j] = graph[i - 1][j - 1] + 1 if i and j else 1
        else:
            graph[i][j] = max(graph[i - 1 if i else i][j], graph[i][j - 1 if j else j])

print(graph[-1][-1])

```