import sys
sys.stdin = open("1954.txt")

# 달팽이 함수로 만들어보기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = [[0] * N for _ in range(N)]
    y, x, cnt, flag = 0, 0, 1, 0
    while cnt <= N ** 2:
        flag = flag % 4
        if flag == 0:
            for i in range(N):
                if ans[y][i] == 0:
                    ans[y][i] = cnt
                    cnt += 1
                    x = i
        elif flag == 1:
            for i in range(N):
                if ans[i][x] == 0:
                    ans[i][x] = cnt
                    cnt += 1
                    y = i
        elif flag == 2:
            for i in range(N - 1, -1, -1):
                if ans[y][i] == 0:
                    ans[y][i] = cnt
                    cnt += 1
                    x = i
        else:
            for i in range(N - 1, -1, -1):
                if ans[i][x] == 0:
                    ans[i][x] = cnt
                    cnt += 1
                    y = i
        flag += 1
    print("#{}".format(tc))
    for i in ans:
        for j in i:
            print(j, end=" ")
        print()
