# 시간
- 1시간 (시간초과)

# 풀이
- bfs 를 사용하였고 queue 에 x, y, 거리, 벽을 부쉈는지 여부 를 기록했습니다.
- 주의할 점은 벽을 안 부순 케이스와 부순 케이스가 같은 좌표에서 나타날 수 있다는 건데
- 이 케이스를 핸들링 하기 위해 visited 리스트에 튜플로 벽을 부쉈는지 안 부쉈는지를 기록합니다. 
- 시간초과를 해결하기위해 이 예외처리 부분을 조금 더 손볼 수 있을 것 같습니다.

# 코드
```python
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

graph = [[int(c) for c in input().rstrip()] for _ in range (N)]
visited = [[(False,0) for i in range(M)] for j in range(N)]
visited[0][0] = (True, 0)
moves = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs():
    queue = [(0,0,1,0)] # (x,y,distance,bomb)
    while len(queue) > 0:
        target = queue.pop(0)
        if target[0:2] == (M-1, N-1):
            return target[2]
        for move in moves:
            nx = target[0] + move[0]
            ny = target[1] + move[1]
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] != (True, 0) :
                bomb = target[3]
                if graph[ny][nx]:
                    if bomb:
                        continue
                    else:
                        bomb = bomb + 1
                new_target = (nx, ny, target[2]+1, bomb)
                if new_target not in queue:
                    queue.append(new_target)
                    visited[ny][nx] = (True, bomb)

    return -1 

print(bfs())
```