# 풀이
2시간 걸렸다.
스택 안쓰고 for 문 중첩했다가 시간초과 걸리고
스택 썼는데 어떻게 쓰는지 잘 몰라서 계속 틀리고..
O(N^2) -> O(N) 이 되어 신기하다.

# 코드
```python
from collections import deque
import sys


input = sys.stdin.readline

N = int(input())
origin = deque(enumerate(list(map(int, input().split()))))
temp = [origin.popleft()]
answer = ["-1"] * N
while temp and origin:
    t_idx, target = origin.popleft()
    c_idx, curr = temp.pop()
    if target <= curr:
        temp.append((c_idx, curr))
        temp.append((t_idx, target))
    else:
        while target > curr:
            answer[c_idx] = str(target)
            if not temp:
                break
            c_idx, curr = temp.pop()
        if target <= curr:
            temp.append((c_idx, curr))
        temp.append((t_idx, target))

print(" ".join(answer))
```