import sys
sys.stdin = open("4873.txt")

T = int(input())
for tc in range(1, T + 1):
    s = input()
    # flag = True
    # while flag:
    #     temp = 0
    #     for w in range(len(s)-1):
    #         if s[w] == s[w+1]:
    #             s = s[:w] + s[w+2:]
    #             temp = 1
    #             break
    #     if not temp:
    #         flag = False
    #
    # print("#{} {}".format(tc, len(s)))

    stack = []
    for i in s:
        if not len(stack):
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop(-1)
            else:
                stack.append(i)
    print("#{} {}".format(tc, len(stack)))
