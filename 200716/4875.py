import sys
sys.stdin = open("4875.txt")

dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def dfs(y, x):
    global ans
    visited[y][x] = 1
    if ans:
        return
    if maze[y][x] == 3:
        ans = 1
        return
    for i in range(4):
        newY = y + dy[i]
        newX = x + dx[i]
        if not (0 <= newY <= N - 1 and 0 <= newX <= N - 1):
            continue
        if maze[newY][newX] != 1 and visited[newY][newX] == 0:
            dfs(newY, newX)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = 0
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                dfs(y, x)
                break
        if ans:
            break
    print("#{} {}".format(tc, ans))