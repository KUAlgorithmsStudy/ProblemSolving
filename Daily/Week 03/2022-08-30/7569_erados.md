# 퓰이
처음엔 sum 중첩으로 0이 있는지를 구했는데 이건 평균 시간 복잡도가 for 문 보다 오래 걸려서 시간초과가 났다.
target 의 time 을 그대로 출력하는 부분이 참 잘 짜인 것 같다.

# 코드
```python
from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

tomatos = [[list(map(int, input().split())) for n in range(N)] for h in range(H)]

moves = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

to_visit = deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatos[h][n][m] == 1:
                to_visit.append((m, n, h, 0))

while to_visit:
    target = to_visit.popleft()
    m, n, h, time = target
    for move in moves:
        nm = m + move[0]
        nn = n + move[1]
        nh = h + move[2]
        ntime = time + 1
        if 0 <= nm < M and 0 <= nn < N and 0 <= nh < H:
            if tomatos[nh][nn][nm] == 0:
                tomatos[nh][nn][nm] = 1
                to_visit.append((nm, nn, nh, ntime))


for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatos[h][n][m] == 0:
                print(-1)
                exit()
else:
    print(time)
```