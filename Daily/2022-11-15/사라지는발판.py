def solution(board, aloc, bloc):
    answer = -1

    R = len(board)
    C = len(board[0])
    # a : 0 , b : 1
    loc = [aloc, bloc]

    # 누가 이길 지 부터 알아내자
    def move(player):  # player 가 이길 것인가? -> True/False
        x, y = loc[player]
        if board[x][y] == 0:  # 발판 사라졌으면 짐
            return False

        # 갈 데 있는 지 체크
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] == 1:
                    loc[player] = (nx, ny)
                    board[x][y] = 0
                    if move(1 if player == 0 else 0):  # 내가 승리 못할거라면 이 길 가면 안됨.
                        board[x][y] = 1
                        loc[player] = (x, y)
                    else:
                        return True
        else:
            return False

    winner = move(0)
    print(winner)

    # 이기는 쪽은 min step 하도록, 지는 쪽은 max step 하도록 움직이자
    # return answer


if __name__ == '__main__':
    board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    aloc = [1, 0]
    bloc = [1, 2]
    print(solution(board, aloc, bloc))  # 5

    # board = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    # aloc = [1, 0]
    # bloc = [1, 2]
    # print(solution(board, aloc, bloc))  # 4
