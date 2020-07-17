import sys
sys.stdin = open("5097.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    # idx = M % N

    print("#{} {}".format(tc, data[idx]))