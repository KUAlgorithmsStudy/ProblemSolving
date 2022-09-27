# 시간 
- 10분

# 풀이
- DP 를 사용해서 풀었습니다.

# 코드
```python
import sys
input = sys.stdin.readline

N = int(input())

small = [0, 0, 0]
big = [0, 0, 0]

for _ in range(N):
    temp = list(map(int, input().split()))
    small = [min(small[0], small[1]) + temp[0], min(small) + temp[1], min(small[1], small[2]) + temp[2]]
    big = [max(big[0], big[1]) + temp[0], max(big) + temp[1], max(big[1], big[2]) + temp[2]]

print(max(big), min(small))
```