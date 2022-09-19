# 시간 1시간 ?

# 풀이

진짜 구현 문제다.
처음엔 8진수인가? 비트마스킹인가? 했는데 그냥 구현 문제였다.

# 코드
```python
import sys
input = sys.stdin.readline

def shift(gear, direction):
    direction = direction * -1
    return gear[direction:]+gear[:direction]

T = int(input())
gears = [[]]
gears.extend([ input().rstrip() for _ in range(T)])

left = 0
right = 0

K = int(input())
for _ in range(K):
    N, D = map(int, input().split())
    right = gears[N][2]
    left = gears[N][6]
    gears[N] = shift(gears[N], D)
    cnt = 1
    for i in range(N+1, T+1):
        if gears[i][6] != right:
            right = gears[i][2]
            gears[i] = shift(gears[i], D * (-1)**cnt)
            cnt += 1
        else:
            break
    cnt = 1
    for j in range(N-1, 0, -1):
        if gears[j][2] != left:
            left = gears[j][6]
            gears[j] = shift(gears[j], D * (-1)**cnt)
            cnt += 1
        else:
            break
print([gear[0] for gear in gears[1:]].count('1'))
```