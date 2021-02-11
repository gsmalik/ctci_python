import numpy as np

import linked_list as ll


def return_k_to_last(head, k):
    """
    Function to k from last node of linked list.

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
print(return_k_to_last(head, 4).value)