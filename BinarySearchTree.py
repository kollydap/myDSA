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