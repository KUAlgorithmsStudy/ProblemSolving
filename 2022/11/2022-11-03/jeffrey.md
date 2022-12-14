빗물
: 스택; 20분

```python
H, W = map(int, input().split())
board = list(map(int, input().split()))


left = []
for h in board:
    if not left:
        left.append(h)
    else:
        el = max(left[-1], h)
        left.append(el)

right = []
for h in reversed(board):
    if not right:
        right.append(h)
    else:
        el = max(right[0], h)
        right.insert(0, el)

N = len(board)
result = 0
for i in range(N):
    result += (min(left[i], right[i]) - board[i])

print(result)
```

합승택시
: 벨만포드 알고리즘 ; 35분

```python
"""
벨만포드 알고리즘

주의사항
1. 1-idx 임

- 자기자신에서 출발하고 도착하는건 0으로 따로 업데이트해줘야함.
"""

import math
def solution(n, s, dest_a, dest_b, fares):
    
    table = [[math.inf for _ in range(n+1)] for _ in range(n+1)]

    for (st, ed, f) in fares:
        table[st][ed] = f
        table[ed][st] = f
    
    for i in range(n+1):
        table[i][i] = 0

    for k in range(n+1):
        for src in range(n+1):
            for dst in range(n+1):
                table[src][dst] = min(table[src][k] + table[k][dst], table[src][dst])

    min_common_fare = math.inf
    for k in range(n+1):
        cur = table[s][k] + table[k][dest_a] + table[k][dest_b]
        min_common_fare = min(min_common_fare, cur)

    independet_fare = table[s][dest_a] + table[s][dest_b]

    return min(min_common_fare, independet_fare)
```