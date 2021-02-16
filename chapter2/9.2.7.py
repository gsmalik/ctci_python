import linked_list as ll
import numpy as np


def determine_intersection(head_1, head_2):
    """
    Function to determine if 2 linked lists intersect.

    Parameters
    ----------
    head_1: ``Node``
        Head node of first linked list.

    head_2: ``Node``
        Head node of second linked list.

    Returns
    -------
    True if intersecting. False otherwise.

    Time Complexity
    ---------------
    O(N)
    Space Complexity
    ----------------
    O(1)
    """

    def _traverse_longer_ll(head_1, head_2):
        """
        Function to traverse the longer of the 2 linked lists such that the
        longer linked list has equal number of steps to go before termination as
        the length of the shorter linked list.
        """
        (length_1, length_2) = (
            ll.determine_length_linked_list(head_1),
            ll.determine_length_linked_list(head_2),
        )
        head_1 = ll.traverse_linked_list_steps(head_1, max(0, length_1 - length_2))
        head_2 = ll.traverse_linked_list_steps(head_2, max(0, length_2 - length_1))
        return (head_1, head_2)

    # Determine length of the 2 linked list.
    (length_1, length_2) = (
        ll.determine_length_linked_list(head_1),
        ll.determine_length_linked_list(head_2),
    )

    # Traverse longer linked list by required steps.
    (head_1, head_2) = _traverse_longer_ll(head_1, head_2)

    # Traverse the 2 linked lists and check for equal node values.
    for _ in range(min(length_1, length_2)):
        assert head_1, head_2
        if head_1.value == head_2.value:
            return True
        head_1 = head_1.next
        head_2 = head_2.next

    # If end reached and no common value encounter, this means no intersection.
    return False


# Create 2 random arrays of unequal length.
test_1 = np.random.randint(0, 10, 10)
test_2 = np.random.randint(0, 10, 8)

# Determine randomly if lists will match or not.
intersect = bool(np.random.randint(0, 2, 1))
# Both lists will be singly linked, it follows that every node after the common
# node (if present) must be the same in both linked lists. Code below implements
# this logic.
if intersect:
    intersection_pont = np.random.randint(0, 8)
    test_1[: 2 + intersection_pont] = np.random.randint(-10, 0, 2 + intersection_pont)
    test_1[2 + intersection_pont :] = test_2[intersection_pont:]
# If lists do not intersect, then node values must not match at all.
else:
    test_1 = np.random.randint(-10, 0, 10)

# Create linked list
print(test_1)
head_1 = ll.create_linked_list(test_1)

# Create linked list
print(test_2)
head_2 = ll.create_linked_list(test_2)

# Determine if intersecting
print("Lists intersect:", determine_intersection(head_1, head_2))