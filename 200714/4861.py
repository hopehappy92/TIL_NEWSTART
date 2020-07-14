import sys
sys.stdin = open("4861.txt")

def palindrome(N, M):
    for y in range(N):
        for x in range(N - M + 1):
            tempX = ""
            tempY = ""
            for m in range(M):
                if data[y][x + M - 1 - m] != data[y][x + m]:
                    break
                tempX += data[y][x + m]
            if tempX == tempX[-1::-1] and len(tempX) == M:
                return tempX
            for m in range(M):
                if data[x + M - 1 - m][y] != data[x + m][y]:
                    break
                tempY += data[x + m][y]
            if tempY == tempY[-1::-1] and len(tempY) == M:
                return tempY

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(str, input())) for _ in range(N)]
    print("#{} {}".format(tc, palindrome(N, M)))
