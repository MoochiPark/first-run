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
            p1 = stack.pop()
            if p1 == '(':
                break
            else:
                print(p1, end=" ")
    elif not token.isdigit():
        for n in range(len(stack)):
            tmp = stack[-1]
            if outPriority[token] <= inPriority[tmp]:
                print(tmp, end=" ")
                del stack[n]
            else:
                break

        stack.append(token)

while stack:
    p3 = stack.pop()
    print(p3, end=" ")
