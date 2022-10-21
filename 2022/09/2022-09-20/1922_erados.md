# 시간 
- 풀다가 잠

# 풀이
cycle 을 어떻게 체크할 지 누워서 생각하다가 자버림..

# 코드
```python
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

visited = [False] * (N + 1)
lines = []

for _ in range(M):
    lines.append(list(map(int,input().split())))
lines.sort(key=lambda a:a[2])

print(lines)

while False in visited:
    
```