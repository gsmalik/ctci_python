import numpy as np


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


def create_linked_list(array, forward=True):
    """
    Function to create linkded list of provided array.

    Parameters
    ----------
    array: ``list``
        Array whose elements will be connected via a linked list.

    forward: ``bool``
        Whether to connect to next or previous. Defaults to True.

    Returns
    -------
    Head pointer of resultant linked list.

    Time Complexity
    ---------------
    O(N)

    Space Complexity
    ----------------
    O(N)
    """

    head = Node(array[0])
    current_node = head
    for value in array[1:]:
        new_node = Node(value)
        attach_node(src_node=current_node, to_attach_node=new_node, forward=forward)
        current_node = new_node
    return head


def attach_node(src_node, to_attach_node, forward=True):
    """
    Function to attach node to another node.

    Parameters
    ----------
    src_node: ``Node``
        Node to attach to.

    to_attach_node: ``Node``
        Node to be attached.

    forward: ``bool``
        Whether to connect to next or previous. Defaults to True.

    Time Complexity
    ---------------
    O(1)

    Space Complexity
    ----------------
    O(1)
    """
    if forward:
        src_node.next = to_attach_node
    else:
        src_node.previous = to_attach_node


def traverse_linked_list(head, forward=True):
    """
    Function to print values of each node of linked list.

    Parameters
    ----------
    head: ``Node``
        Head node of linked list.

    forward: ``bool``
        Whether to connect to next or previous. Defaults to True.

    Time Complexity
    ---------------
    O(N)

    Space Complexity
    ----------------
    O(1)
    """
    if forward:
        while head.next:
            print(head.value, end=" ")
            head = head.next
        print(head.value)
    else:
        while head.previous:
            print(head.value, end=" ")
            head = head.previous
        print(head.value)


def determine_length_linked_list(head, forward=True):
    """
    Function to determine length of linked list.

    Parameters
    ----------
    head: ``Node``
        Head node of linked list.

    forward: ``bool``
        Whether to connect to next or previous. Defaults to True.

    Time Complexity
    ---------------
    O(N)

    Space Complexity
    ----------------
    O(1)
    """
    length = 1
    if forward:
        while head.next:
            length += 1
            head = head.next
    else:
        while head.previous:
            length += 1
            head = head.previous
    return length


def reverse_linked_list(head):
    """
    Function to reverse linked list.

    Parameters
    ----------
    head: ``Node``
        Head node of linked list.

    Returns
    -------
    Head node of type ``Node`` of reversed linked list.

    Time Complexity
    ---------------
    O(N)

    Space Complexity
    ----------------
    O(1)
    """
    
    # create a function to reverse 3 nodes
    def _reverse(previous, current):
        """
        A function to connect current to previous and return "current" node's
        next node.
        Args:
            previous (Node): A node that has already had its "next" reversed.
            current (Node): The node whose "next" needs to be reversed.

        Returns:
            [Node]: The next node of current
        """
        # store the original next of `current`. do this before reversing 
        # `current``
        next = current.next
        
        # reverse the 
        current.next = previous
        
        return current, next
    
    previous = None
    current = head
    while True:
        if previous is None:
            print(f"current is {current.value}")
        else:
            print(f"current is {current.value} and previous is {previous.value}")
        previous, current = _reverse(previous=previous, current=current)
        if current is None:
            break
    
    return previous


def traverse_linked_list_steps(head, steps):
    """
    Function to linked list by specified steps.

    Parameters
    ----------
    head: ``Node``
        Head node of linked list.

    steps: ``int``
        Number of steps to traverse. Must not exceed length of linked list.

    Time Complexity
    ---------------
    O(steps)

    Space Complexity
    ----------------
    O(1)
    """

    for _ in range(steps):
        assert head, "Number of steps greater than length of linked list"
        head = head.next
    return head