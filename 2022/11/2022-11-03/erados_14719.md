# 풀이
스택으로 풀었다.
스택에 무조건 넣고 값이 전보다 커지는 경우에 그 값보다 스택의 top 값이 커질 때까지 pop 하면서 차있는 빗물을 구한다.
# 코드
```python
import sys

input = sys.stdin.readline

H, W = map(int, input().split())
ans = 0
stack = []
for idx, height in enumerate(map(int, input().split())):
    while stack and height > stack[-1][1]:
        top = stack.pop()
        if stack:
            ans += (idx - 1 - stack[-1][0]) * (min(stack[-1][1], height) - top[1])

    stack.append((idx, height))

print(ans)

```