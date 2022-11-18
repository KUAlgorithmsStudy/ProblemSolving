# 시간
- 1시간 (시간초과)

# 풀이
- 처음에는 리스트로 음식 갯수와 차 효과를 저장했으나 메모리 초과가 떴다.
- 그래서 딕셔너리로 바꾸었는데 시간 초과가 뜬다.
- 문제 유형에 DP 와 이분 탐색이 있는데 이걸 힌트로 잘 쓰면 될 것 같다.

# 코드
```python
import sys

input = sys.stdin.readline

T, N, D, K = map(int, input().split())

ans = 0

# 시간대별 음식 갯수
foods = {}

# 시간대별 다이어트 차 효과
score = {}

# 시간대별 음식 갯수 sum
for t in map(int, input().split()):
    foods[t] = 1 if not t in foods else foods[t] + 1

# 시간대별 다이어트 차 효과 sum
for key in foods.keys():
    for delay in range(D):
        if key + delay in foods:
            if key in score:
                score[key] += foods[key + delay]
            else:
                score[key] = foods[key + delay]

values = list(score.values())
values.sort(reverse=True)
print(sum(values[0 : K + 1]))

```