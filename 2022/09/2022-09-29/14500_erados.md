# 시간
- 40분

# 풀이
- brute force 로 풀었다. 채점하는데 시간이 오래걸리는 걸 보니 더 빠르게 풀 수 있는 방법이 있을 것 같다.

# 코드
```python
import sys

input = sys.stdin.readline

tetrominos = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅣ
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅡ
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
    [(1, 0), (1, 1), (1, 2), (0, 2)],  # ㄱ
    [(0, 0), (0, 1), (0, 2), (1, 0)],  # ㄱ
    [(1, 0), (0, 0), (1, 1), (1, 2)],  # ㄱ
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # ㄱ
    [(0, 1), (1, 1), (2, 1), (2, 0)],  # ㄱ
    [(0, 1), (1, 1), (2, 1), (0, 0)],  # ㄱ
    [(0, 0), (1, 0), (2, 0), (0, 1)],  # ㄱ
    [(0, 0), (0, 1), (1, 1), (1, 2)],  # ㄹ
    [(1, 0), (1, 1), (0, 1), (0, 2)],  # ㄹ
    [(1, 0), (2, 0), (1, 1), (0, 1)],  # ㄹ
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # ㄹ
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅜ
    [(0, 1), (1, 1), (2, 1), (1, 0)],  # ㅗ
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅏ
    [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅓ
]

graph = []
N, M = map(int, input().split())
ans = 0


def cal(x, y):
    local_ans = 0
    for tetromino in tetrominos:
        temp = 0
        for cord in tetromino:
            nx = x + cord[0]
            ny = y + cord[1]
            if nx < M and ny < N:
                temp += graph[ny][nx]
            else:
                break
        local_ans = max(temp, local_ans)
    return local_ans


for _ in range(N):
    graph.append(list(map(int, input().split())))

for y in range(N):
    for x in range(M):
        ans = max(cal(x, y), ans)
print(ans)

```