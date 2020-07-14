import sys
sys.stdin = open("2001.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for y in range(N - M + 1):
        for x in range(N - M + 1):
            cnt = 0
            for my in range(y, y + M):
                for mx in range(x, x + M):
                    cnt += data[my][mx]
            if ans < cnt:
                ans = cnt
    print("#{} {}".format(tc, ans))

