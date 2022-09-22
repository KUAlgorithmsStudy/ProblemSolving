# 2022-09-21

# 백준 2206 벽부수고 이동하기

# 1시간 - 유형 BFS+DP

# 코드 - Python

```python
from collections import defaultdict,deque
global n,m,g
n,m = map(int ,input().split())
g = [input() for _ in range(n)]
INF = int(3e9)
dir = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs(sy,sx):
    global n,m,g
    v = [[[0]*2 for _ in range(m)] for _ in range(n)]
    v[sy][sx][0] = 1
    q = deque([(sy,sx,0)])
    while q:
        y,x,bomb = q.popleft()
        if y==n-1 and x == m-1: return v[y][x][bomb]
        for d in dir:
            ny,nx = y+d[0], x+d[1]
            if ny<0 or nx<0 or ny>=n or nx>=m: continue

            if g[ny][nx] == '1' and bomb == 0:
                v[ny][nx][1] = v[y][x][0]+1
                q.append((ny,nx,1))
            elif g[ny][nx] == '0' and v[ny][nx][bomb] == 0:
                v[ny][nx][bomb] = v[y][x][bomb]+1
                q.append((ny,nx,bomb))
    return -1
print(bfs(0,0))

```

# 풀이

BFS 와 DP로 해결했습니다.
벽을 부수고 이동한 경우, 벽을 부수지 않고 이동한 경우의 탐색 횟수를 저장한 메모리를 따로 관리하여 BFS를 해주면 됩니다.
탐색 중 벽을 만났을 때, 벽부수기를 이미 했으면 지금 진행하던 탐색을 멈추고 Queue에 들어있는 다음 노드의 탐색을 진행해주면 됩니다.
지금까지 탐색한 노드의 갯수는
벽부수기를 이미 사용했을때와 하지 않았을때로 따로 저장해주면 됩니다.
