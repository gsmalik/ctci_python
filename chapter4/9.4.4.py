from binarytree import tree


def check_height(node):
    """
    Function to check if binary tree is balanced by confirming that the left subtree's
    height does not differ from the right subtree's height by a magnitude of 1 for each
    node

    Parameters
    ----------
    node: ``Node``
        Root node of balanced tree

    Time Complexity
    ---------------
    O(N), where N is the number of nodes in the binary tree. In the worst case, you may
    have a balanced tree, which would require you to visit each node in the tree.

    Space Complexity
    ---------------
    O(log(N)), where N is the number of vertices in graph. We can have a stack depth of
    recursive calls of O(log(N)) and at each depth we only use constant 4 variables to
    keep tree of left and right subtrees' height and balance properties.
    """
    # Determine height and if left subtree is balanced.
    (left_balanced, left_height) = check_height(node.left) if node.left else (True, 0)
    # Determine height and if right subtree is balanced.
    (right_balanced, right_height) = (
        check_height(node.right) if node.right else (True, 0)
    )

    # Return height of current subtree starting from `node` and wether it is balanced.
    return (
        (left_balanced and right_balanced and abs(left_height - right_height) <= 1),
        max(left_height, right_height) + 1,
    )


my_tree = tree(height=3)
print(my_tree)
print(check_height(my_tree.levels[0][0]))
