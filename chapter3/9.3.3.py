class PlateStacks:
    """
    A class that implements K stacks of certain maximum depth and exposes an API
    that functions as a single stack for the end user.

    Parameters
    ----------
    k: ``int``
       Number of stacks to be implemented.

    depth : ``int``
        Maximum depth of each stack


    Space Complexity
    ----------------
    O(K).
    """

    def __init__(self, k, depth):
        self.k = k
        self.depth = depth

        # Create a list of stacks, akin to towers of plates in a restaurant.
        self.plate_stack = [[] for _ in range(k)]

        # This array of length=k stores wether this stack is already in q. If so,
        # it is not added to the q.
        self.stack_in_q = [True] * k

        # We maintain a queue of which stacks to use. The stack index at the head
        # of the queue is the one used for pushing as well as popping from the
        # unified stack. When popping from another indexed stack, we use
        # ``stack_in_q`` to determine wether to push the index of the popped
        # stack into the queue or not.
        self.q = list(range(k))

        # This array keeps a track of src stack which spilled causing the cuurent
        # stack to be used. This is useful in cases when a ``pop` function is
        # requested and the current stack with the most recent push has become
        # empty, which can happen if your current stack had pushes then pops. For
        # examplle, you could push 2 elements to your current stack and then pop
        # them both. A next pop should be from a different stack, the one which
        # was the active stack before this. This tracks that.
        self.spill_src = [-1] * k

        self.occupied = 0

    def push(self, val):
        """
        Function to push an element to a stack.

        Parameters
        ----------
        val : ``FP32``
            The value of element to be pushed


        Time Complexity
        ---------------
        O(1)
        """
        # Check if space available to push.
        if self.full():
            print(f"Cannot push to stack. Maximum capacity reached")
            return
        self.occupied += 1

        stack_to_use = self.q[0]

        # If current stack is full, pop it from q and use the new head of the q
        if len(self.plate_stack[stack_to_use]) == depth:
            self.spill_src[self.q[1]] = stack_to_use
            self.stack_in_q[stack_to_use] = False
            self.q.pop(0)
            stack_to_use = self.q[0]

        self.plate_stack[stack_to_use].append(val)

        print("**********")
        print(f"Pushed value {val}")
        print(f"Stack:{self.plate_stack}")
        print(f"Queue:{self.q}")
        print(f"Stack in Q:{self.stack_in_q}")

    def pop(self):
        """
        Function to pop most recently pushed value.

        Time Complexity
        ---------------
        O(1)
        """
        if self.occupied == 0:
            print("Cannot pop from stack. Its empty")
        else:
            if len(self.plate_stack[self.q[0]]) == 0:
                return self.pop_index(self.spill_src[self.q[0]])
            else:
                return self.pop_index(self.q[0])

    def pop_index(self, stack_num):
        """
        Function to pop element from top of selected stack.

        Parameters
        ----------
        stack_num: ``int``
            The stack to push the element to

        Time Complexity
        ---------------
        O(1)
        """
        # Check if there is something to pop.
        if len(self.plate_stack[stack_num]) == 0:
            print(f"Pop Failed for stack #{stack_num}. Its empty.")
            return None

        self.occupied -= 1

        # If the stack we are popping from does not exist in q, add it to the end
        # of q
        if not self.stack_in_q[stack_num]:
            self.q.append(stack_num)
            self.stack_in_q[stack_num] = True

        popped_val = self.plate_stack[stack_num].pop()
        print("**********")
        print(f"Popped value {popped_val}")
        print(f"Stack:{self.plate_stack}")
        print(f"Queue:{self.q}")
        print(f"Stack in Q:{self.stack_in_q}")

        return popped_val

    def full(self):
        return self.occupied == self.depth * self.k


k = 3
depth = 2
plate_stack = PlateStacks(k, depth)
plate_stack.push(1)
plate_stack.push(2)
plate_stack.push(3)
plate_stack.pop()
plate_stack.push(4)
plate_stack.pop_index(0)
plate_stack.pop()
plate_stack.pop()
plate_stack.pop()
plate_stack.push(1)
plate_stack.push(2)
plate_stack.push(3)
plate_stack.push(4)
plate_stack.push(5)
plate_stack.push(6)
plate_stack.pop()
plate_stack.pop_index(2)
plate_stack.pop()
plate_stack.pop()