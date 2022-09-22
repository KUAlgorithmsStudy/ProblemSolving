# 시간 ?

# 풀이
- brute force 로 모든 경우의 수를 다 뒤졌다.

# 코드
```python
[n, m] = (int(x) for x in input().split())
lst = []
outerlst = []
for i in range(n):
    lst.append(input())
for i in range(0,n-7):
    innerlst = []
    for j in range(0,m - 7):
        num = 0
        for ii in range(i, i+8):
            for jj in range(j, j+8):
                num += (1 if ((lst[ii][jj] == "W" and (ii+jj) % 2 == 0) or (lst[ii][jj] == "B" and (ii+jj) % 2 == 1)) else 0)
        innerlst.append(num)
    outerlst.append(innerlst)
print(min(64-max(map(max,outerlst)), min(map(min,outerlst))))
```