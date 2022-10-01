# 시간
- 10분

# 풀이
- 각 과제에 대한 정보를 튜플로 만들어 어레이에 저장하고
- 내림 차순으로 정렬 뒤, 한 번 순회하면서 제일 처음 연속으로 쉬는 날짜를 구했다.


# 코드
```python
import sys

input = sys.stdin.readline

N = int(input())
temp = []
for _ in range(N):
    d, t = map(int, input().split())
    temp.append((t, d))
temp.sort(reverse=True)

ans = 10e9
for item in temp:
    t, d = item
    ans = min(t, ans) - d

print(ans)

```