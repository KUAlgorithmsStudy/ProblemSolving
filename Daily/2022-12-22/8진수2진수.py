

# 1. 8진수를 2진수로 바꾼다.
def main(N):
    tmp = []
    for i in N:
        tmp.append(bin(int(i))[2:].zfill(3))
    return ''.join(tmp).lstrip("0")

def solution(N):
    return bin(int(N, 8))[2:]

if __name__ == "__main__":
    
    
    # compare main, solution
    import random
    for N in range(100):
        N = ''.join(random.choices(['0', '1', '2', '3', '4', '5', '6', '7'], k=10))
        # print(main(N), solution(N))
        assert main(N) == solution(N)