class myStack:
    def __init__(self):
        self.userStack = []
        self.pile = []

    def push(self, element):
        self.userStack.append(element)

    def pop(self):
        while self.userStack:
            element = self.userStack.pop()
            self.pile.append(element)
            # print(element)
        self.pile.pop()

        while self.pile:
            self.userStack.append(self.pile.pop())
        return element

test = myStack()
test.push(2)
test.push(3)
test.push(4)
test.push(5)
print(test.pop())
test.push(6)
print(test.pop())
print(test.pop())
print(test.pop())
print(test.pop())
test.push(6)
print(test.pop())
