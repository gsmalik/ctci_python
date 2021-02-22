class min_stack():
    """
    A class that a stack with support for probing minimum val in O(1) time.

    Space Complexity
    ----------------
    O(N). We use another stack for keeping track of minimum elements.
    """
    def __init__(self):
        # Implement main stack to push/pop values from
        self.user_stack = []
        # Implement a stack to track min values. Items only pushed when a new min
        # element is pushed to ``user_stack```. Items only popped when a min
        # element is popped from ``user_stack``.
        self.min_stack = []
    
    def push(self, val):
        """
        Function to push an element to the stack.

        Parameters
        ----------
        val : ``FP32``
            The value of element to be pushed

        Time Complexity
        ---------------
        O(1)
        """
        # If stack is empty, first element pushed is also min element.
        if not self.min_stack:
            self.min_stack.append(val)
        # If new min element pushed, add that to the min_stack
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
        # Push to main stack regardless
        self.user_stack.append(val)

    def pop(self):
        """
        Function to pop element from top of stack.

        Time Complexity
        ---------------
        O(1)
        """
        # Check if item available to pop
        if self.min_stack and self.user_stack:
            # Pop the element
            popped_element = self.user_stack.pop()
            # If min value, pop it from min_stack as well.
            if popped_element == self.min_stack[-1]:
                self.min_stack.pop()
        else:
            print("Stack empty. Nothing to pop")
    
    def min(self):
        """
        Function to return minimum valued element in stack.

        Returns
        -------
        Value of minimum element.

        Time Complexity
        ---------------
        O(1)
        """
        if self.min_stack:
            return self.min_stack[-1]
        else:
            print("Stack empty. No minimum element")


test = min_stack()
test.push(2)
test.push(-100)
test.pop()
print(test.min())