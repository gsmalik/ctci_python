class Node:
    """
    Node data structure to construct BST

    Parameters
    ----------
    value: FP32
        Value of the node.
    """

    def __init__(self, value):
        self.value = value
        # pointers to other nodes
        self.left = None
        self.right = None
        # to keep track of ranks
        self.left_len = 0
        self.right_len = 0


class Track:
    """
    Class to keep a track of each incoming number.
    """

    def __init__(self):
        self.root = None

    def track(self, value):
        """
        Function to track streaming numbers. Mostly uses 'insert_bst'
        """
        if self.root:
            self.insert_bst(value)
        else:
            self.root = Node(value)

    def insert_bst(self, value):
        """
        Function to insert an element into the BST.

        Parameters
        ----------
        value: FP32
            The value to insert.

        Time Complexity
        ---------------
        O(logN), where N is the number of elements in the BST.

        Space Complexity
        ---------------
        O(logN), where N is the number of elements in the BST.
        """
        node = self.root
        while True:
            # go left if value is smaller than current node's value
            if value < node.value:
                # increase the 'left' length of node
                node.left_len += 1
                if node.left:
                    node = node.left
                else:
                    node.left = Node(value)
                    break
            # go right if value is bigger than current node's value
            else:
                # increase the 'right' length of node
                node.right_len += 1
                if node.right:
                    node = node.right
                else:
                    node.right = Node(value)
                    break

    def get_rank(self, value):
        """
        Function to get a rank of value.

        Parameters
        ----------
        value: FP32
            The value to get a rank for.

        Time Complexity
        ---------------
        O(logN), where N is the number of elements in the BST.

        Space Complexity
        ---------------
        O(logN), where N is the number of elements in the BST.
        """
        node = self.root
        rank = 0
        while node.value != value:
            # if value is greater than current node, all elements that are left
            # children of current node will be smaller than 'value', hence
            # increase rank by that amount. then increase rank by 1 since 'value'
            # is also bigger than current node
            if value >= node.value:
                rank = rank + node.left_len
                rank = rank + 1
                node = node.right
            # if value is smaller, rank stays the same
            else:
                node = node.left
        # once value is found, add the left children of the node to rank since
        # they will be smaller than 'value'
        return rank + node.left_len


track = Track()
track.track(5)
track.track(1)
track.track(4)
track.track(4)
track.track(5)
track.track(9)
track.track(7)
track.track(13)
track.track(3)
track.track(6)
print(track.get_rank(1))
print(track.get_rank(3))
print(track.get_rank(6))
print(track.get_rank(13))