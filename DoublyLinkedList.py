class Node:
    def __init__(self, value):
        self.value = value
        self.Prev = None
        self.Next = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            if location == 0:
                newNode.Prev = None
                newNode.Next = self.head
                self.head.Prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                newNode.Prev = self.tail
                self.tail = newNode
            else:
                tempNode = self.head
                count = 0
                # this gives us the node before the position we want to place our new node
                while count < location - 1:
                    tempNode = tempNode.Next
                    count += 1
                newNode.Next = tempNode.Next
                tempNode.Next.Prev = newNode
                tempNode.Next = newNode
                newNode.Prev = tempNode