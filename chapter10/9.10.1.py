import numpy as np


def merge_arrays(array_a, len_a, array_b):
    """
    Function to merge two sorted arrays

    Parameters
    ----------
    array_a: np.1darray
        Array that has a large enough buffer at end to absorb other array for merging.
    len_a: int
        Length of 'array_a', without the buffer.
    array_b: np.1darray
        The other smaller array

    Returns
    -------
    Merged, sorted array

    Time Complexity
    ---------------
    O(B), where B is the number of elements in 'array_b'.

    Space Complexity
    ----------------
    O(1).
    """
    # the important aspect is to start merging from the back. create an index
    # tracker for that.
    index_array_merged = len_a + len(array_b) - 1
    # references to keep a track of which elements have been merged, starting
    # back
    index_array_a = len_a - 1
    index_array_b = len(array_b) - 1

    # keep merging till all elements of 'array_b' have been merged in
    while index_array_b >= 0:
        # since merging in reverse, bigger element will be merged first
        if index_array_a >= 0 and array_a[index_array_a] > array_b[index_array_b]:
            array_a[index_array_merged] = array_a[index_array_a]
            index_array_a -= 1
        else:
            array_a[index_array_merged] = array_b[index_array_b]
            index_array_b -= 1
        index_array_merged -= 1
    return array_a


len_a = 10
len_b = 5
test_a = np.sort(np.random.randint(0, 100, (len_a + len_b)))
test_b = np.sort(np.random.randint(0, 100, (len_b)))
print("array a", test_a)
print("array b", test_b)
print(merge_arrays(test_a, len_a, test_b))
