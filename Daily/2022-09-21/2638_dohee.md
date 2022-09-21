# 2022-09-21

# 백준 2638 치즈

# 20분 - 유형 BFS

# 코드 - Python

```python
from collections import defaultdict,deque

n,m = map(int,input().split())
g = [[*map(int,input().split())] for _ in range(n)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(g):
    sy,sx = 0,0
    visit = [[0]*m for _ in range(n)]
    se = set()
    q = deque([(0,0)])
    visit[0][0] = True
    ret = True
    while q:
        y,x = q.popleft()
        for d in dir:
            ny,nx = y+d[0], x+d[1]
            if ny<0 or nx<0 or ny>=n or nx>=m: continue
            if g[ny][nx] :
                visit[ny][nx] += 1;
                if visit[ny][nx]>=2: se.add((ny,nx)); ret = False
            if visit[ny][nx]: continue
            visit[ny][nx] += 1
            if g[ny][nx] == 0: q.append((ny,nx))
    for l in se : g[l[0]][l[1]] -= 1
    return ret

for i in range(n*m):
    if bfs(g): print(i);exit(0)

```

# 풀이

BFS 문제 입니다.
BFS 로직에서 추가적으로 변형한 사항을 요약하여 정리하자면,
(1) 2차원 배열의 테두리 부분이 항상 비어있는 것을 이용하여 (0,0)을 Q에 넣어 BFS를 시작합니다.
(2) 치즈인 칸은 탐색을 하게 될때마다 visit배열에 방문횟수를 갱신해주고, 방문횟수가 2 이상인 경우에 set에 해당 좌표를 추가해줍니다.
(3)
set이 비어있다면, 시간을 출력하고 프로그램을 꽅내고
비어있지 않다면, 치즈를 녹여주고 시간을 갱신해준 후 BFS를 다시 반복합니다.
시간복잡도는 O(n+e)입니다.
