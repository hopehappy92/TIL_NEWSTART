import sys
sys.stdin = open("1267.txt")

for tc in range(1, 11):
    V, E = map(int, input().split())
    edge = list(map(int, input().split()))
    matrix = [[0] * (V + 1) for _ in range(V + 1)]
    check = [0] * (V + 1)
    ans = ""
    stack = []
    for i in range(0, len(edge), 2):
        matrix[edge[i]][edge[i+1]] = 1
        check[edge[i+1]] += 1
    for i in range(1, len(check)):
        if not check[i]:
            stack.append(i)
    while len(stack):
        currentNode = stack.pop(0)
        ans += str(currentNode) + " "
        for nextNode in range(1, V + 1):
            if matrix[currentNode][nextNode]:
                check[nextNode] -= 1
                if not check[nextNode]:
                    stack.append(nextNode)
    print("#{} {}".format(tc, ans))
