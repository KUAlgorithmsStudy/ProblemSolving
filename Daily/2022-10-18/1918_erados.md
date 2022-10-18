# 풀이
정규식으로 *, / 을 괄호로 감싸고 시작하려다가 그냥 풀어보았따.
어렵다.. 분명 데구알에서 배운 것 같은데 기억이 안난다.
연산자 우선순위를 고려하여 기입력된 연산자가 입력될 연산자보다 우선될 경우 기입력된 연산자를 pop 하여 출력하고 입력될 연산자를 push 한다.
괄호를 만나는 경우 닫는 괄호를 만나면 여는 괄호가 있는 곳까지 연산자를 pop 하여 출력한다.

# 코드
```python
exp = input()
operator_stack = []
operators = ["+", "-", "*", "/"]

for c in exp:

    if c == "(":
        operator_stack.append(c)
    elif c == ")":
        while True:
            a = operator_stack.pop()
            if a != "(":
                print(a, end="")
            else:
                break
    elif c in operators[:2]:
        if len(operator_stack) > 0 and operator_stack[-1] in operators:
            print(operator_stack.pop(), end="")
        operator_stack.append(c)
    elif c in operators[2:]:
        if len(operator_stack) > 0 and operator_stack[-1] in operators[2:]:
            print(operator_stack.pop(), end="")
        operator_stack.append(c)
    else:
        print(c, end="")
print("".join(operator_stack[::-1]))

```