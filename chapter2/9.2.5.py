import numpy as np

import linked_list as ll


def create_number_from_linked_list(head):
    """
    Function to create a number out of given linked list.

    Parameters
    ----------
    head: ``Node``
        Head node of linked list.


    Returns
    -------
    Number of type ``int``.

    Time Complexity
    ---------------
    O(N)
    Space Complexity
    ----------------
    O(1). Number can be represented using constant space in FP64.
    """
    dec_position = 1
    number = 0
    while head:
        number = number + dec_position * head.value
        head = head.next
        dec_position *= 10
    return number


def create_linked_list_from_number(number):
    """
    Function to create a linked list out of given number.

    Parameters
    ----------
    number: ``int``
        Number of which linked list will be created.


    Returns
    -------
    Head of type ``node`` of resultant linked list.

    Time Complexity
    ---------------
    O(D), where D is the number of digits in the number.
    Space Complexity
    ----------------
    O(D)
    """
    head = None

    while number != 0:
        if not head:
            head = ll.Node(number % 10)
            pointer = head
        else:
            pointer.next = ll.Node(number % 10)
            pointer = pointer.next
        number = number // 10
    return head


# Generate 2 random linked lists
test_1 = np.random.randint(0, 10, 5)
test_2 = np.random.randint(0, 10, 7)

head_1 = ll.create_linked_list(test_1)
head_2 = ll.create_linked_list(test_2)

# Create numbers out of linked lists
number_1 = create_number_from_linked_list(head_1)
print(number_1)
number_2 = create_number_from_linked_list(head_2)
print(number_2)

# Create linked list out of summed numbers.
new_head = create_linked_list_from_number(number_1 + number_2)
ll.traverse_linked_list(new_head)
