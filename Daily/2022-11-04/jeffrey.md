"""
시뮬레이션 + dfs (두 개 쪼개진거 체크)

주의점
1. 끝까지 분리 안되면 0 출력


어려웠던 점 :
1. 처음부터 둘로 나뉘어진 경우를 생각 못함
2. 이상한 생각으로 (i,j) 를 key 로 하면 되는데 str(i)+str(j) 로 했다가 12+9 == 1+29 같은 상황을 마주함.
"""

```python
from collections import deque

def sol1(N, M, board):
    cnt = 0
    R = len(board)
    C = len(board[0])

    ice_list = []
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                ice_list.append((i, j, board[i][j]))


    while True:
        # check split
        # print(f"check split : {ice_list}")
        if ice_list:
            queue = deque([ice_list[0]])
        else:
            return 0
            
        visited = {(ice_list[0][0],ice_list[0][1]):True}

        while queue:
            i,j,_ = queue.popleft()

            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 0 and (ni, nj) not in visited:
                    visited[(ni,nj)] = True
                    queue.append((ni,nj,board[ni][nj]))

        if len(visited) != len(ice_list):
            # print("num diff", visited, ice_list)
            break

        cnt += 1
        next_ice_list = []
        # print(ice_list)

        # simulation
        for ice in ice_list:
            i, j, v = ice
            sea = 0
            if i-1 >=0 and board[i-1][j] == 0:
                sea += 1
            if j+1 < C and board[i][j+1] == 0:
                sea += 1
            if j-1>=0 and board[i][j-1] == 0:
                sea += 1
            if i+1 < R and board[i+1][j] == 0:
                sea += 1

            remain = max(0, v - sea)
            # if remain != 0:
            next_ice_list.append((i,j,remain))

        ice_list = []
        for ice in next_ice_list:
            i, j, v = ice
            board[i][j] = v
            if v!= 0:
                ice_list.append((i,j,v))
        
        if not ice_list:
            cnt=0
            break

    return cnt

N, M = map(int, input().split())
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
print(sol1(N,M,board))
```

```python
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):

    # n을 k진수로 변환
    k_num = ''
    while n > 0:
        k_num = str(n % k) + k_num
        n //= k

    answer = 0
    for st in range(len(k_num)):
        for ed in range(st+1, len(k_num)+1):
            if '0' in k_num[st:ed] or not is_prime(int(k_num[st:ed])):
                continue
            elif st>0 and k_num[st-1] == '0' and ed<len(k_num) and k_num[ed] == '0':
                answer += 1
            elif st == 0 and ed < len(k_num) and k_num[ed] == '0':
                answer += 1
            elif st>0 and k_num[st-1] == '0' and ed == len(k_num):
                answer += 1
            elif st == 0 and ed == len(k_num):
                answer += 1

    return answer


# print(solution(437674, 3))
# print(solution(110011, 10))
```