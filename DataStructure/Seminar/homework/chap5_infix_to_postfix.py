expression = list(input("수식을 입력하세요 >>  ").split())
stack = []
inPriority = {'(': 0, ')': 4, '*': 2, '/': 2, '+': 1, '-': 1}
outPriority = {'(': 5, ')': 4, '*': 2, '/': 2, '+': 1, '-': 1}

for token in expression:
    if token.isdigit():
        print(token, end=" ")
        continue
    elif token == ")":
        while stack:
            top = stack.pop()
            if top == '(':
                break
            else:
                print(top, end=" ")
    elif not token.isdigit():
        for n in range(len(stack)):
            tmp = stack[-1]
            if outPriority[token] <= inPriority[tmp]:
                print(tmp, end=" ")
                stack.pop()
            else:
                break
        stack.append(token)

while stack:
    print(stack.pop(), end=" ")
