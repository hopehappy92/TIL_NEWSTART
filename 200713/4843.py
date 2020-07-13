import sys
sys.stdin = open("4843.txt")

def sorting(n):
    for i in range(n):
        if i % 2 == 0:
            limit = 0
            for j in range(i, n):
                if limit < data[j]:
                    limit = data[j]
                    temp = j
            data[temp], data[i] = data[i], data[temp]
        else:
            limit = 1000
            for j in range(i, n):
                if limit > data[j]:
                    limit = data[j]
                    temp = j
            data[temp], data[i] = data[i], data[temp]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    sorting(N)

    print("#{}".format((tc)), end=" ")
    for i in range(10):
        print(data[i], end=" ")
    print()
