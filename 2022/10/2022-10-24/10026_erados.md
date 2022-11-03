## 풀이

for 문의 변수 이름을 코드에서 재정의해서 문제가 생겼었다.
그리고 메모리 초과와 시간초과도 발생했었는데
visited 를 dictionary 로 바꾸어서 해결했다.

## 코드
```python
import sys

input = sys.stdin.readline
N = int(input())

graph = []
to_visit = []
visited = [[False] * N for _ in range(N)]
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
color_map = {"R": ["R", "G"], "G": ["R", "G"], "B": ["B"]}

# 그래프 초기화
for _ in range(N):
    graph.append(list(input().rstrip()))

count = 0
# 모든 Cell 을 둘러볼건데
for y in range(N):
    for x in range(N):
        # 첫 방문이라면 Count 를 증가시키고 아래 로직을 실행한다.
        if not visited[y][x]:
            to_visit.append((y, x))
            count += 1
        while to_visit:
            target = to_visit.pop()
            _y = target[0]
            _x = target[1]
            visited[_y][_x] = True
            # 내 위치 기준으로 주위를 찔러보는데
            for move in moves:
                ny = move[0] + _y
                nx = move[1] + _x
                if 0 <= ny < N and 0 <= nx < N:
                    if not visited[ny][nx]:
                        # 색이 같다면 탐사 계속
                        if graph[ny][nx] == graph[_y][_x]:
                            to_visit.append((ny, nx))
                        # 색이 다르면 pass
                        else:
                            pass

print(count, end=" ")

count = 0
visited = [[False] * N for _ in range(N)]
# 모든 Cell 을 둘러볼건데
for y in range(N):
    for x in range(N):
        # 첫 방문이라면 Count 를 증가시키고 아래 로직을 실행한다.
        if not visited[y][x]:
            to_visit.append((y, x))
            count += 1
        while to_visit:
            target = to_visit.pop()
            _y = target[0]
            _x = target[1]
            visited[_y][_x] = True
            # 내 위치 기준으로 주위를 찔러보는데
            for move in moves:
                ny = move[0] + _y
                nx = move[1] + _x
                if 0 <= ny < N and 0 <= nx < N:
                    if not visited[ny][nx]:
                        # 색이 같다면 탐사 계속
                        if graph[ny][nx] in color_map[graph[_y][_x]]:
                            to_visit.append((ny, nx))
                        # 색이 다르면 pass
                        else:
                            pass


print(count)

```