S = input()
T = input()

# 루프돌면서
# T의 뒤에서부터 1. A를 뺴거나 2. B를 뺀다.
# S와 길이가 같아졌을 때 S와 T가 같은지 확인한다.
# 같으면 1, 아니면 0

def dfs(t):
    if len(S) == len(t):
        if S == t:
            return 1
        else:
            return 0
    else:
        ret = 0
        if t[-1] == 'A':
            ret = dfs(t[:-1])

        if not ret and t[0] == 'B':
            ret = dfs(t[1:][::-1])
        
        return ret

print(dfs(T))