class SortedStack:
    """
    A class that implements a stack that stores elements in min-sorted order, given an
    additional temporary stack.

    Space Complexity
    ----------------
    O(1). We do not use any additional space apart from the given stack.
    """

    def __init__(self):
        # This is the stack we use that stores elements in sorted order with min
        # at top.
        self.stack = []
        # We use the ``sort_stack`` as a placeholder for inserting a to-be-pushed
        # in the correct order. We do this by draining ``stack`` element by
        # element and comparing againsy the to-be-pushed value. When the
        # to-be-pushed value is less than the element being drained, we first
        # push the to-be-pushed element to ``sort_stack`` and then the element
        # being drained. We drain the whole ``stack`` onto ``sort_stack`` and
        # then drain it back.
        self.sort_stack = []

    def push(self, element):
        """
        Function to push value and maintain sorted order of stack.

        Time Complexity
        ---------------
        O(N), where N is the current depth of the stack.
        """

        # ``sort_stack``` should be empty before every push
        assert not self.sort_stack

        print(f"Pushing {element}")
        # If ``stack`` is empty, we can directly push
        if not self.stack:
            self.stack.append(element)
            return

        # Start draining ``stack``
        element_to_be_pushed = True
        while self.stack:
            if element <= self.stack[-1] and element_to_be_pushed:
                self.sort_stack.append(element)
                element_to_be_pushed = False
            self.sort_stack.append(self.stack.pop())
        
        # ``element``` is greatest. Push now
        if element > self.sort_stack[-1]:
            self.sort_stack.append(element)

        # Drain back
        while self.sort_stack:
            self.stack.append(self.sort_stack.pop())

    def pop(self):
        """
        Function to pop value at top of stack.

        Time Complexity
        ---------------
        O(1).
        """

        if not self.stack:
            print("Nothing to pop. Stack empty")
            return
        val_return = self.stack.pop()
        print(f"Popped {val_return}")
        return val_return

test = SortedStack()
test.push(3)
test.push(5)
test.push(0)
test.push(10)
test.push(-10)
test.pop()
test.push(-2)
test.pop()
test.pop()
test.pop()
test.pop()
test.pop()
test.pop()