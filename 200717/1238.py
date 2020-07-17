import sys
sys.stdin = open("1238.txt")

def bfs(s):
    global visited
    queue = []
    queue.append(s)
    visited[s] = 1
    while queue:
        node = queue.pop(0)
        for i in range(101):
            if matrix[node][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[node] + 1
    idx = 0
    maxN = 0
    for i in range(len(visited)):
        if visited[i] >= maxN:
            maxN = visited[i]
            idx = i
    return idx

for tc in range(1, 11):
    L, S = map(int, input().split())
    data = list(map(int, input().split()))
    matrix = [[0] * 101 for _ in range(101)]
    visited = [0] * 101
    for i in range(0, len(data), 2):
        matrix[data[i]][data[i+1]] = 1
    print("#{} {}".format(tc, bfs(S)))
