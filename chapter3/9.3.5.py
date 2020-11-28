class myStack:
    def __init__(self):
        self.userStack = []
        self.pile = []

    def push(self, element):
        self.userStack.append(element)
        self.sortStack()
        print(self.userStack)

    def pop(self):
        return self.userStack.pop()

    def sendMinToBottom(self, depth):
        minElement = 123456789
        for _ in range(depth):
            element = self.userStack.pop()
            if element < minElement:
                minElement = element
            self.pile.append(element)
        
        self.userStack.append(minElement)
        for _ in range(depth):
            element = self.pile.pop()
            if element != minElement:
                self.userStack.append(element)

    def sortStack(self):
        depthStack = len(self.userStack)
        for index in range(depthStack):
            self.sendMinToBottom(depthStack - index)

test = myStack()
test.push(3)
test.push(5)
test.push(0)
test.push(10)
test.push(-10)
test.pop()
test.push(-2)