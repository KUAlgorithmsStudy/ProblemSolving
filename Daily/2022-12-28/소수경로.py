from collections import deque


T = int(input())

visited = [False] * 10000
# 1. 네 자리 소수를 모두 구한다.
for i in range(2, 10000):
    if visited[i]:
        continue
    for j in range(i * 2, 10000, i):
        visited[j] = True

# 2. 각 소수를 노드로 생각하고, 각 노드를 연결하는 간선을 구한다.
graph = [[] for _ in range(10000)]
for i in range(1000, 10000):
    if visited[i]:
        continue
    for j in range(4):
        for k in range(10):
            if j == 0 and k == 0:
                continue
            temp = int(str(i)[:j] + str(k) + str(i)[j + 1:])
            if not visited[temp] and i != temp:
                graph[i].append(temp)

# 3. BFS를 통해 최단 경로를 구한다.

def bfs(from_, to_):
    q = deque([from_])
    dist = [0] * 10000
    while q:
        now = q.popleft()
        if now == to_:
            print(dist[now])
            return
        for next_ in graph[now]:
            if dist[next_] == 0:  # 방문하지 않은 노드일 경우
                q.append(next_)
                dist[next_] = dist[now] + 1
                # print(dist[next_], next_)
    print("Impossible")

for _ in range(T):
    a, b = map(int, input().split())
    bfs(a, b)