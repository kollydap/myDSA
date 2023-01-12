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
