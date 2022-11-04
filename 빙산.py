from collections import deque


N, M = map(int, input().split())

board = []
ice_list = []
for i in range(N):
    row = list(map(int, input().split()))
    for j, el in enumerate(row):
        if el != 0:
            ice_list.append((i, j, el))
    board.append(row)

next_ice_list = []
next_board = [[el for el in row] for row in board]

cnt = 0
R = len(board)
C = len(board[0])
while True:
    cnt += 1

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
        if remain != 0:
            next_ice_list.append((i,j,remain))
        next_board[i][j] = remain

    ice_list = next_ice_list
    board = next_board

    if not ice_list:
        cnt=0
        break
    # check split
    queue = deque([ice_list[0]])
    visited = {str(ice_list[0][0])+str(ice_list[0][1]):True}

    while queue:
        i,j,_ = queue.popleft()

        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 0 and str(ni) + str(nj) not in visited:
                visited[str(ni) + str(nj)] = True
                queue.append((ni,nj,board[ni][nj]))

    if len(visited) != len(ice_list):
        break

print(cnt)