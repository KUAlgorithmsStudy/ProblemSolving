# 풀이
처음엔 막 if 로 분기 엄청 만들었는데, 양수 음수 나누어 저장하는게 효율적일 것 같아서 나눠서 풀었다.

# 코드
```python
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
pos = []
neg = []
sum = 0

N = int(input())


for _ in range(N):
    num = int(input())
    if num > 0:
        heappush(pos, (-num, num))
    else:
        heappush(neg, (num, num))

while len(pos) > 1:
    _, a = heappop(pos)
    _, b = heappop(pos)
    if a == 1 or b == 1:
        sum += a + b
    else:
        sum += a * b

while len(neg) > 1:
    _, a = heappop(neg)
    _, b = heappop(neg)
    sum += a * b

if pos:
    sum += pos[0][1]
if neg:
    sum += neg[0][1]

print(sum)
```