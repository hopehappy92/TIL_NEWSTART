import sys
sys.stdin = open("1226.txt")

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def dfs(y, x):
    global ans
    visited[y][x] = 1
    if maze[y][x] == 3:
        ans = 1
        return
    for i in range(4):
        newY = y + dy[i]
        newX = x + dx[i]
        if not (0 <= newY <= 15 and 0 <= newX <= 15):
            continue
        if maze[newY][newX] != 1 and not visited[newY][newX]:
            dfs(newY, newX)

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    flag = 0
    ans = 0
    for y in range(16):
        for x in range(16):
            if maze[y][x] == 2:
                flag = 1
                dfs(y, x)
            if flag:
                break
        if flag:
            break
    print("#{} {}".format(tc, ans))

