import math

"""
실책성 무브는 어떤 line 에서 필터링 되는건
"""

def solution(board, aloc, bloc):
    R = len(board)
    C = len(board[0])

    def move(r1, c1, r2, c2, step, player):  # -> (can_win, step)
        if board[r1][c1] == 0:
            return False, step

        max_turn = step
        min_turn = math.inf
        my_win = False
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r1 + dr, c1 + dc
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 1:
                board[r1][c1] = 0
                other_win, turn = move(r2, c2, nr, nc, step + 1, player ^ 1)
                if not other_win:
                    my_win = True
                    min_turn = min(min_turn, turn)
                else:  # 이기는 경우가 있다면 굳이 지는 경우는 볼 필요가 없다.
                    max_turn = max(max_turn, turn)
                board[r1][c1] = 1

        return my_win, min_turn if my_win else max_turn

    my_win, answer = move(*aloc, *bloc, 0, 0)

    # 이기는 쪽은 min step 하도록, 지는 쪽은 max step 하도록 움직이자
    return answer


if __name__ == '__main__':
    # board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    # aloc = [1, 0]
    # bloc = [1, 2]
    # print(solution(board, aloc, bloc))  # 5

    board = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    aloc = [1, 0]
    bloc = [1, 2]
    print(solution(board, aloc, bloc))  # 4
