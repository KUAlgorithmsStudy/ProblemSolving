# 풀이
재귀로 풀었다. base case 를 따로 빼고 일반적인 case 를 계산하였다.

# 코드
```python
import sys

input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    row = [c for c in input().rstrip()]
    graph.append(row)


def compress(col, row, size):
    ans = ""
    temp = ""

    if size == 2:
        for r in range(row, row + size):
            for c in range(col, col + size):
                temp += graph[r][c]
        if temp == "0000":
            return "0"
        elif temp == "1111":
            return "1"

    else:
        temp = (
            compress(col, row, size // 2)
            + compress(col + size // 2, row, size // 2)
            + compress(col, row + size // 2, size // 2)
            + compress(col + size // 2, row + size // 2, size // 2)
        )

        if temp == "0000":
            return "0"
        elif temp == "1111":
            return "1"

    return "(" + temp + ")"


print(compress(0, 0, N))
```