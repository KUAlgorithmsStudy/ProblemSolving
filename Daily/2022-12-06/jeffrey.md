# 두 배열의 합
https://www.acmicpc.net/problem/2143

```python
from collections import defaultdict


T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# build A_SUM
prefix_sum_A = defaultdict(int)

for left in range(n):
    cum_sum = 0
    for right in range(left, n):
        cum_sum += A[right]
        prefix_sum_A[cum_sum] += 1

# build B_SUM
prefix_sum_B = defaultdict(int)

for left in range(m):
    cum_sum = 0
    for right in range(left, m):
        cum_sum += B[right]
        prefix_sum_B[cum_sum] += 1

# iterate A_SUM X B_SUM
answer = 0
for key in prefix_sum_A.keys():
    # print(key, prefix_sum_A[key], prefix_sum_B[T - key], prefix_sum_A[key] * prefix_sum_B[T - key])
    answer += prefix_sum_A[key] * prefix_sum_B[T - key]

print(answer)
```