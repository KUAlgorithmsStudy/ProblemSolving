# 2022-09-07

# 백준 9665 n-queen

# ?분 - 유형 BackTracking

# 코드 - Python

```python
import sys; reader = sys.stdin.readline

def search(col, ld, rd, n):
    size = ((1 << n) - 1)
    count = 0
    if col == size: return 1
    slots = ~(col | ld | rd) & size
    while slots:
        bit = slots & -slots 
        count += search(col | bit, (ld | bit) >> 1, (rd | bit) << 1, n)
        slots -= bit
    return count

n = int( reader().rstrip() )
print( search(0, 0, 0, n) )
```

# 풀이

풀어봤던 문제이기에 새로운 방식으로 접근했습니다.
연산 시간을 줄이기 위해
제가 짠 코드에 다른 사람의 코드를 일부 참고했습니다.
코드에서 쉬프트 연산자가 활용된 부분은 참고한 부분입니다. 