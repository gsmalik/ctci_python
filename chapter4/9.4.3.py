from binarytree import tree


class Node:
    """
    A class that implements a node that can have next/previous connections.

    Parameters
    ----------
    value: ``FP32``
       The value of the node

    Space Complexity
    ----------------
    O(1).
    """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


# Create an empty list where we will store the linked lists. For example, it
# can look like [linked_list0, linked_list1, ...] for a number of linked lists.
array = []


def add_node(node, depth):
    """
    Function to add a node to a linked list at `depth` index of `array`.

    Parameters
    ----------
    node: ``Node``
        The node that needs to be appended to the linked list.

    depth: ``int``
        The index of the linked list to which we need to append this node.

    Time Complexity
    ---------------
    O(N), where N is the number of nodes in linked list at that index.

    Space Complexity
    O(1). We do not use any additional space to add this node. Note that we are not
    including the space of the current linked list or the array since that forms part
    of the input relative to this function.
    """
    if depth == len(array):
        array.append(Node(node.value))
        return
    head = array[depth]
    while head.next:
        head = head.next
    head.next = Node(node.value)


def create_linked_lists(node, depth):
    """
    Function to create a list of linked lists, where each index captures all nodes at
    that depth in the tree.

    Parameters
    ----------
    node: ``Node``
        The root node of the tree.

    depth: ``int``
        The index of the list where the linked list will be created.

    Time Complexity
    ---------------
    O(N), where N is the number of nodes in the tree.

    Space Complexity
    O(log(N)), where N is the number of nodes in the tree, assuming a balances tree.
    Otherwise you can frame this as O(D), where D is the maximum depth of the tree
    """
    # Add parent node to array
    add_node(node, depth)
    # Recursively add all nodes to the left of this parent node
    if node.left:
        create_linked_lists(node.left, depth + 1)
    # Recursively add all nodes to the right of this parent node
    if node.right:
        create_linked_lists(node.right, depth + 1)


def print_linked_list_depth():
    """Prints linked list iteratively"""
    for head_node in array:
        while head_node:
            print(head_node.value, end=" ")
            head_node = head_node.next
        print("")


my_tree = tree(height=3)
print(my_tree)
create_linked_lists(my_tree.levels[0][0], 0)
print_linked_list_depth()