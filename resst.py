# valid = True
# while valid:
#     userInput = input("input a number")
#     if userInput[0] == '-':
#         print("negative number")
#     elif userInput == "Quit":
#         valid = False
#     else:
#         print("positive number")

# myList = [1, 2, 3.5, 7, 8.876]


# def myListLoop(mylist):
#     for i in mylist:
#         print(i)


# def myListLoop2(mylist):
#     newList = myList[2:6]
#     for i in newList:
#         print(i)


# def myLooper(myList: list, target: int):
#     for i in range(len(myList)):
#         for j in range(i+1, len(myList)):
#             if myList[i] + myList[j] == target:
#                 print(i, j, myList[i], myList[j])


def getMaxValue(myList):
    maxSum = 0
    bigNum = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] > maxSum:
                maxSum = myList[i] + myList[j]
                bigNum.append(i)
                bigNum.append(j)
    bigNum.reverse()
    return bigNum[0], bigNum[1]


def getThreeSum(myList, target):
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            for k in range(j+1, len(myList)):
                if myList[i] + myList[j] + myList[k] == target:
                    print(myList[i], myList[j], myList[k])
                    return i, j, k
    return "Not Found"


def getMaxValue(myList):
    maxSum = 0

    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] > maxSum:
                maxSum = myList[i] + myList[j]
                pairs = str(i) + " " + str(j)
    return pairs


def containsDuplicate(arr: list) -> bool:
    """
    Checks if A List Contains Duplicate
    """
    ar = []
    for a in arr:
        if a in ar:
            return True
        else:
            ar.append(a)
    return False


class TreeNode:
    def __init__(self, data, children=[]) -> None:
        self.data = data
        self.children = children

    def __str__(self, level=0) -> str:
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def insertChild(self, TreeNode):
        self.children.append(TreeNode)


tree = TreeNode("Drinks")
hot = TreeNode("Cofee")
smallZobo = TreeNode("SmallZobo")
bigZobo = TreeNode("BigZobo")
zobo = [smallZobo, bigZobo]
cold = TreeNode("Zobo", [zobo, zobo])


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild


def preOrdertraverse(rootNode: TreeNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrdertraverse(rootNode.leftChild)
    preOrdertraverse(rootNode.rightChild)


def inOrdertraverse(rootNode: TreeNode):
    if not rootNode:
        return
    inOrdertraverse(rootNode.leftChild)
    print(rootNode.data)
    inOrdertraverse(rootNode.rightChild)


def postOrdertraverse(rootNode: TreeNode):
    if not rootNode:
        return
    postOrdertraverse(rootNode.leftChild)
    postOrdertraverse(rootNode.rightChild)
    print(rootNode.data)


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insertChild(self, child):
        if self.data == None:
            self.data = child.data
        elif child.data > self.data:
            self.rightChild = child
        elif child.data < self.data:
            self.rightChild = child

    def addChild(self, data):
        if self.data == None:
            self.data = data

        elif data > self.data:
            if self.rightChild == None:
                # if we dont have a rightnode we create one
                self.rightChild = BinarySearchTree(data)
            else:
                self.addChild(self.rightChild, data)
        else:
            if self.leftChild == None:
                # if we dont have a rightnode we create one
                self.leftChild = BinarySearchTree(data)
            else:
                self.addChild(self.leftChild, data)
        return "the node has been successfully inserted"
class Student:

    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    

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


class ListBinaryTree:
    def __init__(self, size: int):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value) -> str:
        if self.lastUsedIndex + 1 == self.maxSize:
            print("binary tree is full")
            return "Binary Tree Is Full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        print("successfully inserted")
        return "successfully inserted"

    def traverse(self):
        for val in self.customList:
            print(val)

    def linearsearch(self, value):
        for val in self.customList:
            if val == value:
                print(f"your {val} was found")
                return val

    def preOrderTraversal(self, index: int):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)


# lbt1 = ListBinaryTree(9)
# lbt1.insertNode("Mood")
# lbt1.insertNode("happy")
# lbt1.insertNode("sad")
# lbt1.insertNode("playing")
# lbt1.insertNode("having fun")
# lbt1.traverse()
# lbt1.traverse()
# lbt1.linearsearch("sad")
# lbt1.preOrderTraversal(1)

# class Graph:
#     def __init__(self,gdict=None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict
    
#     def addEdge(self,vertex,edge):
#         '''
#         Adds Edge to A given Vertex
#         '''
#         self.gdict[vertex].append(edge)

# dt = {"a":["b","c"],
#     "b":["a","d","e"],
#     "c":["a","e"],
#     "d":["b","e","f"],
#     "e":["d","f","c"],
#     "f":["d","e"]
# }
# gp = Graph(dt)
# gp1 = Graph()
# gp1.addEdge("a","k")
# print(gp1.gdict)