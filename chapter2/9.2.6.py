import numpy as np

np.random.seed(0)

import linkledList as ll

test = np.array([0, 3, 1, 3, 1, 3, 0])
myLinkedList = ll.linkedList()
myLinkedList.createLinkedList(test)
myLinkedList.traverseLinkedList()
myLinkedList.reverseLinkedList()
myLinkedList.reversedList.traverseLinkedList()
myLinkedList.checkPalindrome()
print(myLinkedList.palindrome)