--
날짜: "2022-09-22"
문제번호:
  - "1018"
  - "17142"
---

# 2022-10-31

## 1. 8980 (택배)

https://www.acmicpc.net/problem/8980

### 알고리즘 분류

- greedy

```python
N, C = map(int, input().split())
M = int(input())

info = []
for _ in range(M):
    from_, to, v = map(int, input().split())
    info.append((from_, to, v))
info.sort(key=lambda x:x[1])


# greedy
# 배송 빨리 끝나는 순서대로 배송
result = 0
luggage = [0 for _ in range(N+1)]

for (from_, to, v) in info:

    to_carry = min(C-max(luggage[from_:to]), v)

    for i in range(from_, to):
        luggage[i] += to_carry

    result += to_carry

print(result)
```

## 2. 헤비유저가 소유한 장소

https://www.acmicpc.net/problem/17142

### 알고리즘 분류
- where 절에 사용하는 subquery

소요시간 : 3분

```sql
select * from PLACES
where HOST_ID in 
(select HOST_ID
from PLACES
group by HOST_ID
having count(HOST_ID) > 1)
```
