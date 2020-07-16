import sys
sys.stdin = open("4881.txt")

def dfs(sumN, k):
    global N, ans
    if sumN > ans:
        return
    if k == N and ans > sumN:
        ans = sumN
        return
    else:
        for i in range(N):
            if not check[i]:
                check[i] = 1
                dfs(sumN + data[k][i], k+1)
                check[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    ans = 987654321
    dfs(0, 0)
    print("#{} {}".format(tc, ans))