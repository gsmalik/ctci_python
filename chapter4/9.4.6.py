import random, graphs


def find_next_visit(node):
    """
    Function to print next node in a bst.

    Parameters
    ----------
    node: ``Node``
        Node of a BST.

    Time Complexity
    ---------------
    O(d), where d is the maximum depth of the BST. In the worst case, you may have to
    traverse all levels of the BST.

    Space Complexity
    ---------------
    O(d), where d is the maximum depth of the BST. In the worst case, you may have to
    traverse all levels of the BST while doing in-order traversal.
    """
    print(f"Next node after {node.value}: ", end="")
    # Check if right child exists and perform in-order traversal on that because
    # in-order traversal means left->node(this)->right
    if node.right:
        graphs.in_order(node.right)
        return

    # If there is no right child, in-order traversal means that we need to climb up.
    # This being a BST means that the next unvisited node will need to be bigger than
    # the value of current node. This is derived from in-oder traversal of a BST.
    while node.parent:
        if node.parent.value > node.value:
            break
        node = node.parent
    # Check if I have reached root of tree, which means the original node was the
    # rightmost leaf node and there is nothing more to traverse.
    if node.parent is None:
        print("None")
        return
    print(node.value)


# Represent BST using an array for easy access to parent without too much coding
N = 10
bst_test = list(range(N))

# For N=10, the tre looks like below
#           -----5-----
#          |          |
#       ---2---    ---8---
#      |      |    |     |
#     -1      4   -7     9
#    |           |
#    0           6

bst = graphs.create_bst(bst_test, None)
# 9
find_next_visit(bst.right.right)
# 7
find_next_visit(bst.right.left)
# 0
find_next_visit(bst.left.left.left)
# 4
find_next_visit(bst.left.right)
