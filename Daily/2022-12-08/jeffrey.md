## 선분덮기

```python
from collections import deque

M = int(input())
lines = []
while True:
    L, R = map(int, input().split())
    if (L, R) == (0, 0):
        break

    L = max(L, 0)
    R = min(R, M)
    if L < R:
        lines.append((L, R))


def sol1(lines):

    answer = 0
    st = 0
    max_R = 0

    while lines:
        # st >= L 을 만족하는 것들 중 가장 긴놈이 어떤건지 알아봐야 함
        L, R = lines.popleft()

        if st < L:
            continue

        max_R = max(max_R, R)
        while lines and lines[0][0] <= st:  # 안빠질수도 있음.
            L, R = lines.popleft()
            max_R = max(max_R, R)

        st = max_R
        answer += 1

        if st >= M:
            return answer
    
    else:
        return 0
    
lines.sort()
print(sol1(deque(lines)))
```