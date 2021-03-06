import random, graphs

def find_next_visit(node):
    print(f"Next node after {node.value}: ", end='')
    # Check if right child exists
    if node.right:
        graphs.in_order(node.right)
        return
    
    while node.parent:
        if node.parent.value > node.value:
            break
        node = node.parent
    # Check if I have reached root of tree
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
