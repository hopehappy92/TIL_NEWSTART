import sys
sys.stdin = open("1224.txt")

# 다시 고민해보기
# 한번에 가는 방법이있음
# 기호의 우선순위랑 계산방법



def priority(v):
    if v == "+":
        return 1
    elif v == "*":
        return 2
    elif v == "(":
        return 0


for tc in range(1, 11):
    N = int(input())
    code = list(input())
    postfixList = []
    postfixStack = []
    ansStack = []

    for i in range(len(code)):
        if code[i].isdigit():
            postfixList.append(code[i])
        else:
            if code[i] == "(":
                postfixStack.append(code[i])
            elif code[i] == ")":
                while postfixStack[-1] != "(":
                    postfixList.append(postfixStack.pop())
                postfixStack.pop()
            else:
                if postfixStack:
                    while priority(code[i]) <= priority((postfixStack[-1])) and postfixStack:
                        postfixList.append(postfixStack.pop())
                    postfixStack.append(code[i])
                    
    for i in postfixList:
        if i.isdigit():
            ansStack.append(int(i))
        else:
            num1 = ansStack.pop()
            num2 = ansStack.pop()
            if i == "+":
                ansStack.append(num1 + num2)
            else:
                ansStack.append(num1 * num2)
    print("#{} {}".format(tc, ansStack[0]))






    # stack = []
    # i = 0
    # while i != N:
    #     if code[i] in nums:
    #         stack.append(code[i])
    #     elif code[i] in operator and code[i+1] in nums:
    #         num = stack.pop()
    #         if code[i] == "+":
    #             stack.append(num + code[i+1])
    #         else:
    #             stack.append(num * code[i+1])
    #         i += 1
    #     elif code[i] in operator and code[i+1] == "(":
    #         tempStack = []
    #         j = i + 2
    #         while code[j] == ")":
    #             if code[j] in nums:
    #                 tempStack.append(code[j])
    #             elif code[j] in operator and code[j + 1] in nums:
    #                 num = tempStack.pop()
    #                 if code[j] == "+":
    #                     tempStack.append(num + code[j + 1])
    #                 else:
    #                     tempStack.append(num * code[j + 1])
    #                 j += 1
    #         if code[j+1] == ")":
    #             pass
    #         elif code[j+2] in nums and code[j+1] in operator:
    #             num = stack.pop()
    #             if code[j + 1] == code[i]:
    #                 if code[i] == "+":
    #                     stack.append(num + tempStack[0] + code[j + 2])
    #                 elif code[i] == "*":
    #                     stack.append(num * tempStack[0] * code[j + 2])
    #             elif code[j+1] == "*" and code[i] == "+":
    #                 stack.append(tempStack[0] * code[j + 2] + num)
    #             elif code[j+1] == "+" and code[i] == "*":
    #                 stack.append(tempStack[0] * num + code[j + 2])
    #             i = j + 2
    #         elif code[j+2] == "(" and code[j+1] in operator:
    #             pass
    #     elif code[i] == "(":
    #         pass
    #     i += 1
