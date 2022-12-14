## 거짓말 
: bfs variation; 50분

```python
"""
그냥 생각나는대로 하면 루프 빠져나가는 설계를 하기 어려움.

"""

from collections import defaultdict, deque


def main():
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    truth_people = tmp[1:]

    user2party = defaultdict(list)
    party2user = defaultdict(list)
    for party in range(M):
        tmp = list(map(int, input().split()))
        people = tmp[1:]
        for user in people:
            user2party[user].append(party)
            party2user[party].append(user)

    queue = deque(truth_people)  # 진실 아는 사람들
    visited = set()
    for p in truth_people:
        visited.add(p)

    truth_party = set()
    while queue:
        user = queue.popleft()
        parties = user2party[user]
        for cur_party in parties:
            truth_party.add(cur_party)
            for other_user in party2user[cur_party]:  # visited 체크가 필요한데
                # 진실만 말해야 함
                if other_user not in visited:
                    visited.add(other_user)
                    queue.append(other_user)


    return M - len(truth_party)


if __name__ == "__main__":
    print(main())
```

## 다단계칫솔판매
런타임 에러나는데 왜 그런지 모르겠음

```python 
"""
설계

O(S * logE)
for sale in seller :
    propagte(sale)

주의점 
1. 원단위 절삭


"""
def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]

    name2idx = {name:i for i, name in enumerate(enroll)}

    def propagate(name, amt):
        if name == "-":
            return
        idx = name2idx[name]
        his = int(amt * 0.1)
        mine = amt - his
        answer[idx] += mine
        propagate(referral[idx], his)


    for name, amt in zip(seller, amount):
        amt *= 100
        his = int(amt * 0.1)
        mine = amt - his

        idx = name2idx[name]
        answer[idx] += mine
        if his > 0:
            propagate(referral[idx], his)

    return answer


if __name__ == "__main__":
    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["young", "john", "tod", "emily", "mary"]
    amount = [12, 4, 2, 5, 10]
    print(solution(enroll, referral, seller, amount))  # [360, 958, 108, 0, 450, 18, 180, 1080]
```