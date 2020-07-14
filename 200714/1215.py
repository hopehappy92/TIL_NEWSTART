import sys
sys.stdin = open("1215.txt")

def palindrome(N):
    cnt = 0
    for y in range(8):
        for x in range(8 - N + 1):
            flag = 0
            for n in range(N//2):
                if data[y][x + n] != data[y][x + N - 1 - n]:
                    flag = 1
                    break
            if flag == 0:
                cnt += 1
            flag = 0
            for n in range(N//2):
                if data[x+n][y] != data[x + N - 1 - n][y]:
                    flag = 1
                    break
            if flag == 0:
                cnt += 1
    return cnt
            # tempX = ""
            # tempY = ""
            # for n in range(N//2):
            #     if data[y][x + n] != data[y][x + N - 1 - n]:
            #         break
            #     tempX += data[y][x + n]
            # if tempX == tempX[-1::-1] and len(tempX) == N:
            #     cnt += 1
            # for n in range(N//2):
            #     if data[x + n][y] != data[x + N - 1 - n][y]:
            #         break
            #     tempY += data[x + n][y]
            # if tempY == tempY[-1::-1] and len(tempY) == N:
            #     cnt += 1
    # return cnt
for tc in range(1, 11):
    N = int(input())
    data = [list(map(str, input())) for _ in range(8)]
    print("#{} {}".format(tc, palindrome(N)))