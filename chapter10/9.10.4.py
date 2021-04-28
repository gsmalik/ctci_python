import numpy as np


def element_at(array, index):
    print("probing index", index)
    if index > len(array) - 1:
        return -1
    return array[index]


def find_length(array):
    """
    Function to find length of given array.

    Parameters
    ----------
    array: np.1darray
        Array whose length needs to be determined.

    Time Complexity
    ---------------
    O(logN), where N is the number of elements in the array.

    Space Complexity
    ----------------
    O(logN), where N is the number of elements in the array.
    """
    power = 0
    while element_at(array, 2 ** power) != -1:
        power += 1
    return 2 ** power


def find_element(array, element):
    """
    Function to find an element in a sorted array whose length cannot be probed directly.

    Parameters
    ----------
    array: np.1darray
        Array in which the element needs to be found.
    element

    Time Complexity
    ---------------
    O(logN), where N is the number of elements in the array. Technically, the length
    found via 'find_length' can give a length of 2N. But a binary search on an array of
    length 2N will take log(N)+1 time, which results in overall time complexity being
    O(logN). Note that binary search will typically be modified to take into account -1
    being bigger than the element being searched for. That is an easy change

    Space Complexity
    ----------------
    O(logN), where N is the number of elements in the array. Stack depth, just like
    time complexity, is log(N) + 1.
    """
    length = find_length(array) + 1

    return np.where(array[:length] == element)[0]


test = np.array(
    [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 1, 2, 3, 4, 5, 6, 7]
)

print(find_element(test, 1))
