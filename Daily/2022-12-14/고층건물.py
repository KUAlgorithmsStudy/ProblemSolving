import math

N = int(input())
arr = list(map(int, input().split()))


def solution(arr):
    answer = 0
    for i in range(N):
        cnt = 0

        # 양쪽으로 훑으면서
        for l in range(i - 1, -1, -1):
            angle = (arr[l] - arr[i]) / (l - i)
            # 중간에 아무것도 없으면 cnt += 1
            for k in range(l+1, i):
                if arr[k] >= (k-l) * angle + arr[l]:
                    break
            else:
                cnt += 1

        for r in range(i +1, N):
            angle = (arr[r] - arr[i]) / (r - i)
            # 중간에 아무것도 없으면 cnt += 1
            for k in range(i+1, r):
                if arr[k] >= (k-i) * angle + arr[i]:
                    break
            else:
                cnt += 1

        answer = max(cnt, answer)

    return answer


print(solution(arr))
