import linked_list as ll
import numpy as np

def determine_cyclic(head):
    """
    Function to determine if a linked list is cyclic.

    Parameters
    ----------
    head: ``Node``
        Head node of linked list.

    Returns
    -------
    Value of cyclic node if intersecting. False otherwise.

    Time Complexity
    ---------------
    O(N)
    Space Complexity
    ----------------
    O(1)
    """

    # Infer 2 pointers. Slow pointer hops by 1 while fast pointer hops by 2 in
    # same time
    slow_pointer = head
    fast_pointer = head

    # Wait for fast pointer and slow pointer to intersect. The relative velocity
    # between the pointers is 1. Hence, if we had to divide a cyclic linked list
    # into A acyclic nodes and C nodes in cycle, that means that when slow
    # pointer enters the cycle, it would have taken A steps and hence fast
    # pointer would be A steps ahead. At this stage, it would take fast pointer
    # C-A steps to catch up the slow pointer from behind. This means that slow
    # pointer would be C-A nodes into the cycle (relative to entry node of cycle).
    # Fast pointer has caught up to slow pointer and it will also be at the same
    # node ie C-A nodes away from the starting cycle node.
    init_flag = True
    while (fast_pointer != slow_pointer or init_flag):
        init_flag = False
        # If fast pointer is about to become None, that means linked list is acyclic
        if (fast_pointer.next is None) or (fast_pointer.next.next is None):
            return False
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next

    # Definitely a cycle exists. Since both fast pointer and slow pointer are C-A
    # steps into the cycle, that means that if we reduced fast pointer speed from
    # 2 to 1, it would take A steps to complete the cycle and reach the origin 
    # cyclic node. Hence, we can reset slow pointer to head. This means that
    # slow pointer would take A steps to enter the cycle and it would take fast
    # pointer A steps to again reach the cycle node, which is what we should return.
    slow_pointer = head
    while slow_pointer!=fast_pointer:
        slow_pointer = slow_pointer.next
        # Notice that fast pointer is not hopping by 2. But 1.
        fast_pointer = fast_pointer.next
    
    return fast_pointer.value

def make_cyclic(head, index):
    current_pointer = head
    for _ in range(index):
        current_pointer = current_pointer.next
    looped_node = current_pointer
    current_pointer = head
    while current_pointer.next:
        current_pointer = current_pointer.next
    current_pointer.next =looped_node
    print("cyclic at", current_pointer.next.value)
    return head 

test = np.array([x for x in range(10)])
print(test)
head = ll.create_linked_list(test)
# Randomly decide whether to make linked list cyclic for testing purpose.
if bool(np.random.randint(0,2,1)):
    head = make_cyclic(head, np.random.randint(0,10,1)[0])
print(determine_cyclic(head))