class myStack():
    def __init__(self, string):
        self.string = []
        for character in string:
            self.string.append(character)

    def empty(self):
        return len(self.string) == 0

    def getTopChar(self):
        return self.string.pop(0)

class myString():
    def __init__(self):
        self.string = []

    def appendSpecial(self):
        self.string.append('%')
        self.string.append('2')
        self.string.append('0')

    def appendChar(self, character):
        self.string.append(character)

def URLify(string):
    myStringStack = myStack(string)
    myNewString = myString()
    while not myStringStack.empty():
        character = myStringStack.getTopChar()
        print(character)
        if character == " ":
            myNewString.appendSpecial()
        else:
            myNewString.appendChar(character)

    print(myNewString.string)

URLify("hello ")
    
