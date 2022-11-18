# 2022-10-07

# 백준 1976

# 20분

# Algorithms & Datastructures - BFS or UNION FIND

# 코드 - Python

```python
from collections import defaultdict, deque
n = int(input().rstrip())
m = int(input().rstrip())
g = [[*map(int, input().split())]  for _ in range(n)]
plan = [*map(int ,input().split())]
parent = [i for i in range(n)]

def findd(x):
    if parent[x] != x: parent[x] = findd(parent[x])
    return parent[x]

def union(a, b):
    aa = findd(a)
    bb = findd(b)
    if aa == bb: return
    elif aa<bb: parent[bb] = aa
    else: parent[aa] = bb
    return
for fromm in range(n):
    for to in range(n):
        if g[fromm][to]: union(fromm, to)

for i in range(len(plan)-1):
    if parent[plan[i]-1] != parent[plan[i+1]-1]: print('NO'); exit(0)
print("YES")
```

# 풀이

BFS로 풀자면, 여행가려고 하는 도시 중 한 곳을 시작으로 BFS 탐색을 해줍니다.
그 후 방문하고자 한 도시를 모두 방문 했다면 YES 출력합니다.
