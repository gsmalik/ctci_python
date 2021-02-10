import numpy as np


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


def create_linked_list(array, forward=True):
    """
    Function to create linkded list of provided array.

    Parameters
    ----------
    array: ``list``
        Array whose elements will be connected via a linked list.

    forward: ``bool``
        Wether to connect to next or previous. Defaults to True.

    Returns
    -------
    Head pointer of resultant linked list.

    Time Complexity
    ---------------
    O(N)

    Space Complexity
    ----------------
    O(N)
    """

    head = Node(array[0])
    current_node = head
    for value in array[1:]:
        new_node = Node(value)
        attach_node(src_node=current_node, to_attach_node=new_node, forward=forward)
        current_node = new_node
    return head


def attach_node(src_node, to_attach_node, forward=True):
    """
    Function to attach node to another node.

    Parameters
    ----------
    src_node: ``Node``
        Node to attach to.

    to_attach_node: ``Node``
        Node to be attached.

    forward: ``bool``
        Wether to connect to next or previous. Defaults to True.

    Time Complexity
    ---------------
    O(1)

    Space Complexity
    ----------------
    O(1)
    """
    if forward:
        src_node.next = to_attach_node
    else:
        src_node.previous = to_attach_node


# aaaaa write this, creation and deletion in cheat sheet
def traverse_linked_list(head, forward=True):
    """
    Function to print values of each node of linked list.

    Parameters
    ----------
    head: ``Node``
        Head node of linked list.

    forward: ``bool``
        Wether to connect to next or previous. Defaults to True.

    Time Complexity
    ---------------
    O(N)

    Space Complexity
    ----------------
    O(1)
    """
    if forward:
        while head.next:
            print(head.value, end=" ")
            head = head.next
        print(head.value)
    else:
        while head.previous:
            print(head.value, end=" ")
            head = head.previous
        print(head.value)


def remove_duplicates(head):
    """
    Function to remove nodes with duplicate values in a linked list.

    Parameters
    ----------
    head: ``Node``
        Head node of linked list.

    Time Complexity
    ---------------
    O(N)

    Space Complexity
    ----------------
    O(N)
    """
    seen = set([])
    end_reached = False
    while head.next:
        print(head.value)
        seen.add(head.value)
        while head.next.value in seen:
            if head.next.next:
                attach_node(head, head.next.next)
            else:
                head.next = None
                end_reached = True
                break
        if not end_reached:
            head = head.next


# class linkedList():
#     def __init__(self):
#         self.value = None
#         self.next = None
#         self.previous = None

#     def add_next(self, class_object):
#         self.next = class_object

#     def add_previous(self, class_object):
#         self.previous = class_object


#     def createLinkedList(self, array):
#         head = self
#         for value in array[:-1]:
#             head.value = value
#             head.next = linkedList()
#             head = head.next
#         head.value = array[-1]

#     def traverseLinkedList(self):
#         head = self
#         print(head.value, end=' ')
#         while head.next != None:
#             head = head.next
#             print(head.value, end=' ')
#         print("\n")


#     def removeDuplicates(self):
#         head = self
#         seen = set([])
#         while(head.next!=None):
#             seen.add(head.value)
#             duplicateRemoved = 0
#             while head.next.value in seen:
#                 duplicateRemoved = 1
#                 if head.next.next is None:
#                     head.next = None
#                 else:
#                     head.next = head.next.next
#             if not duplicateRemoved:
#                 head = head.next

#     def determineLengthList(self):
#         head = self
#         self.length = 0
#         while head:
#             self.length += 1
#             head = head.next

#     def returnKthtoLast(self,k):
#         self.determineLengthList()
#         head = self
#         for _ in range(self.length - k -1):
#             head = head.next
#         return head.value

#     def deleteKthfromFront(self,k):
#         head = self
#         for _ in range(k):
#             head = head.next
#         self.deleteFromHead(head)

#     def deleteFromHead(self, head):
#         while head.next.next != None:
#             self.traverseLinkedList()
#             head.value = head.next.value
#             head = head.next
#         head.value = head.next.value
#         head.next = None


#     def partitionList(self, x):
#         self.lessThanList = []
#         self.greaterThanList = []
#         self.xInList = False
#         head = self
#         self.lessThanList.append(head.value) if head.value <= x else self.greaterThanList.append(head.value)
#         if head.value == x:
#             self.xInList = True
#         while head.next != None:
#             head = head.next
#             if head.value == x:
#                 self.xInList = True
#             self.lessThanList.append(head.value) if head.value <= x else self.greaterThanList.append(head.value)

#         self.lessThanLinkedList = linkedList()
#         self.lessThanLinkedList.createLinkedList(self.lessThanList)

#         self.greaterThanLinkedList = linkedList()
#         self.greaterThanLinkedList.createLinkedList(self.greaterThanList)

#         self.lessThanLinkedList.traverseLinkedList()
#         self.greaterThanLinkedList.traverseLinkedList()

#     def createNumberFromList(self):
#         head = self
#         multiplier = 1
#         number = head.value * multiplier
#         while head.next != None:
#             head = head.next
#             multiplier = multiplier * 10
#             number = number + multiplier * head.value
#         return number

#     def reverseLinkedList(self):
#         self.createArrayFromList()
#         self.reversedList = linkedList()
#         self.reversedList.createLinkedList(np.flip(self.arrayFromList))
#         self.reversedList.createArrayFromList()

#     def createArrayFromList(self):
#         myList = []
#         head = self
#         myList.append(head.value)
#         while head.next != None:
#             head = head.next
#             myList.append(head.value)

#         self.arrayFromList = np.array(myList)

#     def checkPalindrome(self):
#         self.determineLengthList()
#         self.palindrome = True
#         for index in range(self.length):
#             if self.arrayFromList[index] != self.reversedList.arrayFromList[index]:
#                 self.palindrome = False