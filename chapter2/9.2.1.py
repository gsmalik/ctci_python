import numpy as np
import linked_list as ll

def remove_duplicates(head):
    """
    Function to remove nodes with duplicate values in a linked list.
    Parameters
    ----------
    head: ``Node``
        Head node of linked list.
    Time Complexity
    ---------------
    O(N)
    Space Complexity
    ----------------
    O(N)
    """
    # Create a set to store seen values
    seen = set([])
    # Flag to store whether end of linked list is reached
    end_reached = False

    # Keep removing duplicates until end of linked list reached
    while head.next:
        # Add value of current node to set.
        seen.add(head.value)

        # Keep removing next node until we encounter a node value not seen in set
        while head.next.value in seen:
            # Reattach head.next to head.next.next if head.next.next exists
            if head.next.next:
                ll.attach_node(head, head.next.next)
            # This means head.next is end of linked list
            else:
                head.next = None
                end_reached = True
                break
        # Only move if head.next is not last node in linked list
        if not end_reached:
            head = head.next


test = np.random.randint(0, 5, 10)
print(test)
head = ll.create_linked_list(test)
ll.traverse_linked_list(head)
remove_duplicates(head)
ll.traverse_linked_list(head)
