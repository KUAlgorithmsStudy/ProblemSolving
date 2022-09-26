# 2022-09-26

# 백준 9935

# 20분 - 유형 문자열 폭발

# 코드 - Python

```python
from collections import defaultdict, deque

arr = []
l = list( input() )
bomb = list(input())
n = len(bomb)

for s in l:
    arr.append(s)

    while len(arr)>=n :
        if arr[len(arr)-n:] == bomb:
            for _ in range(n): arr.pop()
        else: break

if arr : print(*arr, sep="")
else : print('FRULA')
```

# 풀이

stack 자료구조(LIFO)를 활용하는 문제이었습니다.
스택에 새로운 문자를 push 한후
슬라이싱을 이용하여 동일 단어를 판별하고
폭발 문자열이면, 폭발문자열이 남아있지 않을 때까지 pop을 진행해줍니다.
