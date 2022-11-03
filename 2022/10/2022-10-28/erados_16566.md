# 풀이
실패

cheat_sheet 의 i 번째 인덱스에 i 보다 큰 민수의 카드를 넣고
그 카드를 꺼내어 사용할 때마다 cheat_sheet 의 해당 카드 값들을 다음 카드 값으로 갱신시킨다.

# 코드
```python
import sys

_MAX = 4000001

input = sys.stdin.readline

# 총 카드 수, 내 카드 수, 문제 수
N, M, K = map(int, input().split())
minsu_cards = sorted(list(map(int, input().split())))
cheat_sheet = [_MAX] * (N + 1)
charles_cards = list(map(int, input().split()))

# graph[i] 에 i 보다 작거나 같은 민수 카드를 넣는다.
# 민수 카드가 2 이면 graph = [2, 2, 2, _MAX, _MAX, ...]
tmp = 0
for i in range(N):
    if tmp < M:
        if minsu_cards[tmp] >= i:
            cheat_sheet[i] = minsu_cards[tmp]
            if minsu_cards[tmp] == i:
                tmp += 1
    else:
        break


def pick_card(charles_card):
    idx = charles_card
    ans = cheat_sheet[idx + 1]
    while cheat_sheet[idx + 1] == ans:
        idx += 1
    next_num = cheat_sheet[idx + 1]
    for i in range(charles_card + 1, idx + 1):
        cheat_sheet[i] = next_num
    return ans


l = [0] * K
for idx, charles_card in enumerate(charles_cards):
    l[idx] = pick_card(charles_card)

print("\n".join(map(str, l)))

``` 