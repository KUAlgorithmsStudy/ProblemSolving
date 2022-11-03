# 풀이
B 를 이진수로 바꿔서 나온 비트에 맞춰, 미리 구해둔 A의 거듭제곱끼리 곱했다.
그리고 (x * 1000 + a) * (y * 1000 + b) % 1000 = a * b % 1000 이다.

# 코드
```python
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [[0] * N for _ in range(N)]

bin_reversed = "{0:b}".format(M)[::-1]

# ans 를 항등행렬로 초기화
ans = [[1 if x == y else 0 for x in range(N)] for y in range(N)]

# A^(2^i) 를 i 번째에 저장하는 리스트
matrix_storage = [None] * (len(bin_reversed) + 1)

# A 초기화
for y in range(N):
    A[y] = list(map(int, input().split()))

# 행렬곱 함수
def mul(A, B):
    B_T = list(map(list, zip(*B)))
    C = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            C[y][x] = sum(map(lambda a, b: a * b, A[y], B_T[x])) % 1000
    return C


# matrix_storage 값 채우기
matrix_storage[0] = A

for i in range(1, len(bin_reversed) + 1):
    matrix_storage[i] = mul(matrix_storage[i - 1], matrix_storage[i - 1])

# 답 구하기
for i, _bin in enumerate(bin_reversed):
    if _bin == "1":
        ans = mul(ans, matrix_storage[i])

for row in ans:
    print(" ".join(list(map(str, row))))

```