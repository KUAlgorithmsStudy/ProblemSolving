import heapq

def solution(n, info):
    answer = []

    # 가성비 정렬
    pq = []
    for i, d in enumerate(info[::-1]):
        if d > 0:
            ratio = (i*2)/ (d+1)
        else:
            ratio = i / (d+1)
        heapq.heappush(pq, (-ratio, i, d))

    answer = [0 for _ in range(11)]
    while pq and n>0:
        r, i, d = heapq.heappop(pq)
        if n > d:
            n -= (d+1)
            answer[10-i] = d+1
    if n > 0 :
        answer[-1] += n

    left = 0
    right = 0
    for i, (d1,d2) in enumerate(zip(info, answer)):
        if d1==d2==0:
            continue
        if d1 >= d2:
            left += 10-i
        else:
            right += 10-i

    if left >= right:
        return [-1]
    return answer

if __name__ == "__main__":
    # n = 5
    # info = [2,1,1,1,0,0,0,0,0,0,0]
    # print(solution(n, info))

    n = 10
    info = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]
    print(solution(n, info))