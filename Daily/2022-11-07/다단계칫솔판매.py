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
        propagate(referral[idx], his)

    return answer


if __name__ == "__main__":
    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["young", "john", "tod", "emily", "mary"]
    amount = [12, 4, 2, 5, 10]
    print(solution(enroll, referral, seller, amount))  # [360, 958, 108, 0, 450, 18, 180, 1080]