import sys
sys.stdin = open("1210.txt")

# flag쓰는게 더 빠르네?

dy = [0, 0, 1]
dx = [1, -1, 0]

def dfs(y, x):
    global cnt, flag
    cnt += 1
    visited[y][x] = 1
    if ladder[y][x] == 2:
        flag = 1
        return
    for i in range(3):
        newY = y + dy[i]
        newX = x + dx[i]
        if not (0 <= newY <= 99 and 0 <= newX <= 99):
            continue
        if ladder[newY][newX] and visited[newY][newX] == 0:
            return dfs(newY, newX)

for _ in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    flag = 0
    ans = 0
    cnt = 0
    for i in range(100):
        visited = [[0] * 100 for _ in range(100)]
        if ladder[0][i]:
            dfs(0, i)
            if flag == 1:
                ans = i
                break
    print("#{} {}".format(T, ans))
    print(cnt)