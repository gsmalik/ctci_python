class Node:
    def __init__(self, value, rank):
        self.value = value
        self.rank = rank
        self.left = None
        self.right = None
        self.left_len = 0
        self.right_len = 0


class Track:
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
        node = self.root
        rank = 0
        while node.value != value:
            rank = rank + node.left_len

            if value < node.value:
                rank -= node.right_len
                node = node.left
            else:
                rank += 1
                node = node.right
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

print(track.get_rank(9))