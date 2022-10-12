# 풀이 (실패)
graph[i][j] 가 num[i:j] 만큼의 파일을 만드는 데에 드는 최소 비용 으로 놓고 풀면 된다는 정보를 컨닝을 통해 찾아 풀이를 시도했으나 실패함.

# 코드
```python
import sys
import pprint

input = sys.stdin.readline

T = int(input())


def solve():
    N = int(input())
    graph = [[0] * N for _ in range(N)]
    nums = list(map(int, input().split()))

    for i in range(N):
        graph[i][i] = nums[i]

    for diff in range(1, N):
        for y in range(N):
            x = y + diff
            if x < N:
                graph[y][x] = (
                    min(graph[y][x - 1] + nums[x], graph[y + 1][x] + nums[y])
                    if diff == 1
                    else min(
                        2 * graph[y][x - 1] + nums[x], 2 * graph[y + 1][x] + nums[y]
                    )
                )
    print(graph[0][N - 1])
    pprint.pprint(graph)


for _ in range(T):
    solve()

```