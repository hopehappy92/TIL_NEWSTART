import sys
sys.stdin = open('4835.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    ansList = []
    temp = 0
    for i in range(M):
        temp += data[i]
    ansList = [temp]
    for i in range(1, N-M+1):
        ansList.append(ansList[len(ansList)-1]-data[i-1]+data[i+M-1])
    print("#{} {}".format(tc, max(ansList) - min(ansList)))
