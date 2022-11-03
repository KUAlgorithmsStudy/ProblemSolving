# 2022-10-06

# 백준 1194

# 20분

# Algorithms & Datastructures - BFS

# 코드 - Python

```python
from collections import defaultdict, deque
import heapq as hq

n, m = map(int, input().split())

g =[ list(input() ) for _ in range(n) ]
visit = [ [deque() for _ in range(m)] for _ in range(n) ]
q = deque()
for y in range(n):
    for x in range(m):
        if g[y][x] == '0':
            q.append((0,y,x,0))
            visit[y][x].append(0)
dir = [(0,1), (1,0),(-1,0),(0,-1)]
Aord, Zord = ord('A'), ord('Z')
aord, zord = ord('a'), ord('z')
while q:
    cnt, y, x, keys = q.popleft()
    if cnt+1 == (n*m)**2: continue
    for d in dir:
        ny, nx = y+d[0], x+d[1]
        if ny<0 or nx<0 or ny>= n or nx>=m: continue
        if g[ny][nx] == '#' or (Aord<= ord(g[ny][nx]) <= Zord and keys & (1<<ord(g[ny][nx].lower())-aord) ==0 ): continue
        if g[ny][nx] == '1': print(cnt+1); exit(0)
        if keys in visit[ny][nx]: continue
        visit[ny][nx].append(keys)
        if aord <= ord(g[ny][nx]) <= zord: q.append( (cnt+1, ny, nx, keys| 1<< (ord(g[ny][nx]) - aord ) ) )
        else: q.append( (cnt+1, ny, nx, keys) )
print(-1)
```

# 풀이

특정 위치를 방문할때 이전에 방문 했던 위치(노드) 이더라도 저번과 가지고 있는 열쇠가 다르다면 재방문할 수 있습니다.
