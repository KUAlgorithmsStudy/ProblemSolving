# 2022-09-22

# 백준 1018 체스판다시칠하기

# 1시간 - 유형 BruteForce

# 코드 - Python

```python
from collections import defaultdict, deque
global ans,g

n,m = map(int,input().split())
g = [input() for _ in range(n)]
INF = int(3e9)
ans = INF
def changeCol(col): return ('B' if col == 'W' else 'W')
def check(color,counterpart, y,x):
    global ans,g
    ret = 0
    for i in range(8):
        for j in range(8):
            if ret>ans: return
            if (i+j)%2 == 0: 
                if g[y+i][x+j] != color: ret+=1
            else: 
                if g[y+i][x+j] != counterpart: ret+=1
    ans = min(ans,ret)
    

for y in range(0,n-7):
    for x in range(0,m-7):
        check('B','W',y,x)
        check('W','B',y,x)
        if ans == 0: print(0);exit(0)
print(ans)

```

# 풀이

(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)

2차원 배열의 인덱스가 다음과 같은 경우 
대각선으로 이어진 칸들은  ( index1+index2 ) % 2 == 0 인것을 알 수 있습니다.
이와 같은 원리를 활용하여 해결했습니다.

