import numpy as np


def create_peaks_valleys(array):
    """
    Function to arrange given array into alternating peaks and valleys.

    Parameters
    ----------
    arrays: np.1darray
        Array that needs to be arranged

    Time Complexity
    ---------------
    O(N), where N is the number of elements in the array.

    Space Complexity
    ----------------
    O(1).
    """
    for index in range(len(array) - 1):
        peak = index % 2 == 0
        valley = not peak
        if (peak and array[index] < array[index + 1]) or (
            valley and array[index] > array[index + 1]
        ):
            array[index], array[index + 1] = array[index + 1], array[index]
    return array


test = np.random.randint(0, 100, 10)
print(test)
print(create_peaks_valleys(test))