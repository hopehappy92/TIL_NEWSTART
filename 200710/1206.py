import sys
sys.stdin = open('1206.txt')

T = 10
for tc in range(T):
    N = int(input())
    data = list(map(int, (input().split())))
    answer = 0
    # for i in range(len(data)):
    #     if 2 <= i <= len(data)-3:
    #         temp = [data[i-2], data[i-1], data[i], data[i+1], data[i+2]]
    #         if temp[2] > temp[0] and temp[2] > temp[1] and temp[2] > temp[3] and temp[2] > temp[4]:
    #             minN = 987654321
    #             for j in range(5):
    #                 if j != 2:
    #                     tempSum = temp[2] - temp[j]
    #                     if tempSum <= minN:
    #                         minN = tempSum
    #             answer += minN

    for i in range(2, N-2):
        if i >= 2:
            rangeMin = 987654321
            for j in range(5):
                if j != 2:
                    if data[i] - data[i-2+j] < rangeMin:
                        rangeMin = data[i] - data[i-2+j]
            if rangeMin >= 0:
                answer += rangeMin

    print("#{} {}".format(tc+1, answer))

