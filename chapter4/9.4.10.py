from binarytree import tree


def check_subtree(node_1, node_2):
    """

    Function to check if a tree is subtree of another.
    Parameters
    ----------
    node_1: ``Node``
        Node of the larger tree.
    node_1: ``Node``
        Node of the potential sub-tree.

    Returns
    -------
    True if sub-tree. False otherwise.

    Time Complexity:
    ---------------
    O(N), where N is the number of nodes in `node_1` tree.

    Space Complexity:
    ----------------
    O(log(N)), where N is the number of nodes in `node_1` tree.

    """
    if not node_1:
        return False
    # Launch a traversal comparison if values match.
    if node_1.value == node_2.value:
        if compare_traversal(node_1, node_2):
            return True
    # Check if node_2 is sub-tree of `node_1.left`
    if check_subtree(node_1.left, node_2):
        return True
    # Check if node_2 is sub-tree of `node_1.right`
    if check_subtree(node_1.right, node_2):
        return True
    # No sub-tree
    return False


def compare_traversal(node_1, node_2):
    """
    Function to compare if traversal of two trees is identical.

    Parameters
    ----------
    node_1: ``Node``
        One of the two nodes to check for traversal equality.
    node_2: ``Node``
        The second of the two nodes to check for traversal equality.

    Returns:
    -------
    True if traversal is identical. False otherwise.

    Time Complexity:
    ---------------
    O(N), when N is the number of nodes in the trees and traversal is identical.

    Space Complexity:
    ----------------
    O(log(N)), when N is the number of nodes in the trees and traversal is identical.
    """
    if (not node_1) and (not node_2):
        return True
    # For an identical tree, we cannot have one of the nodes becoming None while
    # other is a Node object
    if (node_1 and not node_2) or (not node_1 and node_2):
        return False
    # If values do not match, that is also False.
    if node_1.value != node_2.value:
        return False
    # If values match for this node as well as for left and right children of
    # the two nodes, that means that the traversal is same. Return True.
    if (
        node_1.value == node_2.value
        and compare_traversal(node_1.left, node_2.left)
        and compare_traversal(node_1.right, node_2.right)
    ):
        return True


tree_1 = tree(height=4)
tree_2 = tree(height=4)
tree_2.levels[0][0].value = tree_1.levels[0][0].value

print(tree_1)
print(tree_2)

# Testing for actually subtree
print(check_subtree(tree_1.levels[0][0], tree_1.levels[2][0]))
# Testing for not subtree
print(check_subtree(tree_1.levels[0][0], tree_2.levels[0][0]))
