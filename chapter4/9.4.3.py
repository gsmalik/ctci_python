from binarytree import tree

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

array = []

def add_node(node, depth):
    if depth == len(array):
        array.append(Node(node.value))
        return
    head = array[depth]
    while head.next:
        head=head.next
    head.next = Node(node.value)


def create_linked_lists(node, depth):
    add_node(node, depth)
    if node.left:
        create_linked_lists(node.left, depth+1)
    if node.right:
        create_linked_lists(node.right, depth+1)

def print_linked_list_depth():
    for head_node in array:
        while head_node:
            print(head_node.value, end=' ')
            head_node = head_node.next
        print('')

my_tree = tree(height=3)
print(my_tree)
create_linked_lists(my_tree.levels[0][0],0)
print_linked_list_depth()