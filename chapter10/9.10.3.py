import numpy as np


def find_rotation_point(array, left, right):
    """
    Function to find rotation point of an array that is sorted and has been rotated an
    unknown number of times.

    Parameters
    ----------
    array: np.1darray
        Sorted, rotated array.
    left: int
        Left index of the search for rotation point
    right: int
        Right index of the search for rotation point

    Returns
    -------
    Index of rotation point in the array

    Time Complexity
    ---------------
    O(logN), where N is the number of elements in the array.

    Space Complexity
    ----------------
    O(logN), where N is the number of elements in the array. This function has a
    recursive stack depth of log(N).
    """
    # if array is already sorted between left and right
    if array[left] <= array[right]:
        return left
    # if only 2 elements remaining in array
    if right - left == 1:
        return left if array[left] <= array[right] else right

    # find middle point
    mid = (left + right) // 2

    # since a sorted array has been rotated, if array[mid] < array[left], that
    # must mean that the rotation point lies somewhere between left and mid
    if array[mid] < array[left]:
        return find_rotation_point(array, left, mid)
    # if above is not true, that must mean that rotation point lies somewhere
    # between mid and right
    else:
        return find_rotation_point(array, mid, right)


def find_element(array, element):
    """
    Function to find an element in an array that is sorted and has been rotated an
    unknown number of times.

    Parameters
    ----------
    array: np.1darray
        Sorted, rotated array.
    element: FP32
        Element that needs to be found

    Returns
    -------
    Index of element in the array

    Time Complexity
    ---------------
    O(logN), where N is the number of elements in the array. It takes log(N) time to
    find the rotation point. After that, we either search in 0:rotation_point or
    rotation_point:end, both of which are sorted arrays. Hence finding the element in
    these sorted arrays also takes log(N) time.

    Space Complexity
    ----------------
    O(logN), where N is the number of elements in the array. Finding rotation point
    and searching for element have a recursive stack depth of log(N).
    """
    # find rotation point of this array
    rotation_point = find_rotation_point(array, 0, len(array) - 1)
    # if element is less than last element of array, that means it must lie
    # between 'rotation_point' and end of array
    if element <= array[-1]:
        return np.where(array[rotation_point:] == element)[0] + rotation_point
    # otherwise it must lie between start of array and 'rotation_point'
    else:
        return np.where(array[:rotation_point] == element)[0]


test = np.array(
    [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 1, 2, 3, 4, 5, 6, 7]
)
print(find_element(test, 19))
