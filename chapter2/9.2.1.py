import numpy as np
import linkledList as ll


test = np.random.randint(0, 5, 10)
print(test)
head = ll.create_linked_list(test)
ll.traverse_linked_list(head)
ll.remove_duplicates(head)
ll.traverse_linked_list(head)
