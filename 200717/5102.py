import sys
sys.stdin = open("5102.txt")

def bfs(s, g, v):
    queue = []
    queue.append(s)
    visited[s] = 1
    while queue:
        node = queue.pop(0)
        if node == g:
            return visited[node] - 1
        for i in range(v + 1):
            if data[node][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[node] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        s, g = map(int, input().split())
        data[s][g] = 1
        data[g][s] = 1
    S, G = map(int,input().split())
    print("#{} {}".format(tc, bfs(S, G, V)))
