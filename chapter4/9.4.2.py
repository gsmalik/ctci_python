import graphs

def create_bst(array):
    middle = len(array)//2
    root = graphs.BinaryNode(array[middle])
    if middle < len(array) - 1:
        root.right = create_bst(array[middle+1:])
    if middle > 0:
        root.left = create_bst(array[:middle])

    return root

test = [1,2,3,4,5,6,7,8]
root = create_bst(test)
print(f"{root.value} {root.left.value} {root.right.value}")
test = [1]
root = create_bst(test)
print(f"{root.value} {root.left} {root.right}")
