import numpy as np


def zero_matrix(matrix, M, N):
    """
    Function to zero out its entire row and column if an element is 0 in the
    given matrix.

    Parameters
    ----------
    matrix: ``np.ndarray``
        Matrix that needs to be rotated.

    M: ``int``
        Number of rows in the matrix.

    M: ``int``
        Number of columns in the matrix.

    Returns
    -------
    Zeroed out matrix

    Time Complexity
    ---------------
    O(N^2). We touch each element once.

    Space Complexity
    ----------------
    O(1). We zero out in-place.
    """

    # Define flags to capture special condition. The typical idea is to iterate
    # element by element of the matrix and if an element at (row, column) is zero,
    # set its (0, column) and (row, 0) elements to zero. But there is a corner
    # case, which is that for elements that are zero in the topmost row or
    # leftmost column, then we would set (0,0) as 0, and there would be no way
    # for us to know if this was marked by a zero element in the topmost row or
    # leftmost column. We use these flags to track this corner case.
    zero_out_row = False
    zero_out_column = False

    # Mark elements by iterating through matrix.
    for row in range(M):
        for column in range(N):
            if matrix[row][column] == 0:
                if row == 0:
                    zero_out_row = True
                if column == 0:
                    zero_out_column = True
                matrix[0][column] = 0
                matrix[row][0] = 0

    # Set entire row to 0.
    for row in range(1, M):
        if matrix[row][0] == 0:
            matrix[row, :] = 0

    # Set entire column to 0.
    for column in range(1, N):
        if matrix[0][column] == 0:
            matrix[:, column] = 0

    # Handle corner case
    if zero_out_row:
        matrix[0, :] = 0

    if zero_out_column:
        matrix[:, 0] = 0

    return matrix


# np.random.seed(1)
test_matrix = np.random.randint(7, size=(6, 4))
print(test_matrix)
print(zero_matrix(test_matrix, 6, 4))
