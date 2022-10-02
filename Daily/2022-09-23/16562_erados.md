# 시간
- 30분 (틀림)

# 풀이
- union-find 로 풀었다.
- `unionFriend` 함수에서 친구비가 가장 작은 친구를 위로 올려주었다.
- 최적화를 위해 `findFreiend` 함수에서 root 를 찾는 동안 거치는 친구들을 모두 root 와 parant-child 관계를 가지게 하였다.
- 최소 비용을 계산하기 편하게 만들기위해 트리 아래 있는 노드들도 마지막에 root 와 parant-child 관계를 가지게 하였다.

# 코드
```pythond
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
friendship = [i for i in range(N + 1)]

def findFriend(friend):
    if friend == friendship[friend]:
        return friend
    friendship[friend] = findFriend(friendship[friend])
    return friendship[friend] 

def unionFriend(a, b):
    rootA = findFriend(a)
    rootB = findFriend(b)
    if A[rootA - 1] > A[rootB - 1]:
        friendship[rootA] = rootB
    else:
        friendship[rootB] = rootA
    

for _ in range(M):
    a, b = map(int, input().split())
    unionFriend(a, b)
    
for i in range(M):
    findFriend(i + 1)

cost = sum(A[i - 1] for i in list(set(friendship)) if i != 0)
print(cost if cost <= K else "Oh no")


```
# 수정한 코드
- M -> N 으로 수정
```python
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
friendship = [i for i in range(N + 1)]


def findFriend(friend):
    if friend == friendship[friend]:
        return friend
    friendship[friend] = findFriend(friendship[friend])
    return friendship[friend]


def unionFriend(a, b):
    rootA = findFriend(a)
    rootB = findFriend(b)
    if rootA == rootB:
        return
    if A[rootA - 1] > A[rootB - 1]:
        friendship[rootA] = rootB
    else:
        friendship[rootB] = rootA


for _ in range(M):
    a, b = map(int, input().split())
    if a != b:
        unionFriend(a, b)

for i in range(N):
    findFriend(i + 1)

cost = sum(A[i - 1] for i in list(set(friendship)) if i != 0)
print(cost if cost <= K else "Oh no")

```