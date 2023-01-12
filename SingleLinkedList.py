
import Student

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertStudent(self,name,age,grade,location):
        newStudent = Student(name,age,grade)
        newNode = Node(newStudent)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            # if we want to insert into first position
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                # to set node at the end
            elif location == 1:
                # every LastNode Has A Null Value
                newNode.next = None
                # set the former tail to reference new node
                self.tail.Next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                count = 0
                while count < location-1:
                    tempNode = tempNode.Next
                    count += 1
                nextNode = tempNode.Next
                tempNode.Next = newNode
                newNode.Next = nextNode



    def insertValue(self, value, location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            # if we want to insert into first position
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                # to set node at the end
            elif location == 1:
                # every LastNode Has A Null Value
                newNode.next = None
                # set the former tail to reference new node
                self.tail.Next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                count = 0
                while count < location-1:
                    tempNode = tempNode.Next
                    count += 1
                nextNode = tempNode.Next
                tempNode.Next = newNode
                newNode.Next = nextNode

    def traverseLinkedList(self):
        if self.head is None:
            return "No LinkedList Here"
        else:
            node = self.head
            while node is not None:
                print(node.value)
                print(node.next)

    def searchLinkedList(self, value):
        if self.head is None:
            return "No LinkedList Here"
        else:
            node = self.head
            num = 0
            while node is not None:
                if node.value == value:
                    print(f" {num},  {node.value}")
                    return
                num = num + 1
                node = node.next


# node1 = Node(3)
# node2 = Node(15)
# node3 = Node(30)
# singlyLinkedList = SLinkedList()
# singlyLinkedList.head = node1
# singlyLinkedList.tail = node3
# node1.next = node2
# node2.next = node3
# print([node.value for node in singlyLinkedList])

s1 = SLinkedList()
s1.insertStudent("kola",23,"B+",0)
s1.insertStudent("kolawole",20,"A+",1)
s1.insertStudent("Osagie",26,"C",1)
print([node.value.name for node in s1])

