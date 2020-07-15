import sys
sys.stdin = open("4866.txt")

def check():
    stack = []
    for i in data:
        if not len(stack) and (i == ")" or i == "}" or i == "]"):
            return 0
        if i == "(" or i == "{" or i == "[":
            stack.append(i)
        elif i == ")" or i == "}" or i == "]":
            if stack[-1] == "(" and i == ")":
                stack.pop(-1)
                continue
            elif stack[-1] == "{" and i == "}":
                stack.pop(-1)
                continue
            elif stack[-1] == "[" and i == "]":
                stack.pop(-1)
                continue
            else:
                return 0
    if not len(stack):
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T + 1):
    data = input()
    print("#{} {}".format(tc, check()))

