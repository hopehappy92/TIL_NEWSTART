import sys
sys.stdin = open("4869.txt")

def find(n):
    memo = [0, 1, 3]
    if n <= 2:
        return memo[n]
    for i in range(3, n + 1):
        memo.append(memo[i-1] + 2 * memo[i-2])
    return memo[n]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print("#{} {}".format(tc, find(N//10)))

    # 10 - 1
    # 20 - 3 - 1 + 2
    # 30 - 5 - 2 + 3
    # 40 - 11 - 6 + 5
    # 50 - 21
    # 60 - 43
    # 70 - 85