from binarytree import tree

def find_common_ancestor(root, node_1, node_2):
    if root is None:
        return (False, False)

    left_children = find_common_ancestor(root.left, node_1, node_2)
    right_children = find_common_ancestor(root.right, node_1, node_2)

    if (
        (root == node_1 and (right_children[1] or left_children[1]))
        or (root == node_2 and (right_children[0] or left_children[0]))
        or all(
            left or right
            for left, right in zip(
                left_children,
                right_children,
            )
        )
    ):
        print(f"common ancestor is {root.value}")
        return None, None

    return (
        root == node_1 or left_children[0] or right_children[0],
        root == node_2 or left_children[1] or right_children[1],
    )

my_tree = tree(height=3)

print(my_tree)

print(my_tree.levels[2][0])
print(my_tree.levels[3][0])
find_common_ancestor(my_tree.levels[0][0], my_tree.levels[2][0], my_tree.levels[3][0])

print(my_tree.levels[2][0])
print(my_tree.levels[2][1])
find_common_ancestor(my_tree.levels[0][0], my_tree.levels[2][0], my_tree.levels[2][1])

print(my_tree.levels[3][0])
print(my_tree.levels[2][2])
find_common_ancestor(my_tree.levels[0][0], my_tree.levels[2][0], my_tree.levels[2][1])