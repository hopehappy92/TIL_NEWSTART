import sys
sys.stdin = open("5105.txt")

def bfs(y, x):
    global ans, N
    queue = []
    queue.append([y,x])
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            newY = y + dy[i]
            newX = x + dx[i]
            if not (0 <= newY <= N - 1 and 0 <= newX <= N - 1):
                continue
            if maze[newY][newX] != 1 and not visited[newY][newX]:
                if maze[newY][newX] == 3:
                    ans = visited[y][x]
                    return
                visited[newY][newX] = visited[y][x] + 1
                queue.append([newY, newX])


dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = 0
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                bfs(y, x)
                break
        if ans:
            break
    print("#{} {}".format(tc, ans))