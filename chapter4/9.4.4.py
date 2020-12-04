from binarytree import tree

def checkHeight(node):
    leftHeight = checkHeight(node.left) if node.left else 0
    rightHeight = checkHeight(node.right) if node.right else 0
    if leftHeight is False or rightHeight is False or abs(leftHeight-rightHeight)>1:
        return False
    else:
        return max(leftHeight, rightHeight)+1

my_tree = tree(height=3)

print(my_tree)
print(checkHeight(my_tree.levels[0][0]))
