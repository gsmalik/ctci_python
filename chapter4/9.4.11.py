import numpy as np
import graphs


class Node(graphs.BinaryNode):
    """Just add attribute to track size of left and right subtrees"""

    def __init__(self, value):
        super().__init__(value)
        self.left_size = 0
        self.right_size = 0


class BinarySearchTree:
    """
    Implementation of a Binary Search Tree,

    Parameters
    ----------
    val: ``FP32``
        Value of root node of BST.

    Space Complexity:
    O(N), where N is the current number of nodes in the BST.
    """

    def __init__(self, val):
        self.root_node = Node(val)

    def insert(self, node):
        """
        Inserts a node in the BST while following BST principles.

        Parameters
        ----------
        node: ``Node``
            Node to be inserted.

        Time Complexity
        ---------------
        O(D), where D is the longest path in the tree. For a balanced BST, D is log(N).
        """
        current_node = self.root_node
        while True:
            # if node is smaller, move to left and increment size
            if current_node.value > node.value:
                current_node.left_size += node.left_size + node.right_size + 1
                if current_node.left:
                    current_node = current_node.left
                # Break if empty slot found
                else:
                    current_node.left = node
                    break
            # if node is bigger, move to right and increment size
            else:
                current_node.right_size += node.left_size + node.right_size + 1
                if current_node.right:
                    current_node = current_node.right
                # Break if empty slot found
                else:
                    current_node.right = node
                    break

    def randomly_select(self, node):
        """
        Function to randomly select a node from given BST with equal probability

        Parameters
        ----------
        node: ``Node``
            Starting node for random selection.

        Time Complexity
        ---------------
        It makes more sense to calculate average time complexity here. For simplicity,
        we can assume a balanced BST here. Since there is equal probability  for any
        node to be selected, over large number of trials averaging it, we will get:
        (samples/D)*(1+2+3+4+5+...D)/(samples) = O(D), where D = log(N) is number of
        levels in the BST.
        """
        # Have a 3 sided dice roll where probability of choosing a node is 1/size.
        # Probability of choosing to do another dice roll on left is left_size/size and
        # probability of choosing to do another dice roll on right is right_size/size.
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
        """
        Function to delete a node from the BST and re-insert children of deleted nodes.

        Parameters
        ----------
        node: ``Node``
            Node to be deleted from the BST.

        Time Complexity
        ---------------
        O(log(N)) where N is number of nodes in BST.

        """
        current_node = self.root_node
        # Find parent node whose child is node we want to delete
        while current_node.left != node and current_node.right != node:
            if current_node.value > node.value:
                current_node.left_size -= node.left_size + node.right_size + 1
                current_node = current_node.left
            else:
                current_node.right_size -= node.left_size + node.right_size + 1
                current_node = current_node.right

        # Delete the node and reduce parent size accordinly
        if current_node.left == node:
            current_node.left_size -= node.left_size + node.right_size + 1
            current_node.left = None
        else:
            current_node.right_size -= node.left_size + node.right_size + 1
            current_node.right = None

        # Reinsert children of deleted node.
        if node.left:
            self.insert(node.left)
        if node.right:
            self.insert(node.right)

    def return_random_node(self):
        """Returns random node in the entire BST"""
        return self.randomly_select(self.root_node)

    def find(self, val):
        """
        Find and return node with given value

        Parameters
        ----------
        val: ``FP32``
            Value to search for

        Returns
        -------
        Node with value if found. None otherwise.

        Time Complexity
        ---------------
        O(log(N)) for a balanced BST.
        """
        self.find_node = self.root_node
        while True:
            if self.find_node is None:
                print(f"Cannot find {val}")
                return None
            if self.find_node.value == val:
                print(f"Found {val}")
                return self.find_node
            if self.find_node.value > val:
                self.find_node = self.find_node.left
            else:
                self.find_node = self.find_node.right

    def bft(self):
        """Your run-of-the-mill BFT"""
        bft_q = [self.root_node]
        while bft_q:
            currentNode = bft_q[0]
            print(
                currentNode.value,
                currentNode.left_size,
                currentNode.right_size,
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
print(f"deleting {node.value}")
myBST.delete_node(node)
myBST.bft()
print(f"generating random node: {myBST.return_random_node().value}")
