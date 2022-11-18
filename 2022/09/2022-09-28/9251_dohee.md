# 2022-09-27

# 백준 1918

# 실패 - 후위표기식

# Algorithms & Datastructures - stack

# 코드 - Python

```python
from collections import defaultdict,deque
global st, orda,ordz
st = deque( input() )
n = len(st)
stk = deque()
orda, ordz = ord('A'), ord('Z')
ans = ''

for s in st:
    if orda <= ord(s) <= ordz: ans += s
    else:
        if s == '(': stk.append(s)
        elif s == '*' or s == '/' :
            while stk and ( stk[-1] == '*' or stk[-1] == '/' ) : ans += stk.pop()
            stk.append( s )
        elif s == '+' or s == '-':
            while stk and stk[-1] != '(': ans += stk.pop()
            stk.append(s)
        elif s == ')':
            while stk and stk[-1] != '(': ans += stk.pop()
            stk.pop()
while stk:
    if stk[0] == '(' or stk[0] == ')': stk.pop(); continue
    ans += stk.pop()

print(ans)
```

# 풀이

Stack 자료구조를 활용하여 해결했습니다.

입력값의 문자를 순서대로 하나하나 조회합니다.

1. 알파벳인 경우 순서대로 answer에 저장해줍니다.
2. 알파벳이 아닌 경우,
   다음과 같이 stack을 활용하여 연산자들의 우선순위를 결정해줍니다.
   (1) '(' 인 경우, 스택에 push 합니다.
   (2) '/' 이거나 '_'인 경우에는
   스택에 들어있던 연산자가 '/,_'이면, 스택에서 pop하여 answer에 저장 해줍니다.
   (스택에 들어있는 '/,_'가 지금의 '/,_' 보다 우선순위가 높기에)
   스택에 현재 '/,\*'를 push합니다.
   (3) '+' 이거나 '-'인 경우에는
   '+, -'는 우선순위가 가장 낮은 연산자이므로
   '('를 제외한 모든 stack에 있는 연산자를 pop하여 answer에 저장해줍니다.
   스택에 현재 '+,-'를 push합니다.
   (4) ')'인 경우, '('가 나올때까지 스택에 저장된 연산자를 모두 pop하여 answer에 저장해줍니다.
   stack의 top이 '('이면 pop을 멈춥니다.
   pop을 한번 시행하여 stack에 남아있는 '('를 제거합니다.

조회가 끝나면,
stack에 남아있는 모든 연산자를 pop하여 ans에 저장해줍니다.
