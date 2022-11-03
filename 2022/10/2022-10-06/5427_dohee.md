# 2022-10-06

# 백준 5427

# 40분

# Algorithms & Datastructures - BFS

# 코드 - Python

```python
from collections import defaultdict, deque
dir = [(0,1),(1,0),(-1,0),(0,-1)]
def bfs(gg, r, c):
    time = 0
    q = deque()
    fq = deque()
    for y in range(r):
        for x in range(c):
            if gg[y][x] == '@': q.append((0,y,x))
            elif gg[y][x] == '*': fq.append((0,y,x))
    while q:
        time += 1
        while fq and time > fq[0][0] :
            ft, y,x = fq.popleft()
            for d in dir:
                ny, nx = y+d[0], x+d[1]
                if ny<0 or nx<0 or ny>=r or nx>=c: continue
                if gg[ny][nx] == '#'  or gg[ny][nx] == '*': continue
                gg[ny][nx] = '*'
                fq.append((ft+1, ny,nx))
        while q and time > q[0][0]:
            cnt, y, x = q.popleft()
            for d in dir:
                ny, nx = y+d[0], x+d[1]
                if ny<0 or nx<0 or ny>=r or nx>= c: return time
                if gg[ny][nx] == '#' or gg[ny][nx] == '@' or gg[ny][nx] == '*': continue
                if gg[ny][nx] == '.':
                    gg[ny][nx] = '@'
                    q.append((cnt+1, ny, nx))
    return -1

t = int(input())
for tt in range(t):
    w, h = map(int ,input().split())
    g = [ list(input()) for _ in range(h)]
    res = bfs(g, h, w)
    if res == -1: print('IMPOSSIBLE')
    else: print(res)
```

# 풀이

특정 조건이 추가된 BFS입니다.
