import sys
sys.stdin = open("1259.txt")

def dfs(ansList,dataList):
    if len(ansList) == N * 2:
        return ansList
    else:
        for i in range(0, len(dataList), 2):
            if dataList[i] == ansList[-1]:
                ansList.append(dataList[i])
                ansList.append(dataList[i+1])
                del dataList[dataList.index(i)]
                break
        return dfs(ansList, dataList)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    startList = []
    endList = []
    for i in range(0, len(data), 2):
        startList.append(data[i])
        endList.append(data[i+1])
    for i in startList:
        if i not in endList:
            startPoint = i
    print(startPoint)