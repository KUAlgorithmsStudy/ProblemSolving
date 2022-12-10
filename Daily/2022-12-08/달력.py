N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

# 시작 빠른 순대로 정렬
schedule.sort(key=lambda x:(x[0], -(x[1]-x[0])))

arr = [0 for _ in range(366)]
for st, ed in schedule:
    arr[st] += 1
    arr[ed+1] -= 1

# cumsum
cumsum = [0 for _ in range(366)]
for i in range(1, len(arr)):
    cumsum[i] = cumsum[i-1] + arr[i]

# width, height
w, h = 0, 0
result = 0
for i in range(1, len(arr)):
    if cumsum[i] == 0:
        result += w*h
        w, h = 0,0
    else:
        w += 1
        h = max(cumsum[i], h)
print(result)
