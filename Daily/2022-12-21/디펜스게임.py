"""
1<=n<10억
1<=k<50만
1<=len(enemy) < 100만

"""

import heapq
from collections import deque

def solution(n, k, enemy):
    answer = 0

    pq = []
    enemy = deque(enemy)
    # init : k 개 모두 사용하기
    while enemy and len(pq) < k:
        heapq.heappush(pq, enemy.popleft())
        answer += 1

    # 기존 사용 했을 때보다 enemy 가 더 많다면 기존 거 버리고 새로운 거에 무적권 사용. pq 에 넣기
    while enemy:
        if enemy[0] > pq[0]:  # 무적권 교체
            if n >= pq[0]:
                n -= heapq.heappop(pq)
                heapq.heappush(pq, enemy.popleft())
            else:
                break

        else:  # 몸으로 맞음
            if n >= enemy[0]:
                n -= enemy.popleft()
            else:
                break
        answer += 1

    return answer


if __name__ == "__main__":
    print(solution(700,3,[4, 2, 4, 5, 3, 3, 1]))
    print(solution(2,4,[3,3,3,3]))