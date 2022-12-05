"""
요약

설계
DP? pq?

주의점


"""

import heapq

M = int(input())
lines = []
while True:
    L, R = map(int, input().split())
    if (L, R) == (0, 0):
        break

    L = max(L, 0)
    R = min(R, M)

    if R-L != 0:

        heapq.heappush(lines, (R-L, L, R))

# R 순 으로 pq, L <st 이면 ㄱㄱ
answer = 0
st = 0
while lines:
    l, L, R = heapq.heappop(lines)
    if st < L:
        continue

    st = R
    answer += 1

if st < M:
    answer = 0
print(answer)
