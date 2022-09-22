# 2022-09-12

# 백준 1911 흙길 보수하기

# 60분 - 유형 Sweeping

# 코드 - Python

```python
from collections import defaultdict, deque
n, l = map(int, input().split())
e,ans = 0,0
arr = []
for i in range(n) : arr.append( [*map(int, input().split())] )
arr.sort()

for i, ll in enumerate(arr):
    if ll[1] <= e : continue
    if e < ll[0]:
        cnt = (ll[1] - ll[0]) // l + ( 1 if (ll[1] - ll[0]) % l  else 0 )
        ans += cnt
        e = ll[0]+cnt*l
    else:
        cnt = (ll[1] - e) // l +  ( 1 if (ll[1] - e) % l  else 0 )
        ans += cnt
        e = e+cnt*l

print(ans)
```

# 풀이
