from collections import deque
import heapq


N = int(input())

A = []
B = []
queue_A = []
queue_B = []
for i in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)
    heapq.heappush(queue_A, (a,i))
    heapq.heappush(queue_B, (b,i))

# queue_A = deque(sorted(A))
# queue_B = deque(sorted(B))

aval = queue_A[0][0]
aidx = queue_A[0][1]
visited = [False] * N
visited[aidx] = True
ret = aval

answer = [ret]
for _ in range(1,N):
    # 음식 개수 늘릴 때 A 방향으로 늘릴 것인가
    while True:
        a,a_i = heapq.heappop(queue_A)
        if not visited[a_i]:
            
            break
    
    while True:
        b,b_i = heapq.heappop(queue_B)
        if not visited[b_i]:
            
            break

    if a - aval + B[aidx] < b:
        ret += a - aval + B[aidx]
        visited[a_i] = True
        answer.append(ret)
        aidx = a_i
        aval = a
        # queue_B.append((b, b_i))
        heapq.heappush(queue_B, (b,b_i))
    else:
        ret += b
        visited[b_i] = True
        answer.append(ret)
        # queue_A.append((a, a_i))
        heapq.heappush(queue_A, (a,a_i))

print(*answer, sep='\n')




# if __name__ == "__main__":
    # import random
    # # Random int N
    # N = random.randint(1,10)
    # # generate A, B
    # A = [random.randint(1,10) for _ in range(N)]
    # B = [random.randint(1,10) for _ in range(N)]

    # print(N, A, B)