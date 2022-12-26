from collections import deque
import heapq


N = int(input())
info = list(map(int, input().split()))

tree = [[] for _ in range(N)]
for i in range(1,N):
    tree[info[i]].append(i)



def dfs(v):
    if len(tree[v]) == 0:  # leaf node 인 경우
        return 1
    else:
        curmax = 0

        pq = []
        for i, n  in enumerate(tree[v]):
            t = dfs(n)
            heapq.heappush(pq, (-t, n))

        cnt = 0
        while pq:
            t, n = heapq.heappop(pq)
            curmax = max(curmax, -t + cnt)
            cnt += 1

        return curmax + 1

# print(tree)
print(dfs(0) - 1)


