import numpy as np


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_size = 0
        self.right_size = 0
        self.count = 0

    def returnNode(self):
        treeSize = self.left_size + self.right_size + 1
        dice = np.random.multinomial(
            1,
            [1 / treeSize, self.left_size / treeSize, self.right_size / treeSize],
            size=1,
        )[0]
        if dice[0] == 1:
            self.count += 1
            return self.val
        if dice[1] == 1:
            return self.left.returnNode()
        else:
            return self.right.returnNode()


class BinaryTree:
    def __init__(self, val):
        self.rootNode = Node(val)
        self.currentNode = self.rootNode
        self.paths = ["0"]

    def insert(self, node):
        self.currentNode = self.rootNode
        self.path = self.paths[0]
        while self.currentNode:
            if node.val >= self.currentNode.val:
                self.currentNode.right_size += node.left_size + node.right_size + 1
                if not self.currentNode.right:
                    self.currentNode.right = node
                    self.currentNode = None
                else:
                    self.currentNode = self.currentNode.right
                self.path = self.path + "1"
            else:
                self.currentNode.left_size += node.left_size + node.right_size + 1
                if not self.currentNode.left:
                    self.currentNode.left = node
                    self.currentNode = None
                else:
                    self.currentNode = self.currentNode.left
                self.path = self.path + "0"
        self.currentNode = node
        self.paths.append(self.path)

    def deleteNode(self, node):
        currentNode = self.rootNode
        while currentNode.left != node and currentNode.right != node:
            if currentNode.val > node.val:
                currentNode.left_size -= node.left_size + node.right_size + 1
                currentNode = getattr(currentNode, "left")
            else:
                currentNode.right_size -= node.left_size + node.right_size + 1
                currentNode = getattr(currentNode, "right")

        newNode_left = node.left
        newNode_right = node.right

        if currentNode.left == node:
            currentNode.left_size -= node.left_size + node.right_size + 1
            currentNode.left = None
        else:
            currentNode.right_size -= node.left_size + node.right_size + 1
            currentNode.right = None

        if newNode_left:
            self.insert(newNode_left)
        if newNode_right:
            self.insert(newNode_right)

    def randomly_select(self):
        # choose randomly from self.paths
        return self.rootNode.returnNode()

    def find(self, val):
        self.find_node = self.rootNode
        while self.find_node.val != val and self.find_node is not None:
            if self.find_node.val > val:
                self.find_node = self.find_node.left
            else:
                self.find_node = self.find_node.right

        return self.find_node

    def BFT(self):
        bftQ = [self.rootNode]
        while bftQ:
            currentNode = bftQ[0]
            print(
                currentNode.val,
                currentNode.left_size,
                currentNode.right_size,
                currentNode.count,
            )
            if currentNode.left:
                bftQ.append(currentNode.left)
            if currentNode.right:
                bftQ.append(currentNode.right)
            bftQ.pop(0)


# Test Inserts
myBST = BinaryTree(2)
myBST.insert(Node(1))
myBST.insert(Node(3))
myBST.insert(Node(-1))
myBST.insert(Node(1.5))
myBST.insert(Node(-2))
myBST.insert(Node(-0))
myBST.insert(Node(1.25))
myBST.insert(Node(1.75))
myBST.insert(Node(-3))
myBST.insert(Node(-1.5))
myBST.insert(Node(1.12))

myBST.deleteNode(myBST.rootNode.left.left)
myBST.deleteNode(myBST.rootNode.right)
for _ in range(100000):
    myBST.randomly_select()
myBST.BFT()
