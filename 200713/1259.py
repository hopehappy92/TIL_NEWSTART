import sys
sys.stdin = open("1259.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    ans = ""
    flag = [0] * 2 * N
    for i in range(0, len(data), 2):
        if data.count(data[i]) == 1:
            startPoint = data[i]
            break
    # startList = []
    # endList = []
    # for i in range(0, len(data), 2):
    #     startList.append(data[i])
    #     endList.append(data[i+1])
    # for i in startList:
    #     if i not in endList:
    #         startPoint = i
    while 0 in flag:
        for i in range(0, len(data), 2):
            if data[i] == startPoint and flag[i] == 0:
                flag[i], flag[i+1] = 1, 1
                ans += str(data[i]) + " " + str(data[i+1]) + " "
                startPoint = data[i+1]
                break
    print("#{} {}".format(tc, ans))