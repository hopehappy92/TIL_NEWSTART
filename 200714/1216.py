import sys
sys.stdin = open("1216.txt")

def palindrome():
    for n in range(100, -1, -1):
        for y in range(100 - n + 1):
            for x in range(100 - n + 1):
                tempX = ""
                tempY = ""
                for m in range(n):
                    if data[y][x+m] != data[y][x + n - 1 - m]:
                        break
                    tempX += str(data[y][x+m])
                if len(tempX) == n and tempX == tempX[-1::-1]:
                    return n
                for m in range(n):
                    if data[x+m][y] != data[x + n - 1 - m][y]:
                        break
                    tempY += str(data[x+m][y])
                if len(tempY) == n and tempY == tempY[-1::-1]:
                    return n

for _ in range(1, 11):
    tc = int(input())
    data = [list(map(str, input())) for _ in range(100)]
    print("#{} {}".format(tc, palindrome()))