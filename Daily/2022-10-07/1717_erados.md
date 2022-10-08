# 풀이
- Union-find 를 사용하였다.
- Union-find 의 최적화 방법은 두 가지 정도가 있는데
- 1. find 함수에서 각 노드와 root_parent 를 직접 연결시키기
- 2. union 함수에서 길이가 짧은 것을 긴 쪽에 붙이기
- 이다. 나는 1 만 구현하는 버릇이 있는데 2도 찾아보자..지금

# 코드
```python
import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
        return parent[a]
    return a


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a == parent_b:
        return

    parent[parent_a] = parent_b
    find(a)


for _ in range(M):
    c, a, b = map(int, input().split())
    parent_a = find(a)
    parent_b = find(b)
    if c:
        print("YES" if parent_a == parent_b else "NO")
    else:
        union(a, b)

```