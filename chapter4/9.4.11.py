import numpy as np


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_size = 0
        self.right_size = 0


class BinarySearchTree:
    def __init__(self, val):
        self.root_node = Node(val)

    def insert(self, node):
        current_node = self.root_node
        while True:
            if current_node.val > node.val:
                current_node.left_size += node.left_size + node.right_size + 1
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = node
                    break
            else:
                current_node.right_size += node.left_size + node.right_size + 1
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = node
                    break

    def randomly_select(self, node):
        tree_size = node.left_size + node.right_size + 1
        dice = np.random.multinomial(
            1,
            [1 / tree_size, node.left_size / tree_size, node.right_size / tree_size],
            size=1,
        )[0]
        if dice[0] == 1:
            return node
        if dice[1] == 1:
            return self.randomly_select(node.left)
        else:
            return self.randomly_select(node.right)

    def delete_node(self, node):
        current_node = self.root_node
        while current_node.left != node and current_node.right != node:
            if current_node.val > node.val:
                current_node.left_size -= node.left_size + node.right_size + 1
                current_node = current_node.left
            else:
                current_node.right_size -= node.left_size + node.right_size + 1
                current_node = current_node.right

        if current_node.left == node:
            current_node.left_size -= node.left_size + node.right_size + 1
            current_node.left = None
        else:
            current_node.right_size -= node.left_size + node.right_size + 1
            current_node.right = None

        if node.left:
            self.insert(node.left)
        if node.right:
            self.insert(node.right)
        # self.insert(node)

    def return_random_node(self):
        return self.randomly_select(self.root_node)

    def find(self, val):
        self.find_node = self.root_node
        while True:
            if self.find_node is None:
                print(f"Cannot find {val}")
                return None
            if self.find_node.val == val:
                print(f"Found {val}")
                return self.find_node
            if self.find_node.val > val:
                self.find_node = self.find_node.left
            else:
                self.find_node = self.find_node.right

    def bft(self):
        bft_q = [self.root_node]
        while bft_q:
            currentNode = bft_q[0]
            print(
                currentNode.val,
                currentNode.left_size,
                currentNode.right_size,
                currentNode.count,
            )
            if currentNode.left:
                bft_q.append(currentNode.left)
            if currentNode.right:
                bft_q.append(currentNode.right)
            bft_q.pop(0)


# Test Inserts
myBST = BinarySearchTree(2)
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
myBST.bft()
node = myBST.root_node.left.left
print(f"deleting {node.val}")
myBST.delete_node(node)
myBST.bft()
print(f"generating random node: {myBST.return_random_node().val}")
