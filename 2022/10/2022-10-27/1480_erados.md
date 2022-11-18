# 풀이
비트마스킹을 사용해서 이전 가방에 넣은 보석은 고려하지 않도록했다.
dp로 풀었는데 실패했다.


# 코드
```python
import sys
from pprint import pprint

input = sys.stdin.readline

N, M, C = map(int, input().split())
weights = [0] + list(map(int, input().split()))

# dp[가방 인덱스 + 1][보석 인덱스 + 1][가방 용량] = (보석 인덱스+1  bin, 총 무게)
dp = [[[(0, 0)] * (C + 1) for n in range(N + 1)] for m in range(M + 1)]

for m in range(1, M + 1):
    last_back_b, last_back_w = dp[m - 1][N][C]
    for n in range(1, N + 1):
        for c in range(1, C + 1):
            # n 번째 보석을 아직 안 챙겼고 가방에 담을 수 있는 사이즈면
            if (not (last_back_b & (1 << n))) and weights[n] <= c:
                # 함 넣어본다.
                prev_b, prev_w = dp[m][n - 1][c - weights[n]]
                new_b = prev_b | (1 << n)
                new_w = weights[n] + prev_w
                # 무게 많이 드는 쪽으로 넣는다. << 여기가 잘못된 듯
                dp[m][n][c] = max((new_b, new_w), dp[m][n - 1][c], key=lambda a: a[1])

            # 못 담으면 이전 값을 이어나간다.
            else:
                dp[m][n][c] = dp[m][n - 1][c]

# pprint(dp, width=200)

b = 0
for m in range(1, M + 1):
    b |= dp[m][N][C][0]
print(bin(b).count("1"))

```