import numpy as np
import math


def search_magic_index(array, start, end):
    if start <= end:
        mid_index = int(((start + end) / 2))
        print("mid index:", mid_index, "start:", start, "end:", end)
        mid_value = array[mid_index]

        if mid_index == mid_value:
            print("Found magic index at", mid_value)
        if start != end:
            search_magic_index(array, start, min(mid_value, mid_index - 1))
            search_magic_index(array, max(mid_value, mid_index + 1), end)


test = np.array([0, 1, 1, 3, 4, 10005, 100, 10, 10, 10, 10])
search_magic_index(test, 0, len(test) - 1)

