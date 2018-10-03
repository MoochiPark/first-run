class Node:
    def __init__(self, coef, degree):
        self.coef = coef
        self.degree = degree
        self.next = None


class LinkedList:
    def __init__(self):
        HeadNode = Node("HEAD", "HEAD")
        self.head = HeadNode
        self.tail = HeadNode
        self.NumOfData = 0

    def insert(self, coef, degree):
        insertNode = Node(coef, degree)
        self.tail.next = insertNode
        self.tail = insertNode
        self.NumOfData += 1

    def printList(self):
        current = self.head
        if self.NumOfData == 0:
            print("List is empty!")
            return None
        print("HEAD::", end='')
        for i in range(self.NumOfData - 1):
            print(current.next.coef, "->", end='')
            current = current.next
        print(current.next.coef)


def polyAdd(pA, pB, pR):
    f1 = pA.head
    f2 = pB.head
    ret = pR.head
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

polyAdd(pListA, pListB, pReturn)

pReturn.printList()

