def solution(board, aloc, bloc):
    answer = -1

    R = len(board)
    C = len(board[0])
    loc = [aloc, bloc]  # a : 0 , b : 1

    # 누가 이길 지 부터 알아내자
    def move(player, step, hist):  # player 가 이길 것인가? -> True/False
        print(hist)
        x, y = loc[player]
        if board[x][y] == 0:  # 발판 사라졌으면 짐
            return False

        # 갈 데 있는 지 체크
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == 1:
                loc[player] = (nx, ny)
                board[x][y] = 0
                hist['a'].append((nx, ny)) if player == 0 else hist['b'].append((nx, ny))
                if move(1 if player == 0 else 0, step + 1, hist):  # 내가 승리 못할거라면 이 길 가면 안됨; 최대한 시간 끌기
                    print(f'{"a" if player == 0 else "b"} dont want to lose. rollback!')
                    board[x][y] = 1
                    loc[player] = (x, y)
                    hist['a'].pop() if player == 0 else hist['b'].pop()
                else:  # 내가 승리할 수 있다면 이 길 가야함; 최대한 빨리 끝내기
                    return True


    winner = move(0, 0, dict(a=[aloc], b=[bloc]))
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
