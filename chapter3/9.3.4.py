class myQueue:
    """
    A class that implements a queue using 2 stacks

    Space Complexity
    ----------------
    O(1). We do not use ant additional space apart from the given stacks.
    """
    def __init__(self):
        # We use stack_1 for all pushes
        self.stack_1 = []
        # We use stack_2 for all pops. If stack_2 is empty, we drain stack_1 into
        # stack_2, thus reversing order and pop the top most element. If stack_2
        # already has element, we do not drain as the top of the element in 
        # stack_2 will always be the oldest.
        self.stack_2 = []
    
    def pop(self):
        """
        Function to pop most recently pushed value.

        Time Complexity
        ---------------
        O(N), where N is the depth of the queue.
        """
        # If stack 2 is not empty, the element at top is the oldest and hence
        # should be returned
        if self.stack_2:
            val_return = self.stack_2.pop(-1)
            print(f"Popped {val_return}")
            return val_return
        # If stack 2 is empty and stack 1 has elements, then we need to reverse
        # order by draining stack 1 into stack 2 and then popping the top most
        # element.
        elif self.stack_1:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop(-1))
            val_return = self.stack_2.pop(-1)
            print(f"Popped {val_return}")
            return val_return
        # Both empty. Nothing to pop
        else:
            print("Queue empty. Nothing to pop")
    
    def push(self, val):
        """
        Function to push value to queue.

        Time Complexity
        ---------------
        O(1).
        """
        self.stack_1.append(val)

test = myQueue()
test.push(2)
test.push(3)
test.push(4)
test.push(5)
test.pop()
test.push(6)
test.pop()
test.pop()
test.pop()
test.pop()
test.pop()
test.push(6)
test.pop()
