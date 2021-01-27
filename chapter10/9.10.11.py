import numpy as np


def create_peaks_valleys(array):
    # create valleys
    for index in range(1, len(array) - 1, 2):
        min_elem = min(array[index - 1], array[index], array[index + 1])
        if min_elem == array[index - 1]:
            array[index], array[index - 1] = array[index - 1], array[index]
        elif min_elem == array[index + 1]:
            array[index], array[index + 1] = array[index + 1], array[index]

    # Create last peak
    if len(array) % 2 == 0:
        if array[-1] > array[-2]:
            array[-1], array[-2] = array[-2], array[-1]

    return array


test = np.random.randint(0, 10, 11)
print(create_peaks_valleys(test))