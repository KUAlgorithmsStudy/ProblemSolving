# 풀이
 - sys.setrecursionlimit(51) 이 핵심이다.
 - tree 와 dfs 를 사용했다.

# 코드
```python
import sys

input = sys.stdin.readline
sys.setrecursionlimit(51)

N = int(input())

# tree[parent] = [child1, child2, ...] 가 저장되는 dict
tree = {}
root = -1
cnt_leaf = 0

# tree 에 각 노드의 child 정보를 넣는다.
for child, parent in enumerate(list(map(int, input().split()))):
    if parent != -1:
        if parent in tree:
            tree[parent].append(child)
        else:
            tree[parent] = []
            tree[parent].append(child)
    else:
        root = child

node_to_remove = int(input())


def dfs(parent):
    global cnt_leaf

    if parent == node_to_remove:
        return

    if parent not in tree or tree[parent] == [node_to_remove]:
        cnt_leaf += 1
        return

    for child in tree[parent]:
        if child != node_to_remove:
            dfs(child)


dfs(root)
print(cnt_leaf)

```