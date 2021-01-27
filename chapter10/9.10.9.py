import numpy as np


def find_element(matrix, element):
    row = 0
    col = np.shape(matrix)[1] - 1
    while row < np.shape(matrix)[0] and col >= 0:
        if matrix[row][col] == element:
            return (row, col)
        elif matrix[row][col] > element:
            col -= 1
        else:
            row += 1
    return False


def create_sorted_matrix(rows, cols):
    return np.reshape(np.sort(np.random.randint(0, 75, (rows * cols))), (rows, cols))


rows = 5
cols = 10
test = create_sorted_matrix(rows, cols)
print(test)
print(find_element(test, 10))