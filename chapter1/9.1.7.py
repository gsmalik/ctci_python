import numpy as np


def rotate_matrix(matrix, size_matrix):
    """
    Function to rotate the matrix 90 degree clockwise.

    Parameters
    ----------
    matrix: ``np.ndarray``
        Matrix that needs to be rotated

    size_matrix: ``int``
        Number of rows = columns of the matrix

    Returns
    -------
    Rotated matrix

    Time Complexity
    ---------------
    O(N^2). We touch each element once

    Space Complexity
    ----------------
    O(1). We replace in-place. Hence, only need constant space for replacement
    variables.
    """

    def _rotate_outer_gear(matrix, size_matrix):
        """Rotate outermost gear of given matrix"""

        # Loop over the 0th row element by element, rotating each element as you go
        for column in range(size_matrix - 1):
            # Element at (0, column) goes to (column, size_matrix-1)
            temp1 = matrix[column][size_matrix - 1]
            matrix[column][size_matrix - 1] = matrix[0][column]

            # Element at (column, size_matrix-1) goes to (size_matrix-1, size_matrix-1-column)
            temp2 = matrix[size_matrix - 1][size_matrix - 1 - column]
            matrix[size_matrix - 1][size_matrix - 1 - column] = temp1

            # Element at (size_matrix-1, size_matrix-1-column) goes to (size_matrix-1-column, 0)
            temp1 = matrix[size_matrix - 1 - column][0]
            matrix[size_matrix - 1 - column][0] = temp2

            # Element at (size_matrix-1-column, 0) goes to (0, column)
            matrix[0][column] = temp1
        return matrix

    # Each gear level quantifies which gear is rotated. Think of a gear as a
    # peeled layer of a 2D rubix. You first rotate the outermost gear, then
    # the next gear inside and so on.
    for gearLevel in range(int(size_matrix / 2)):
        # Only updates to the specific gear are applied
        matrix[
            gearLevel : size_matrix - gearLevel, gearLevel : size_matrix - gearLevel
        ] = _rotate_outer_gear(
            matrix[
                gearLevel : size_matrix - gearLevel, gearLevel : size_matrix - gearLevel
            ],
            size_matrix - 2 * gearLevel,
        )
    return matrix


N = 5
matrix = np.random.randint(0, 100, (N, N))
print("Original Matrix is:\n", matrix)
print("Clockwise 90 degrees rotated matrix:\n", rotate_matrix(matrix, N))
