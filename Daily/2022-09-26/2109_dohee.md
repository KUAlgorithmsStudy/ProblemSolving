# 2022-09-26

# 백준 2109

# 60분 - 순회강연

# 코드 - Python

```python
from collections import defaultdict, deque
import heapq as hq

n = int(input().rstrip())
arr = []
for _ in range(n):
    p, d = map(int ,input().split())
    arr.append((d, p))
arr.sort()
ans = []
for l in arr:
    hq.heappush(ans, l[1])
    if len(ans) > l[0] : hq.heappop( ans )

print( sum(ans) )
```

# 풀이

greedy 와 heap을 활용하여 문제를 해결 할 수 있습니다.
d를 기준으로 오름차순 정렬한 후
heap에 p를 모두 넣어주고 heap에 저장된 원소의 개수가 지금 확인하고 있는 대학의 d보다 작을때
heap에서 삭제를 진행해주면 됩니다.
( 해당 힙이 최소힙일때 삭제를 시행하면 지금 원소중 최소값이 삭제됩니다. )
d를 기준으로 오름차순 정렬했기에
