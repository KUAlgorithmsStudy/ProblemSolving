# 2022-09-17

# 백준 13460 구슬탈출

# 50분 - 유형 BFS/Simulation

# 코드 - Python

```python
from collections import defaultdict,deque
global n,m, g
n,m = map(int,input().split())
g = [list(input()) for _ in range(n)]
visit = defaultdict(list)

sry,srx,sby,sbx = 0,0,0,0
for y in range(n):
    for x in range(m):
        if g[y][x] == 'B': 
            sby,sbx = y,x
            g[y][x] = '.'
        elif g[y][x] == 'R': 
            sry,srx = y,x
            g[y][x] = '.'
visit[(sry,srx,sby,sbx )] = 1
dir = [(1,0),(-1,0),(0,1),(0,-1)]
direct = [ [2,3], [2,3], [0,1], [0,1], [0,1,2,3] ]
q = deque([(1,4,sry,srx,sby,sbx)])

def playball(d,sy,sx):
    global n,m, g
    y,x = sy,sx
    ret = 0
    
    while g[ y+dir[d][0] ][ x+dir[d][1] ] != '#'  and g[y][x] != 'O'  :
        y,x = y+dir[d][0],x+dir[d][1]
        ret += 1
    if g[y][x] == 'O': return -1,-1, ret
    else : return y, x, ret

def play(d, cnt, ry, rx, by, bx ):
    global n,m, g
    nry,nrx,rcnt = playball(d,ry,rx)
    nby,nbx,bcnt = playball(d,by,bx)
    if nry==-1 and nby>-1: print(cnt);exit(0)

    if nry>-1 and nry == nby and nrx == nbx :
        if rcnt>bcnt: nry -=dir[d][0]; nrx -= dir[d][1]
        else: nby -=dir[d][0]; nbx -= dir[d][1]
    return nry,nrx,nby,nbx

while q:
    cnt,pre,ry,rx,by,bx = q.popleft()
    if cnt>=11: continue
    for d in direct[pre]:
        nry,nrx, nby, nbx = play(d, cnt, ry, rx, by, bx )
        if nry == -1 and nrx == -1 and nby == -1 and nbx == -1: continue
        if visit[(nry,nrx,nby,nbx )] : continue
        visit[(nry,nrx,nby,nbx )] = 1
        q.append((cnt+1, d, nry,nrx, nby,nbx))

print(-1)            
```

# 풀이
BFS 문제이었습니다.
평소와 다르게 2차원 배열로 표현된 지도상에 존재하는
빨간 구슬과 파란 구슬의 좌표를 대상으로 탐색(BFS)을 했습니다.
구슬 이동 구현이 어려웠습니다.
구슬을 모두 굴린 후
파란 구슬과 빨간 구슬이 겹쳐졌을때,
각각 이번 회차에서 이동한 칸수를 비교해서 
더 많은 칸을 이동한 구슬을 한칸 덜 이동하도록
구현해주면 조금 더 쉽게 구슬 굴리는 행위를 구현할 수 있습니다.