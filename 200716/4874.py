import sys
sys.stdin = open("4874.txt")

def forth(code):
    stack = []
    for i in code:
        if i == "+" or i == "*" or i == "-" or i == "/":
            if len(stack) < 2:
                return "error"
            num1 = stack.pop()
            num2 = stack.pop()
            if i == "+":
                stack.append(num2 + num1)
            elif i == "*":
                stack.append(num2 * num1)
            elif i == "-":
                stack.append(num2 - num1)
            else:
                stack.append(num2 // num1)
        elif i == ".":
            if len(stack) == 1:
                return stack[0]
            else:
                return "error"
        else:
            stack.append(int(i))

T = int(input())
for tc in range(1, T + 1):
    data = list(input().split())
    print("#{} {}".format(tc, forth(data)))
