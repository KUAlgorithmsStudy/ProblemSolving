---
date: "2022-11-09"
문제번호:
  - 4195
  - 60058
---

# 2022-11-09

## 1. 4195 (친구 네트워크)
https://www.acmicpc.net/problem/4195
: parent 외에 number 를 관리하는게 편함

```python
T = int(input())
for _ in range(T):
    F = int(input())
    parent = {}
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x = find(x)
        y = find(y)
        if x != y:
            parent[y] = x
            number[x] += number[y]

    number = {}
    for _ in range(F):
        x, y = input().split()
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        union(x, y)
        print(number[find(x)])

```

### 알고리즘 분류
- 자료 구조
- 해시를 사용한 집합과 맵
- 분리 집합

## 2. 60058 (괄호 변환)
https://school.programmers.co.kr/learn/courses/30/lessons/60058

: 시뮬레이션, 문자열 처리

```python
"""




"""


def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if p == '': return ''

    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    u, v = '', ''
    for i in range(2, len(p) + 1, 2):
        if p[:i].count('(') == p[:i].count(')'):
            u, v = p[:i], p[i:]
            break

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    def is_valid(u):
        stack = []
        for c in u:
            if c == '(':
                stack.append(c)
            elif stack:
                stack.pop()
            else:
                return False
        return True

    if is_valid(u) and u.count('(') > 0:
        return u + solution(v)

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
    #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    #   4-3. ')'를 다시 붙입니다.
    #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
    #   4-5. 생성된 문자열을 반환합니다.
    else:
        return '(' + solution(v) + ')' + ''.join(['(' if i == ')' else ')' for i in u[1:-1]])


if __name__ == '__main__':
    # print(solution("(()())()"))
    print(solution(")("))
    # print(solution("()))((()"))

```