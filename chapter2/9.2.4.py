import numpy as np

np.random.seed(0)

import linkledList as ll

test = np.random.randint(0,10,10)
myLinkedList = ll.linkedList()
myLinkedList.createLinkedList(test)
myLinkedList.traverseLinkedList()
myLinkedList.partitionList(4)