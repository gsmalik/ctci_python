import numpy as np

import linked_list as ll


def delete_middle_node(node):
    """
    Function to delete node from linked list.

    Parameters
    ----------
    node: ``Node``
        Node to be deleted. Cannot be last node of linked list.

    Time Complexity
    ---------------
    O(N), where N is the number of nodes after given node in the linked list.

    Space Complexity
    ----------------
    O(1)
    """

    assert node.next, "Cannot be last node of a linked list"

    # Copy next node's value to current node until you reach 2nd to last node.
    while node.next.next:
        node.value = node.next.value
        node = node.next

    # Copy next node's value to current second to last node and cut off the link.
    node.value = node.next.value
    node.next = None


def return_k_to_last(head, k):
    """
    Function to return k from last node of linked list.

    Parameters
    ----------
    head: ``Node``
        Head node of linked list.

    k: ``int``
        Index of node relative to last node. Starts from 1.

    Time Complexity
    ---------------
    O(N)

    Space Complexity
    ----------------
    O(1)
    """
    # Determine length of linked list
    length_linked_list = ll.determine_length_linked_list(head)

    # Traverse ``length_linked_list`` - ``K`` nodes
    for _ in range(length_linked_list - k):
        head = head.next

    return head


test = np.random.randint(0, 10, 10)
print(test)
head = ll.create_linked_list(test)
ll.traverse_linked_list(head)
delete_middle_node(return_k_to_last(head, 4))
ll.traverse_linked_list(head)