# 시간 
- 1시간(시간초과)

# 풀이
- dfs 로 풀었다.. 왜 나만 시간초과가 나는지 모르겠다.

# 코드
```python
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

ones = []
twos = []
visited = [False] * 2500
selected_twos = []
temp = []
ans = 10e10

for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 1:
            ones.append((r,c))
        elif row[c] == 2:
            twos.append((r,c))

def calculate(selected_twos):
    return sum([ min( [abs(r1-r0) + abs(c1-c0) for (r1, c1) in selected_twos]) for (r0, c0) in ones]) 


def dfs(depth):
    global ans
    if depth == M:
        temp.append(calculate(selected_twos))
        return
    for i, two in enumerate(twos):
        if not visited[i]:
            visited[i] = True
            selected_twos.append(two)
            dfs(depth+1)
            selected_twos.pop()
            visited[i] = False

dfs(0)

print(min(temp))
```