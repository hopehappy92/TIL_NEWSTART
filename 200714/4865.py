import sys
sys.stdin = open("4865.txt")

T = int(input())
for tc in range(1, T + 1):
    N = set(str(input()))
    M = str(input())
    ans = 0
    for n in N:
        cnt = 0
        for m in M:
            if n == m:
                cnt += 1
        if ans < cnt:
            ans = cnt

    print("#{} {}".format(tc, ans))