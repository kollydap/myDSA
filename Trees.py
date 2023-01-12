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
