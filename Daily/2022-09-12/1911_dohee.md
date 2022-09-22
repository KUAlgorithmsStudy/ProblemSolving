# 2022-09-10

# 백준 12100 2048EASY

# 60분 - 유형 Simulation

# 코드 - Python

```python
# 2048(EASY) 26 분
from collections import defaultdict,deque
from copy import deepcopy

global n,ans,biggest

n = int(input().rstrip())
g = [[*map(int,input().split())] for _ in range(n)]
ans,biggest = 0,0
for i in g: ans = max(ans,max(i))

def rotate90(g):
    global n, ans, biggest
    gg = deepcopy(g)
    for y in range(n):
        for x in range(n):g[x][n-1-y] = gg[y][x]
    return g

def play(arr):
    global n, ans, biggest
    flag = True
    neww = []
    for i in arr:
        if i :
            if neww :
                if flag and neww[-1]==i :
                    neww[-1]*=2 ; flag = False
                    biggest = max(neww[-1], biggest)
                else: neww.append(i); flag=True
            else : neww.append(i)

    return neww + [0]*(n-len(neww))


def bt(cnt,g,maxi):
    global n, ans, biggest
    if cnt == 5 : ans = max(ans,maxi); return
    elif cnt < 5 :
        for d in range(4):
            biggest = maxi
            gg = [ play(arr) for arr in g]
            if gg!= g: bt(cnt+1, gg, biggest)
            if d<3: g = rotate90(g)
bt(0,g,ans)
print(ans)
```

# 풀이
