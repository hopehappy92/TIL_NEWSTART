import sys
sys.stdin = open("1208.txt")

for tc in range(1, 11):
    N = int(input())
    data = list(map(int, input().split()))
    ans = 0
    while N > 0:
        maxIndex = data.index(max(data))
        minIndex = data.index(min(data))
        data[maxIndex] -= 1
        data[minIndex] += 1

        # maxN = 0
        # maxIndex = -1
        # minN = 101
        # minIndex = -1
        # for i in range(len(data)):
        #     if maxN < data[i]:
        #         maxN = data[i]
        #         maxIndex = i
        #     if minN > data[i]:
        #         minN = data[i]
        #         minIndex = i
        # data[maxIndex] -= 1
        # data[minIndex] += 1
        N -= 1

    print("#{} {}".format(tc, max(data)-min(data)))