import graphs

# Create test array
test = [1, 2, 3, 4, 5, 6, 7, 8]

#  Create BST
root = graphs.create_bst(test, None)
print(f"{root.value} {root.left.value} {root.right.value}")

# Test a corner case of array having a single element only
test = [1]
root = graphs.create_bst(array=test, parent_node=None)
print(f"{root.value} {root.left} {root.right}")
