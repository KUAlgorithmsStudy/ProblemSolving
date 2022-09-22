# 2022-09-16

# 백준 4485 녹색 옷 입은 애가 젤다지? 

# 30분 - 유형 BFS

# 코드 - Python

```python
from collections import defaultdict,deque
import  sys; sys.setrecursionlimit(5000) 
input = sys.stdin.readline
global n,g,ans,v
t = 0

dir = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs():
    global n,g,ans
    q = deque([(0,0,g[0][0])])
    while q:
        y,x,total = q.popleft()
        if y == n-1 and x == n-1: ans = min(ans, total); continue       
        for d in dir:
            ny,nx = d[0]+y,d[1]+x
            if ny<0 or nx<0 or ny>=n or nx>=n: continue
            if visit[ny][nx]>-1 and visit[ny][nx]<= total+g[ny][nx]: continue

            visit[ny][nx] = g[ny][nx]+total
            q.append((ny,nx,g[ny][nx]+total))

while True:
    n = int(input().rstrip())
    if n == 0: break
    ans = float('inf')
    t += 1
    g = [[*map(int, input().split())] for _ in range(n)]
    visit = [[-1]*n for _ in range(n)]
    visit[0][0] = g[0][0]

    bfs()
    print("Problem {0}: {1}".format(t,ans) )

```

# 풀이
BFS 문제이었습니다.
문제는 통과했지만 연산 시간을 더 줄이는 풀이를 연구해보아야겠습니다.