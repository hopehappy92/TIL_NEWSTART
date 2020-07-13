import sys
sys.stdin = open('4836.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    flag = [[0] * 10 for _ in range(10)]
    data = []
    for n in range(N):
        data.append(list(map(int, input().split())))
    for r in range(len(data)):
        for y in range(data[r][0], data[r][2]+1):
            for x in range(data[r][1], data[r][3]+1):
                flag[y][x] += data[r][4]
    ans = 0
    for i in flag:
        ans += i.count(3)
    print("#{} {}".format(tc, ans))