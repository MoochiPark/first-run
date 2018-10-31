import re

plusMinus = re.compile('[+-]')
mulDiv = re.compile('[*/]')


expression = list(input("수식을 입력하세요 >> ").split())
stack = []

for token in expression:
    if token.isdigit():
        print(token, end=" ")
    elif not token.isdigit():
        if plusMinus.match(token):
            # if '(' not in stack and '*' in stack:
            #
            # else:
                stack.append(token)

        elif mulDiv.match(token):
            stack.append(token)

        elif token == ")":
            while True:
                p2 = stack.pop()

                if p2 == "(":
                    break
                else:
                    print(p2, end=" ")
        else:
            stack.append(token)
    # print(stack)


while stack:
    p3 = stack.pop()
    print(p3, end=" ")