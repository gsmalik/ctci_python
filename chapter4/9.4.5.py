from binarytree import tree, bst

def checkBSTTree(node):
    checkBST(node)
    if node.left:
        checkBSTTree(node.left)
    if node.right:
        checkBSTTree(node.right)

def checkBST(node):
    print(node.val)
    leftVal = node.left.val if node.left else -999999
    rightVal = node.right.val if node.right else 999999

    if not (leftVal <= node.val <= rightVal):
        print("Not BST")
        return False
    else:
        return True

my_tree = bst(height=5)

print(my_tree)
checkBSTTree(my_tree.levels[0][0])