from collections import deque


N, M = map(int, input().split())

count = [0] * (N+1)
graph = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    if b not in graph[a]:
        graph[a].add(b)
        count[b] += 1

queue = deque([])
for i in range(1, N+1):
    if count[i] == 0:
        queue.append(i)

answer = []
while queue:
    node = queue.popleft()
    answer.append(node)
    for i in graph[node]:
        count[i] -= 1
        if count[i] == 0:
            queue.append(i)

print(*answer)