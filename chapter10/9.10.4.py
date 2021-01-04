import numpy as np

def elementAt(array, index):
    print("probing index", index)
    if index > len(array) - 1:
        return -1
    return array[index]


def find_length(array):

    power = 0
    while elementAt(array, 2 ** power) != -1:
        power += 1

    if power == 0:
        return power

    return 2 ** (power - 1) + find_length(array[2 ** (power - 1) :])

def find_element(array, element):
    length = find_length(array) + 1

    return np.where(array[:length]==element)[0]

test = np.array(
    [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 1, 2, 3, 4, 5, 6, 7]
)

print(find_element(test,1))