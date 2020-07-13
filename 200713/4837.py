import sys
sys.stdin = open('4837.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    data = [1,2,3,4,5,6,7,8,9,10,11,12]
    dataLen = len(data)
    for i in range(1 << dataLen):
        sumN = 0
        cnt = 0
        for j in range(dataLen):
            if i & (1 << j):
                sumN += data[j]
                cnt += 1
                if sumN > K or cnt > N:
                    break
        if cnt == N and sumN == K:
            ans += 1
    print("#{} {}".format(tc, ans))