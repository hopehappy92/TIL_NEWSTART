import sys
sys.stdin = open('4828.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    maxN = 0
    minN = 987654321
    for i in range(N):
        if data[i] > maxN:
            maxN = data[i]
        elif data[i] < minN:
            minN = data[i]
    print('#{} {}'.format(tc+1,maxN-minN))