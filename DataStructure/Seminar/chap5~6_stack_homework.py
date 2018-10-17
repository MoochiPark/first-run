import re

pm = re.compile('[+-]')
md = re.compile('[*/]')

ex = list(input("수식을 입력하세요 >> ").split())
stack = []

for n in ex:
    if n.isdigit():
        print(n, end=" ")
    elif not n.isdigit():
        if pm.match(n):
            stack.append(n)

        elif md.match(n):
            stack.append(n)

        elif n == ")":
            while True:
                p2 = stack.pop()

                if p2 == "(":
                    break
                else:
                    print(p2, end=" ")
        else:
            stack.append(n)

while stack:
    p3 = stack.pop()
    print(p3, end=" ")
