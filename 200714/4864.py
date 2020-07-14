import sys
sys.stdin = open("4864.txt")

def find():
    for m in range(len(M)-len(N)+1):
        for n in range(m, len(N)+1+m):
            if n - m == len(N) and n <= len(M) and N == M[m:n]:
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = str(input())
    M = str(input())
    ans = find()
    print("#{} {}".format(tc, ans))

