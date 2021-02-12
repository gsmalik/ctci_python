import numpy as np

np.random.seed(0)

import linked_list as ll


def check_equal(head_1, head_2):
    """
    Function to check if two linked list have nodes with euqal vales.

    Parameters
    ----------
    head_1: ``Node``
        Head node of first linked list.

    head_2: ``Node``
        Head node of second linked list.

    Returns
    -------
    True if nodes are equal. False otherwise

    Time Complexity
    ---------------
    O(N)

    Space Complexity
    ----------------
    O(1)
    """
    while head_1 and head_2:
        if head_1.value != head_2.value:
            return False
        head_1 = head_1.next
        head_2 = head_2.next
    return True if (head_1 is None and head_2 is None) else False


# Test case for palindrome
test = np.array([3, 1, 3, 1, 3])
print(test)
# Reverse your linked list
reversed_head = ll.reverse_linked_list(ll.create_linked_list(test))
head = ll.create_linked_list(test)
# For palindrom, a linked list should be equal to its reversed version
print(check_equal(head, reversed_head))

# Test case for not palindrome
test = np.array([3, 3, 1, 3])
print(test)
reversed_head = ll.reverse_linked_list(ll.create_linked_list(test))
head = ll.create_linked_list(test)
print(check_equal(head, reversed_head))