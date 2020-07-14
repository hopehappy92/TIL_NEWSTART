import sys
sys.stdin = open("codeforce_653.txt")

T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    modDict = dict()
    for i in range(len(data)):
        mod = k - (data[i] % k)
        if mod != k:
            if mod not in modDict:
                modDict[mod] = 1
            else:
                modDict[mod] += 1
    if len(modDict) == 0:
        print(0)
        continue
    maxCnt = 0
    maxMod = 0
    for key, value in modDict.items():
        if maxCnt < value:
            maxCnt = value
            maxMod = key
        elif maxCnt == value:
            if maxMod < key:
                maxMod = key
    print((maxCnt - 1) * k + maxMod + 1)
    # flag = [0] * n
    # ans = 0
    # while 0 in flag:
    #     for i in range(len(data)):
    #         if not data[i] % k and flag[i] == 0:
    #             flag[i] = 1
    #             continue
    #         if not (data[i] + ans) % k and flag[i] == 0:
    #             data[i] += ans
    #             flag[i] = 1
    #             break
    #     ans += 1
    # print(0 if ans < 2 else ans)



    # ccccccccccccccccccccccccccccccccc
    # n = int(input())
    # s = str(input())
    # ans = 0
    # cnt = 0
    # for i in s:
    #     if i == ")":
    #         cnt += 1
    #     else:
    #         cnt -= 1
    #     if ans < cnt:
    #         ans = cnt
    # print(ans)
    #
    # 5
    # 2
    # )(
    # 4
    # ()()
    # 8
    # ())()()(
    # 10
    # )))((((())
    # 6
    # ()))((


    # bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    # n = int(input())
    # if n == 1:
    #     print(0)
    #     continue
    # cntTwo = 0
    # cntThree = 0
    # flag = 0
    # while n != 1:
    #     if not n % 2:
    #         n = n / 2
    #         cntTwo += 1
    #     elif not n % 3:
    #         n = n / 3
    #         cntThree += 1
    #     else:
    #         flag = 1
    #         break
    # if flag == 1 or cntTwo > cntThree:
    #     print(-1)
    #     continue
    # print(2 * cntThree - cntTwo)
    #
    # 7
    # 1
    # 2
    # 3
    # 12
    # 12345
    # 15116544
    # 387420489

    # aaaaaaaaaaaaaaaa
    # x, y, n = map(int, input().split())
    # mod = n % x
    # if mod > y:
    #     print(n - (mod - y))
    # elif mod < y:
    #     print(n - (mod + x - y))
    # else:
    #     print(n)

    # 7
    # 7
    # 5
    # 12345
    # 5
    # 0
    # 4
    # 10
    # 5
    # 15
    # 17
    # 8
    # 54321
    # 499999993
    # 9
    # 1000000000
    # 10
    # 5
    # 187
    # 2
    # 0
    # 999999999
