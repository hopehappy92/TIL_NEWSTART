import sys
sys.stdin = open('4831.txt')

def find(ans, currentLocation):
    exiting = False
    while not exiting:
        for i in range(K, -1, -1):
            if i == 0:
                return 0
            flag = False
            for stopIndex in range(len(busStop) - 1, -1, -1):
                if currentLocation + i == busStop[stopIndex]:
                    ans += 1
                    currentLocation += i
                    flag = True
                    break
            if flag == True:
                break
        if currentLocation + K >= N:
            exiting = True
    return ans

T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    busStop = list(map(int, input().split()))

    answer = find(0, 0)

    print('#{} {}'.format(tc+1, answer))
