"""
요약
- 닭의 도움을 받을 수 있는 최대 소의 개수

주의
1. 소는 최대 한 마리의 닭을 도와줄 수 있다.
2. 닭도 최대 한 마리의 소를 도와줄 수 있다.
3. 1<= N , C < 2만

"""
import heapq
from collections import deque

C, N = map(int, input().split())

T = []
for _ in range(C):
    T.append(int(input()))
T.sort()
T = deque(T)

cow = []
for i in range(N):
    s,e = map(int, input().split())
    cow.append((s,e,i))
cow.sort()
cow = deque(cow)

answer = 0
pq_e = []
while T:
    t = T.popleft()
    # s 기준으로 자격 되는 것 중
    while cow and cow[0][0] <= t:
        # s,e,i = heapq.heappop(cow)
        s,e,i = cow.popleft()
        heapq.heappush(pq_e, (e,s,i))

    # e 기준으로 가장 빠른거 가져오자
    while pq_e:
        e,s,i = heapq.heappop(pq_e)
        if t<=e:
            answer += 1
            break

    # 더 빨리 끝나면 어차피 자격 안됨.

print(answer)