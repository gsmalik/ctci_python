import numpy as np


def find_rotation_point(array, left, right):
    if array[left] <= array[right]:
        return left
    if right - left == 1:
        return right
    else:
        mid = left + (right - left + 1) // 2
        print("left is", left, "mid is", mid, "right is", right)
        print(array[left], array[mid], array[right])
        assert (array[left] > array[mid]) != (array[right] < array[mid])

        if array[left] > array[mid]:
            return find_rotation_point(array, left, mid)
        else:
            return find_rotation_point(array, mid, right)


def find_element(array, element):
    rotation_point = find_rotation_point(array, 0, len(array) - 1)
    print("rotation point is", rotation_point)
    if element <= array[-1]:
        return np.where(array[rotation_point:] == element)[0] + rotation_point
    else:
        return np.where(array[:rotation_point] == element)[0]


# test = np.array([1,2,3,4,5,6,7])
test = np.array(
    [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 1, 2, 3, 4, 5, 6, 7]
)
print(find_element(test, 19))