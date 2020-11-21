import numpy as np
import linkledList as ll
# np.random.seed(0)


test = np.random.randint(0,10,15)
myLinkedList = ll.linkedList()
myLinkedList.createLinkedList(test)
myLinkedList.traverseLinkedList()
myLinkedList.removeDuplicates()
myLinkedList.traverseLinkedList()

