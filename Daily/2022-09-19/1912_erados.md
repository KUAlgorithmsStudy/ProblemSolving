# 시간 18분

# 풀이
STARE 하니 풀이가 보였다. 진짜로..;;;

# 코드
```python
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

candidates = [data[0]]

for i in range(1, n):
    candidates.append(max(candidates[i-1]+data[i], data[i]))

print(max(candidates))
```