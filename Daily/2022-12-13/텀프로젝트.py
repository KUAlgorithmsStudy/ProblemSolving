def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]


def postprocess(v):
    if settled[v] != 0:
        return

    settled[v] = 1
    postprocess(preference[v])


def dfs(v):
    if settled[v] == 1:
        return

    a = find(v)
    b = find(preference[v])

    if a == b:  # cycle detected
        postprocess(preference[v])  # settle nodes in cycle
        return
    else:
        union(v, preference[v])
        dfs(preference[v])


T = int(input())
for _ in range(T):
    n = int(input())
    parent = [i for i in range(n + 1)]
    settled = [0] * (n + 1)

    preference = {i + 1: v for i, v in enumerate(map(int, input().split()))}
    for i in range(1, n + 1):
        dfs(i)

    print(n - sum(settled))
