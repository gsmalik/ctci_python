import numpy as np


def zeroMatrix(matrix, M, N):
    zeroOutRow = False
    zeroOutColumn = False

    for row in range(M):
        for column in range(N):
            if matrix[row][column] == 0:
                if row == 0:
                    zeroOutRow = True
                if column == 0:
                    zeroOutColumn = True
                matrix[0][column] = 0
                matrix[row][0] = 0

    for row in range(1, M):
        if matrix[row][0] == 0:
            matrix[row,:] = 0

    for column in range(1, N):
        if matrix[0][column] == 0:
            matrix[:,column] = 0

    if zeroOutRow:
        matrix[0,:] = 0

    if zeroOutColumn:
        matrix[:,0] = 0

    return matrix

# np.random.seed(1)
testMatrix = np.random.randint(7, size=(6, 4))
print(testMatrix)
print(zeroMatrix(testMatrix, 6, 4))

