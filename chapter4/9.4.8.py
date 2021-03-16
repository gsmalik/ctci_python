from binarytree import tree


def find_common_ancestor(root, node_1, node_2):
    """
    Function to determine if a given node is common ancestor of other nodes.

    Parameters
    ----------
    root: ``Node``
        The node for which we want to determine if it is an ancestor.

    node_1: ``Node``
        The first of the two nodes for which we are determining if `root` is common
        ancestor.
    node_2: ``Node``
        The second of the two nodes for which we are determining if `root` is common
        ancestor.

    Returns
    -------
        (bool(node is ancestor of node_1), bool(node is ancestor of node_2))

    Time Complexity
    ---------------
    O(N), where N is the number of nodes in the tree.

    Space Complexity
    ----------------
    O(log(N)), where N is the number of nodes in the tree.
    """
    # If root is none, it cannot be ancestor of node_1 and node_2
    if root is None:
        return (False, False)

    # Find if root.left is common ancestor of node_1 or node_2
    left_ancestor = find_common_ancestor(root.left, node_1, node_2)
    # Find if root.right is common ancestor of node_1 or node_2
    right_ancestor = find_common_ancestor(root.right, node_1, node_2)

    # There are 3 conditions where root can be common ancestor:
    # 1. root is node_1 and root.left or root.right is common ancestor of node_2,
    # captured by either right_ancestor[1] being True or left_ancestor[1] being
    # True.
    #
    # 2. root is node_2 and root.left or root.right is common ancestor of node_1,
    # captured by either right_ancestor[0] being True or left_ancestor[0] being
    # True.
    #
    # 3. root.left is common ancestor of node_1 or node_2 and root.right is
    # common ancestor of other.
    #
    # Also note that we return (None, None) while emptying the recursive stack,
    # so although all the parent nodes of root will also be common ancestors,
    # this condition will not be True for them and we will not print them as
    #  common ancestors.
    if (
        (root == node_1 and (right_ancestor[1] or left_ancestor[1]))
        or (root == node_2 and (right_ancestor[0] or left_ancestor[0]))
        or all(
            left or right
            for left, right in zip(
                left_ancestor,
                right_ancestor,
            )
        )
    ):
        print(f"common ancestor is {root.value}")
        return None, None

    # Return wether root is common ancestor of node_1 or node_2
    return (
        root == node_1 or left_ancestor[0] or right_ancestor[0],
        root == node_2 or left_ancestor[1] or right_ancestor[1],
    )


my_tree = tree(height=3)

print(my_tree)

# Testing some cases
print(my_tree.levels[2][0])
print(my_tree.levels[3][0])
find_common_ancestor(my_tree.levels[0][0], my_tree.levels[2][0], my_tree.levels[3][0])

print(my_tree.levels[2][0])
print(my_tree.levels[2][1])
find_common_ancestor(my_tree.levels[0][0], my_tree.levels[2][0], my_tree.levels[2][1])

print(my_tree.levels[3][0])
print(my_tree.levels[2][2])
find_common_ancestor(my_tree.levels[0][0], my_tree.levels[2][0], my_tree.levels[2][1])