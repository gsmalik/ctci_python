from binarytree import tree, bst


def check_bst(node):
    """
    Function to check if binary tree is BST.

    Parameters
    ----------
    node: ``Node``
        Root node of binary tree.

    Time Complexity
    ---------------
    O(N), where N is the number of nodes in the binary tree. In the worst case, you may
    have a BST, which would require you to visit each node in the tree.

    Space Complexity
    ---------------
    O(log(N)), where N is the number of vertices in graph. We can have a stack depth of
    recursive calls of O(log(N)) and at each depth we only use constant 6 variables to
    keep tree of left and right subtrees' BST characteristics and values.
    """
    # Check wether left subtree maintained its BST properties and note value
    # of left root node of left subtree.
    (left_val, left_bst) = check_bst(node.left) if node.left else (None, True)
    # Check wether right subtree maintained its BST properties and note value
    # of right root node of right subtree.
    (right_val, right_bst) = check_bst(node.right) if node.right else (None, True)

    # Construct BST property check for this node.
    node_greater_left = left_val is None or left_val < node.value
    right_greater_node = right_val is None or right_val > node.value

    return (
        node.value,
        node_greater_left and right_greater_node and left_bst and right_bst,
    )


# Generate binary search tree
my_tree = bst(height=5)
print(my_tree)
# This should be True
print(check_bst(my_tree.levels[0][0]))

# Generate binary search tree
my_tree = bst(height=5)
# Intentionally make it non BST
my_tree.levels[1][0].value = my_tree.levels[0][0].value + 1
print(my_tree)
# This should be False
print(check_bst(my_tree.levels[0][0]))
