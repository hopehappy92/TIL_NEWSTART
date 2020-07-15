import sys
sys.stdin = open("4871.txt")

def dfs(s, g):
    global ans
    if s == g:
        ans = 1
        return
    for i in range(1, V + 1):
        if ans:
            return
        if data[s][i] == 1 and visited[i] == 0:
            newS = i
            visited[i] = 1
            dfs(newS, g)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    data = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        s, g = map(int, input().split())
        data[s][g] = 1
    start, goal = map(int, input().split())
    ans = 0
    dfs(start, goal)
    print("#{} {}".format(tc, ans))