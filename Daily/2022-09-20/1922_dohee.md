# 2022-09-20

# 백준 1922 네트워크 연결

# 10분 - 유형 kruskal

# 코드 - Python

```python
from collections import defaultdict,deque

n = int(input().rstrip())
m = int(input().rstrip())
arr = []
for _ in range(m):
    a,b, c = map(int ,input().split())
    arr.append((c,a-1,b-1))
arr.sort()
parent = [i for i in range(n)]

def findd(x):
    if parent[x] != x: parent[x] = findd(parent[x])
    return parent[x]

def union(a,b):
    aa = findd(a)
    bb = findd(b)
    if aa == bb: return False
    elif aa<bb: parent[bb] = aa
    else: parent[aa] = bb
    return True

ans = 0
for l in arr:
    cost,a,b = l
    if union(a,b): ans += cost
print(ans)

```

# 풀이

전형적인 kruskal 알고리즘 문제이었습니다.
크루스칼 알고리즘은 union find를 바탕으로 구현할 수 있습니다.
(1) weight를 기준으로 node의 연결 정보를 sort한 후,
(2) find를 통해 연결의 여부를 확인하고
(3) union을 통해 연결되지 않은 node들을 연결해주면 됩니다.

연결 관계를 이미 sorting(오름차순) 해두었기 때문에 가장 적은 weight 먼저 연결해주게 됩니다.

따라서 최종적으로 모두 연결해주면 완성되는 그래프는 MST(특정 그래프에서 최소한의 비용으로 만들어지는 tree)입니다.
