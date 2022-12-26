import heapq


N, K = map(int, input().split())

jewelry = []
for _ in range(N):
    M, V = map(int, input().split())
    jewelry.append((M, V))

bag = []
for _ in range(K):
    bag.append(int(input()))

jewelry.sort(key=lambda x: x[0])
bag.sort()


def sol1(bag, jewelry):
    result = 0
    heap = []
    for b in bag:
        while jewelry and b >= jewelry[0][0]:
            M, V = jewelry.pop(0)
            heapq.heappush(heap, -V)

        if heap:
            result -= heapq.heappop(heap)
        else:
            break

    return result


def sol2(bags, jew):
    answer = 0
    tmp_jew = []
    for bag in bags:
        while jew and bag >= jew[0][0]:
            heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
        if tmp_jew:
            answer -= heapq.heappop(tmp_jew)
        elif not jew:
            break
    return answer


if __name__ == "__main__":
    # generate random input and compare two solutions
    import random
    import time

    for _ in range(100):
        N = random.randint(1, 1000)
        K = random.randint(1, 1000)
        jewelry = []
        for _ in range(N):
            M = random.randint(1, 100000)
            V = random.randint(1, 100000)
            jewelry.append((M, V))

        bag = []
        for _ in range(K):
            bag.append(random.randint(1, 100000))

        result1 = sol1(bag, sorted(jewelry))
        result2 = sol2(bag, sorted(jewelry))

        
        if result1 != result2:
            print("Wrong Answer")
            break
        else:
            print("Correct Answer")