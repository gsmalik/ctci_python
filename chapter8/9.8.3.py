import numpy as np
import math


def search_magic_index(array, start, end):
    """
    Function to find a magic index in the given array.

    Parameters
    ----------
    array: np.1darray
        Array to search for magic index.
    start: int
        Starting index for searching.
    end: int
        Ending index for searching.

    Time Complexity
    ---------------
    O(N), where N is the number of nodes in the array.

    Space Complexity
    ----------------
    O(log(N)), where N is the number of nodes in the array.
    """
    if start <= end:
        # Calculate middle index and value at middle index.
        mid_index = (start + end) // 2
        mid_value = array[mid_index]

        # If the mid value is even bigger than the length of array, then that
        # means there is no magic index possible.
        if mid_value > end:
            return

        if mid_index == mid_value:
            print("Found magic index at", mid_value)

        if start != end:
            # When searching on the left side, you can basically skip all indices
            # that are bigger than the middle value.
            search_magic_index(array, start, min(mid_value, mid_index - 1))
            # When searching on the right side, you can similarly skip all
            # indices that are smaller than the middle value.
            search_magic_index(array, max(mid_value, mid_index + 1), end)


test = np.array([-2, 1, 1, 3, 4, 8])
search_magic_index(test, 0, len(test) - 1)
