import sys
sys.stdin = open('4834.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    string_data = input()
    data = [0] * 10
    for i in string_data:
        data[int(i)] += 1
    maxCnt = max(data)
    maxIndex = 0
    for i in range(len(data)-1, -1, -1):
        if data[i] == maxCnt:
            maxIndex = i
            break
    print("#{} {} {}".format(tc+1, maxIndex, maxCnt))