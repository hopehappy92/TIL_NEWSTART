import sys
sys.stdin = open("1209.txt")

for _ in range(1, 11):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    ansList = []
    sumC = 0
    sumRC = 0
    for y in range(100):
        sumN = 0
        ansList.append(sum(data[y]))
        sumC += data[y][y]
        sumRC += data[y][99 - y]
        for x in range(100):
            sumN += data[x][y]
        ansList.append(sumN)
    ansList.append(sumRC)
    ansList.append(sumC)
    print("#{} {}".format(tc, max(ansList)))
    # for y in range(100):
    #     sumX = 0
    #     sumY = 0
    #     sumCross = 0
    #     sumReverseCross = 0
    #     for x in range(100):
    #         sumX += data[y][x]
    #         sumY += data[x][y]
    #         if x == y:
    #             sumCross += data[y][x]
    #         if x + y == 99:
    #             sumReverseCross += data[y][x]
    #     if sumX > sumY and sumX > ans:
    #         ans = sumX
    #     elif sumX < sumY and sumY > ans:
    #         ans = sumY
    # if sumCross > sumReverseCross and sumCross > ans:
    #     ans = sumCross
    # elif sumCross < sumReverseCross and sumReverseCross > ans:
    #     ans = sumReverseCross
    # print("#{} {}".format(tc, ans))
