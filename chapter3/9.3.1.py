import numpy as np

class KStacks():
    def __init__(self, k, n):
        self.k = k
        self.n = n
        # array to use
        self.arr = [0 for x in range(n)]

        # index of most recently pushed element at each stack
        self.top_indices = [-1 for x in range(k)]

        # Maybe you do not need the -1
        self.info = [x+1 for x in range(n)]
        # next index to use to push an item. this also gets updated when
        # a stack is popped and that index then becomes free
        self.free = 0

        self.occupied = 0
    
    def push(self, stack_num, val):
        if self.full():
            print(f"Cannot push to stack #{stack_num}. Array is full.")
            return
        self.occupied += 1
        index_push = self.free
        self.free = self.info[self.free]
        self.arr[index_push] = val
        self.info[index_push] = self.top_indices[stack_num]
        self.top_indices[stack_num] = index_push

    def pop(self, stack_num):
        if self.top_indices[stack_num] == -1:
            print(f"Pop Failed for stack #{stack_num}. Its empty.")
            return None
        self.occupied -= 1
        previous_index = self.info[self.top_indices[stack_num]]
        val_return = self.arr[self.top_indices[stack_num]]

        self.info[self.top_indices[stack_num]] = self.free
        self.free = self.top_indices[stack_num]
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