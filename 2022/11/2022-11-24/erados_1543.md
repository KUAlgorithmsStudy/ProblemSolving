# 풀이
브루트포스로 풀었다.


# 코드
```python
import sys

input = sys.stdin.readline


a = input().rstrip()
b = input().rstrip()

l_a = len(a)
l_b = len(b)

i = 0
ans = 0

while i < l_a:
    if a[i : i + len(b)] == b:
        i += len(b)
        ans += 1
    else:
        i += 1

print(ans)

```