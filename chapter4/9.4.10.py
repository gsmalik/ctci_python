from binarytree import tree


def check_subtree(node_1, node_2):
    if not node_1:
        return False
    if node_1.value == node_2.value:
        if compare_traversal(node_1, node_2):
            return True
    if check_subtree(node_1.left, node_2):
        return True
    if check_subtree(node_1.right, node_2):
        return True
    return False


def compare_traversal(node_1, node_2):
    if (not node_1) and (not node_2):
        return True
    if (node_1 and not node_2) or (not node_1 and node_2):
        return False
    if node_1.value != node_2.value:
        return False
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
