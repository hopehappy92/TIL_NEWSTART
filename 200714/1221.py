import sys
sys.stdin = open("1221.txt")

T = int(input())
for _ in range(1, T + 1):
    tc, N = input().split()
    data = list(map(str, input().split()))
    lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    ansList = [0] * 10
    for i in data:
        ansList[lst.index(i)] += 1

    print(tc, end=" ")
    for i in range(10):
        print((lst[i] + " ") * ansList[i], end=" ")
    print()


# lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# T = int(input())
# for _ in range(1, T + 1):
#     tc, N = input().split()
#     data = list(map(str, input().split()))
#     # ansList = [0] * 10
#     # for i in data:
#     #     ansList[lst.index(i)] += 1
#
#     print(tc, end=" ")
#     for i in range(10):
#         print((lst[i] + " ") * data.count(lst[i]), end=" ")
#     print()