def get_string_at_index(file, index):
    return file[index]


def swap_strings(file, node_index, orig_index):
    file[orig_index], file[node_index] = file[node_index], file[orig_index]
    return file


def heap_sort(file):
    """
    T = O(nlogn) = O(log(n!)). Creating the first heap of entire file takes O(n)
    time (weird derivation. See https://www.youtube.com/watch?v=k72DtCnY4MU). Then
    each time you have to heapify the top element (after swap), that will take log(n-1)
    for first, then log(n-2) for second and so on. Adding all this, it becomes O(log(n!))
    which can be written as O(nlogn) loosely. Not super sure why everyone says time
    complexity is nlogn whereas it should be log(n!).

    S = O(1). Just using a temp variable to do swaps. Everything is in-place.
    """

    def heapify_complete_file(file):
        # Hepaify upper half of string of file. Upper half enough because
        # we will swap with children (2*index+1, 2*index+2) inside this, which
        # lie in lower half.
        for index in range(len(file) // 2, -1, -1):
            file = heapify(file, index)
        return file

    def heapify(file, node_index):

        orig_index = node_index
        left_child_index = 2 * node_index + 1
        right_child_index = 2 * node_index + 2

        # Decide which node to swap with. Will swap with bigger child, if exists.
        if left_child_index < len(file) and get_string_at_index(
            file, left_child_index
        ) > get_string_at_index(file, node_index):
            node_index = left_child_index

        if right_child_index < len(file) and get_string_at_index(
            file, right_child_index
        ) > get_string_at_index(file, node_index):
            node_index = right_child_index

        # Do the swap. Heapify the current element. Note the current element is the
        # orgiginal element. It has just been moved and we are calling heapify on its
        # latest position
        if node_index != orig_index:
            file = swap_strings(file, orig_index, node_index)
            file = heapify(file, node_index)
        return file

    len_file = len(file)

    # Heapify entire file once
    file = heapify_complete_file(file)
    for index in range(len_file - 1, -1, -1):
        # Swap first (max) and last element (of file size index+1).
        file = swap_strings(file, 0, index)

        # Heapify remaining file to find next max element
        file[:index] = heapify(file[:index], 0)

    return file


import random
import string
N = 10
test = []
for _ in  range(10):
    test.append(''.join(random.choices(string.ascii_uppercase, k=random.randint(1,10))))
print("Original File:", test)
print("Sorted File:", heap_sort(test))