class Node:
    """Node data structure to construct BST"""

    def __init__(self, value, rank):
        self.value = value
        self.rank = rank
        self.left = None
        self.right = None
        self.left_len = 0
        self.right_len = 0


class Track:
    """
    Class to keep a track of each incoming number.
    """

    def __init__(self):
        self.root = None
        self.num_elem = 0

    def track(self, value):
        self.num_elem += 1
        if self.root:
            self.insert_bst(value)
        else:
            self.root = Node(value, 0)

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
            # go left
            if value < node.value:
                rank = node.rank
                node.rank += 1
                node.left_len += 1
                if node.left:
                    node = node.left
                else:
                    node.left = Node(value, rank)
                    break
            # go right
            else:
                rank = node.rank + 1
                node.right_len += 1
                if node.right:
                    node = node.right
                else:
                    node.right = Node(value, rank)
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
            if value >= node.value:
                rank = rank + node.left_len
                rank = rank + 1
                node = node.right
            else:
                node = node.left
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