"""
k 개 만큼의 귤을 고르는데, 크기 종류의 수를 최소화하고 싶다.

1<=k,len(tangerine)<=100,000

"""

import heapq
from collections import Counter

def solution(k, tangerine):

    counter = Counter(tangerine)
    pq = []
    for key, value in counter.items():
        heapq.heappush(pq, (-value, key))

    answer = 0
    while k > 0:
        value, size = heapq.heappop(pq)
        k += value
        answer += 1

    return answer

if __name__ == "__main__":
    print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))