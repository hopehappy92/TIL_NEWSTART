import sys
sys.stdin = open("5099.txt")

def bfs(ci, N, M):
    queue = [0] * N
    pizzaQueue = [0] * N
    ovenIdx = 0
    pizzaIdx = 0
    while queue.count(0) != N - 1 or pizzaIdx < M:
        if queue[ovenIdx]:
            queue[ovenIdx] = queue[ovenIdx]//2
        if not queue[ovenIdx] and pizzaIdx < M:
            queue[ovenIdx] = ci[pizzaIdx]
            pizzaQueue[ovenIdx] = pizzaIdx
            pizzaIdx += 1
        ovenIdx = (ovenIdx + 1) % N
    for i in range(len(queue)):
        if queue[i]:
            return pizzaQueue[i] + 1

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ci = list(map(int, input().split()))
    print("#{} {}".format(tc, bfs(ci, N, M)))