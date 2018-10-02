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

    def listNum(self):
        print("현재 리스트에는", self.NumOfData, "개의 요소가 있습니다.")
        return self.NumOfData

    def printList(self):
        current = self.head
        if self.NumOfData == 0:
            print("List is empty!")
            return None
        print("HEAD::", end='')
        for i in range(self.NumOfData - 1):
            print(current.next.data, "->", end='')
            current = current.next
        print(current.next.data)


def polyAdd(pA, pB):
    f1 = pA.head
    f2 = pB.head
    print(f1.next.data + f2.next.data)


pListA = LinkedList()
pListB = LinkedList()
pReturn = LinkedList()

pListA.insert(10)
pListB.insert(1)
pListA.insert(9)
pListB.insert(3)
pListA.printList()

sum(pListA, pListB)
