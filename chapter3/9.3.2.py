class myStack():
    def __init__(self):
        self.userStack = []
        self.minStack = []
    
    def push(self, element):
        if not self.minStack:
            self.minStack.append(element)
        else:
            if element <= self.minStack[-1]:
                self.minStack.append(element)

        self.userStack.append(element)

    def pop(self):
        if self.minStack and self.userStack:
            poppedElement = self.userStack.pop()
            if poppedElement == self.minStack[-1]:
                self.minStack.pop()
    
    def min(self):
        return self.minStack[-1]


test = myStack()
test.push(2)
test.push(-100)
test.pop()
print(test.min())