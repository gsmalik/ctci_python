import numpy as np

import linked_list as ll


def partition_linked_list(head, x):
    """
    Function to partition a linked list around a given value.

    Parameters
    ----------
    head: ``Node``
        Head node of linked list.

    x: ``int``
        Integer value around which linked list needs to be partitioned.

    Returns
    -------
    Head node of type ``Node`` of partitioned linked list.

    Time Complexity
    ---------------
    O(N)
    Space Complexity
    ----------------
    O(N)
    """

    # Create null head nodes for paritioned linked lists.
    smaller_x_head = None
    remaining_head = None

    # Traverse original linked list
    while head:
        print(head.value)
        # If current node's value is smallers than x, then create a node with
        # this value and attach it to the smaller_x linked list.
        if head.value < x:
            if smaller_x_head:
                smaller_x_pointer.next = ll.Node(head.value)
                smaller_x_pointer = smaller_x_pointer.next

            else:
                smaller_x_head = ll.Node(head.value)
                smaller_x_pointer = smaller_x_head
        # Otherwise, attach it to the remaining linked list
        else:
            if remaining_head:
                remaining_x_pointer.next = ll.Node(head.value)
                remaining_x_pointer = remaining_x_pointer.next
            else:
                remaining_head = ll.Node(head.value)
                remaining_x_pointer = remaining_head
        head = head.next

    # Connect the 2 linked lists together
    smaller_x_pointer.next = remaining_head
    return smaller_x_head


test = np.random.randint(0, 10, 10)
print(test)
head = ll.create_linked_list(test)
ll.traverse_linked_list(head)
head_partitioned = partition_linked_list(head, test[5])
ll.traverse_linked_list(head_partitioned)