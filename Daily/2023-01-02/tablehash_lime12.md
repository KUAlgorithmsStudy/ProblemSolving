
## 문제
[테이블 해시 함수](https://school.programmers.co.kr/learn/courses/30/lessons/147354)

- 구현 (N-d list sort 정리, & and | or ^ XOR ~ not << left shift >> right shift)

## 풀이
- 문제에 제시된 대로, 구현한다. 2d list 정렬 방법은 lambda 이용해서, key를 두 개로 설정하면 된다.

```py
from sys import stdin
def solution(data, col, row_begin, row_end):
    answer = 0
    # col 기준, 오름차순 정렬 + 첫번째 컬럼 기준 내림차순 정렬
    data = sorted(data, key=lambda x : (x[col-1], -x[0]))
    # S_i def : i th row / i 나머지 합
    # row begin, end 모든 S_i 누적 
    # bitwise XOR
    #sliced = data[row_begin-1 : row_end]
    total_S=0
    for i in range(row_begin, row_end+1):
        temp_S=0
        for j in data[i-1]:
            temp_S += j % i
        total_S = total_S ^ temp_S
    answer = total_S
    return answer

if __name__ == "__main__":
    solution()
```
