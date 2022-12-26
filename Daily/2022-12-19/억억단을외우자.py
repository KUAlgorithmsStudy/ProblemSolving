"""
문제요약
(e, starts) => result:List
s<=x<=e 범위의 수 중 억억단에서 가장 많이 등장한 수를 답해야 함.

설계
1. s<=x<=e 범위의 수 중 약수의 개수가 가장 많은 수를 찾는다.

주의
1. e<=500만
2. len(starts) <= 10만

"""


def solution(e, starts):
    # 1. e까지의 약수의 개수를 구한다. 에라토스테네스의 체
    sqrt = int(e ** 0.5)
    divisors = [1] * (e + 1)
    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            divisors[j] += 1
     
    record = [0 for _ in range(e+1)]
    curmax = 0
    curidx = e
    for x in range(e, 0, -1):
        if divisors[x] >= curmax:
            curmax = divisors[x]
            curidx = x
        record[x] = curidx

    answer = []
    for s in starts:
        answer.append(record[s])

    return answer

if __name__ == "__main__":
    print(solution(10, [1, 3, 7]))
    # print(solution(500000, [1, 3, 7]))