import numpy as np

class KStacks():
    """
    A class that implements K stacks in a single array.

    Parameters
    ----------
    k: ``int``
       Number of stacks to be implemented.

    n : ``int``
        Length of array used to implement these stacks


    Time Complexity
    ---------------
    Pushing an element to a stack: O(1)
    Popping an element from a stack: O(1)

    Space Complexity
    ----------------
    O(N+K).
    """
    def __init__(self, k, n):
        self.k = k
        self.n = n

        # Define array to store elements of the stacks.
        self.arr = [0 for x in range(n)]

        # This array of length=k stores the corresponding index position in arr
        # for the top element of each stack. Note that this is not the top value
        # of the stack but rather the index of where the top value is in ``arr``.
        self.top_indices = [-1 for x in range(k)]

        # This info object serves two purposes. Note that this is also of length
        # n, same as length of our storage array. Hence, this is basically an
        # extension of the storage array and stores valuable information. For
        # an index in ``arr`` that is currently free and not used by a stack, it
        # stores the next free index in ``arr`` if this index was used up. For
        # example, if index #3 in ``arr`` is free, then index #3 in ``info`  
        # stores which is the next index that is free to be used by the next push
        # For an index that is used up, it stores the index where an element was
        # pushed before it. Basically the index of the previous push. 
        self.info = [x+1 for x in range(n)]

        # This is the immediate index that would be used up by a push. This gets
        # updated after each push/pop by probing ``info``.
        self.free = 0

        # Just a simple tracker to determine if there is space left in the array
        # for elements to be pushed.
        self.occupied = 0
    
    def push(self, stack_num, val):
        """
        Function to push an element to a stack.

        Parameters
        ----------
        stack_num: ``int``
            The stack to push the element to

        val : ``FP32``
            The value of element to be pushed


        Time Complexity
        ---------------
        O(1)

        Space Complexity
        ----------------
        O(N+K).
        """
        # Check if space available to push.
        if self.full():
            print(f"Cannot push to stack #{stack_num}. Array is full.")
            return
        
        self.occupied += 1
        
        # Determine free slot to push to.
        index_push = self.free

        # Update free slot
        self.free = self.info[self.free]

        # Write value to ``arr``
        self.arr[index_push] = val

        # Update ``info`` with index of previous push
        self.info[index_push] = self.top_indices[stack_num]

        # Update index to top most element (now this one)
        self.top_indices[stack_num] = index_push

    def pop(self, stack_num):
        # Check if there is something to pop.
        if self.top_indices[stack_num] == -1:
            print(f"Pop Failed for stack #{stack_num}. Its empty.")
            return None
        
        self.occupied -= 1
        
        # Determine the index of the latest push and get value from ``arr`` at
        # that index.
        previous_index = self.info[self.top_indices[stack_num]]
        val_return = self.arr[self.top_indices[stack_num]]

        # You will use the freed up index from this pop as the index for next
        # push and will store the current ``free`` as the next->next push.
        self.info[self.top_indices[stack_num]] = self.free
        self.free = self.top_indices[stack_num]

        # Update the top index of the stack
        self.top_indices[stack_num] = previous_index
        
        print("popped", val_return)
        return val_return
    
    def full(self):
        return self.occupied == self.n

    def empty(self):
        return self.occupied == 0

k=3
n=9
k_stack = KStacks(k, n)
# test array becomes full
for index in range(n+1):
    k_stack.push(index%k, index)

for index in range(n+1):
    k_stack.pop(index%k)

# Some random interweaving of push/pop between different stacks
k_stack.push(0,1)
k_stack.push(1,4)
k_stack.push(0,2)
k_stack.push(0,3)
k_stack.push(2,7)
k_stack.pop(0)
k_stack.pop(0)
k_stack.pop(0)
k_stack.pop(1)
k_stack.pop(2)
k_stack.push(2,9)
k_stack.push(1,11)
k_stack.pop(2)
k_stack.pop(1)