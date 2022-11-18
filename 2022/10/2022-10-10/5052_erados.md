# 풀이 (틀림)
- 정렬을 한 뒤 트라이 형태로 만들면서 겹치는 문구가 있는지 체크했다.
- 트라이를 제대로 구현한 코드를 찾아봐야겠다. TODO

# 코드
```python
import sys

input = sys.stdin.readline

T = int(input())
tree = {}
end = None
for _ in range(T):
    end = False
    nums = []
    for idx in range(int(input())):
        nums.append(input().rstrip())
    nums.sort()

    for item in nums:
        idx = 0
        temp = tree
        while idx < len(item):
            c = item[idx]
            if not c in temp.keys():
                temp[c] = {}

            if temp[c] == True:
                end = True
                print("NO")
                break

            if idx == len(item) - 1:
                temp[c] = True

            temp = temp[c]
            idx += 1
        if end:
            break
    if not end:
        print("YES")

```