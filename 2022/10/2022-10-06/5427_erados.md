# 풀이 (실패)
- 각 불의 위치를 저장해두고 상하좌우로 번지게 하고
- 상근이의 위치를 DPS 로 이동하면서 불을 피하게 하려고 했다.
- 시간이 없어서 다 못 짰다.
- 그리고 좀 깨끗하게 다시 짜야할 것 같다.

# 코드
```python
import sys

input = sys.stdin.readline

N = int(input())
fires = []
burned = []
character = (0, 0)
moves = [(0, 1), (0, -1), (1, 0), (1, -1)]


def solve(graph):
    queue = [character]
    time = 0
    while character[0] not in [0, H - 1] and character[1] not in [W - 1, 0]:
        new_fires = []
        for fire in fires:
            y, x = fire
            for move in moves:
                burned.append((y, x))
                new_fires.append((y + move[0], x + move[1]))
        fires = new_fires

        for move in moves:
            y, x = character
            ny = y + move[0]
            nx = x + move[1]
            if (
                (ny, nx) not in burned
                and (ny, nx) not in fires
                and graph[ny][nx] != "#"
            ):
                queue.append((ny, nx))
        time += 1
    print(time)


for _ in range(N):
    W, H = map(int, input().split())
    graph = [["#"] * W for _ in range(H)]
    for h in range(H):
        graph[h] = [c for c in input().rstrip()]
        for w in range(W):
            if graph[h][w] == "@":
                character = (w, h)
            elif graph[h][w] == "*":
                fires.append((w, h))
    solve(graph)

"""
'.': 빈 공간
'#': 벽
'@': 상근이의 시작 위치
'*': 불
"""

```