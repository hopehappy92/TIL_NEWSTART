import sys
sys.stdin = open("4839.txt")

def binarysearch(goal, left, right, cnt):
    center = int((left + right) / 2)
    cnt += 1
    if center == goal:
        return cnt
    elif center > goal:
        right = center
        return binarysearch(goal, left, right, cnt)
    else:
        left = center
        return binarysearch(goal, left, right, cnt)


T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    left = 1
    right = P
    aCnt = binarysearch(Pa, left, right, 0)
    bCnt = binarysearch(Pb, left, right, 0)
    if aCnt > bCnt:
        print("#{} B".format(tc))
    elif aCnt < bCnt:
        print("#{} A".format(tc))
    else:
        print("#{} 0".format(tc))


