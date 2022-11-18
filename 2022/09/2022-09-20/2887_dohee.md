# 2022-09-20

# 백준 2887 행성터널

# 30분 - 유형 kruskal

# 코드 - Python

```python
from collections import defaultdict,deque
import sys
input = sys.stdin.readline
n = int(input().rstrip())

parent = [i for i in range(n)]
x , y, z = [], [], []
for i in range(n):
    a,b,c = map(int ,input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))
x.sort()
y.sort()
z.sort()

e = []
for l in x,y,z:
    for i in range(0,n-1):
        e.append( (abs(l[i][0]-l[i+1][0]), l[i][1], l[i+1][1]) )
e.sort()

def findd(x):
    if x != parent[x]: parent[x] = findd( parent[x] )
    return parent[x]

def union(a,b):
    aa = findd(a)
    bb = findd(b)
    if aa == bb: return False
    if aa < bb: parent[bb] = aa
    else: parent[aa] = bb
    return True

ans, cnt = 0, 0
for l in e:
    cost, a,b = l
    if union(a,b): ans += cost; cnt+=1
    if cnt == n-1: break # 이 줄은 없어도 상관없는 연산이지만, 조금이라도 속도를 높이기 위해 작성했습니다.
print(ans)

```

# 풀이

전형적인 kruskal 알고리즘 변형 문제이었습니다.
가중치가 직접적으로 주어지지 않은 상황에서 가중치를 구한 후 크루스칼 알고리즘으로 문제를 해결 할 수 있습니다.

문제를 풀기전에 크루스칼 알고리즘의 핵심 원리를 이해하면 문제를 쉽게 풀 수 있습니다.
크루스칼 알고리즘은 최소신장 트리(MST)를 구하기 위한 알고리즘입니다.
MST 가 되기 위해서는 (1) 모든 정점을 포함 (2) 사이클이 존재하지 않는 하나의 그래프 (3) (1)번과 (2)번을 만족하는 트리들 중 가중치의 합이 최소인 트리
를 만족해야합니다.

MST를 만들기 위해서
(1) 가중치를 기준으로 오름차순 정렬
(2) 정렬된 순서대로 연결되어있지 않은 정점을 연결(union find)
하는 동작을 반복합니다.
최소 가중치를 가장 먼저 연결시도(두 정점이 이미 연결되어있으면-사이클이 형성되지 않으면- 연결하지 않음)한다는 점에서 크루스칼 알고리즘이 그리디 알고리즘의 일종이라고 말 할 수도 있겠습니다.

\*union find 자료구조
union find는 Disjoint Set을 표현하는 자료구조로, 두 집합 병합(union) 연산과 각 원소가 속한 집합 확인(find) 연산을 지원합니다.

이런 관점에서 문제를 해결하였습니다.
다만 이 문제에 특별한 점이 있었다면,
최소 가중치를 구하기 위한 과정이 추가적으로 필요하다는 것과
가중치 후보들이 매우 많았다는 점이 차별점이었습니다.

(1) 최소 가중치를 구하기 위해 x, y, z 비용을 모두 소팅합니다. 소팅된 상태에서 abs(x[i]-x[i+1])의 값들을 모두 하나의 array에 저장합니다.

(2) (1)번 작업을 y와 z비용에도 모두 동일하게 하여 하나의 배열에 저장합니다. 가능한 모든 가중치(|xA-xB|, |yA-yB|, |zA-zB| 전부)를 구했으니 이를 가중치를 기준으로 오름차순 정렬합니다.

최소 가중치 후보들을 직접 구하고
이들을 각각 처리해주는 것이 아니라 모두 하나의 배열에 넣어 union find한다는 것이 독특했을 뿐이지,
거시적으로 보았을때는 전형적인 크루스칼 알고리즘의 동작방식을 띄고 있었습니다.
