# 시간
- 30분 이상

# 풀이
- 원래 index 메소드 썼다가 시간초과 떠서 dictionary 로 바꿨다.
- list 의 index 메소드는 O(n), dict 는 O(1) 이다.
- 이거 참 중요한 것 같다.

# 코드
```python
import sys

input = sys.stdin.readline

N = int(input())

temp = list(map(int, input().split()))
sorted_temp = sorted(list(set(temp)))
dict_temp = {}

for i in range(len(sorted_temp)):
    dict_temp[sorted_temp[i]] = i

print(" ".join([str(dict_temp[i]) for i in temp]))

```