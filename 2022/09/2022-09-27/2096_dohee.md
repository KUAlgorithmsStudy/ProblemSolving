# 2022-09-26

# 백준 2109

# 20분 - 순회강연

# 코드 - Python

```python
from collections import defaultdict, deque
INF= int(3e9)

n = int(input().rstrip())
memo = [[0,0,0] for _ in range(n)]
mini = [[INF,INF,INF] for _ in range(n)]

dir = [(0,1), (0,1,2), (1,2)]

for i in range(n):
    arr = [ *map(int,input().split()) ]

    if i>0 :
        for j in range(3):
            for d in dir[j]:
                memo[i][j] = max(memo[i][j], memo[i-1][d] + arr[j] )
                mini[i][j] = min(mini[i][j], mini[i-1][d] + arr[j] )
    else : memo[i] = arr; mini[i] = arr

print( max(memo[n-1]),  min(mini[n-1]))
```

# 풀이

dynamic programming을 활용했습니다.
