class myStack:
    def __init__(self, limit):
        self.userStack = [[]]
        self.limit = limit
        self.index = 0

    def push(self, element):
        print(self.userStack[self.index] == [], len(self.userStack[self.index]))
        if not self.userStack[self.index]:
            if len(self.userStack[self.index]) < self.limit:
                self.userStack[self.index].append(element)
            else:
                self.index += 1
                self.push(element)

        else:
            self.userStack[self.index].append(element)

    def pop(self):
        if not self.userStack[self.index] == []:  # not empty
            return self.userStack[self.index].pop()
        else:  # empty
            self.index = -1
            self.userStack.pop()


test = myStack(1)
test.push(2)
test.push(3)
test.push(4)
test.push(5)
print(test.pop())
print(test.pop())
print(test.pop())
print(test.pop())
test.push(6)
print(test.pop())
