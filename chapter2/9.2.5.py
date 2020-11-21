import numpy as np

# np.random.seed(0)

import linkledList as ll

test1 = np.random.randint(0,10,5)
test2 = np.random.randint(0,10,7)

myLinkedList1 = ll.linkedList()
myLinkedList1.createLinkedList(test1)
myLinkedList1.traverseLinkedList()
number1 = myLinkedList1.createNumberFromList()

myLinkedList2 = ll.linkedList()
myLinkedList2.createLinkedList(test2)
myLinkedList2.traverseLinkedList()
number2 = myLinkedList2.createNumberFromList()

sum_number = number1 + number2
print(sum_number)

multiplier = 10

myList = []
multiplier = 10
while sum_number != 0:
    myList.append(sum_number % multiplier)
    sum_number = int(sum_number/multiplier)

newLinkedList = ll.linkedList()
newLinkedList.createLinkedList(np.array(myList))
newLinkedList.traverseLinkedList()