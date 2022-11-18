# 풀이
- 처음에는 나머지 연산으로 처리했는데 그것보다 에라토스테네스의 체가 훨씬 빨랐다.
- 난이도에 비해 쉬운 문제.

# 코드
```python
from math import floor
import sys

input = sys.stdin.readline

_min, _max = map(int, input().split())

filtered = [False] * (_max - _min + 1)
ans = _max - _min + 1

i = 2
while i * i <= _max:
    i_sq = i * i
    j = 0
    start = floor(_min / i_sq)
    while (start + j) * i_sq <= _max:
        index = (start + j) * i_sq - _min
        if index >= 0 and not filtered[index]:
            filtered[index] = True
            ans -= 1
        j += 1
    i += 1

print(ans)

```