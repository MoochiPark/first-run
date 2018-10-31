class Node:
    def __init__(self, coef, degree):
        self.coef = coef
        self.degree = degree
        self.next = None


class LinkedList:
    def __init__(self):
        headNode = Node(None, None)
        self.head = headNode
        self.tail = headNode
        self.count = 0

    def insert(self, coef, degree):
        insertNode = Node(coef, degree)
        self.tail.next = insertNode
        self.tail = insertNode
        self.count += 1

    def printList(self):
        current = self.head
        if self.count == 0:
            print("수식을 입력한 후 시도하세요.")
            return None
        print("result = ", end='')
        for i in range(self.count - 1):
            print("{}x^{} + ".format(current.next.coef, current.next.degree), end='')
            current = current.next
        print(current.next.coef)


def polyAdd(pA, pB):
    f1 = pA.head
    f2 = pB.head
    while f1.next and f2.next:

        if f1.next.degree == f2.next.degree:
            sum = f1.next.coef + f2.next.coef
            pReturn.insert(sum, f1.next.degree)
            f1 = f1.next
            f2 = f2.next
        elif f1.next.degree > f2.next.degree:
            pReturn.insert(f1.next.coef, f1.next.degree)
            f1 = f1.next
        else:
            pReturn.insert(f2.next.coef, f2.next.degree)
            f2 = f2.next

    while f1.next or f2.next:
        if f1.next:
            pReturn.insert(f1.next.coef, f1.next.degree)
            f1 = f1.next
        if f2.next:
            pReturn.insert(f2.next.coef, f2.next.degree)
            f2 = f2.next


pListA = LinkedList()
pListB = LinkedList()
pReturn = LinkedList()

pListA.insert(7, 6)
pListA.insert(3, 5)
pListA.insert(5, 2)

pListB.insert(1, 5)
pListB.insert(2, 4)
pListB.insert(3, 2)
pListB.insert(4, 0)

polyAdd(pListA, pListB)

pReturn.printList()
