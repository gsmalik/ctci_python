import numpy as np


def rotateMatrix(matrix, sizeMatrix):
    for gearLevel in range(int(sizeMatrix / 2)):
        matrix[
            gearLevel : sizeMatrix - gearLevel, gearLevel : sizeMatrix - gearLevel
        ] = rotateOuterGear(
            matrix[
                gearLevel : sizeMatrix - gearLevel, gearLevel : sizeMatrix - gearLevel
            ],
            sizeMatrix - 2 * gearLevel,
        )
    return matrix


def rotateOuterGear(matrix, sizeMatrix):
    for column in range(sizeMatrix - 1):
        temp1 = matrix[column][sizeMatrix - 1]
        matrix[column][sizeMatrix - 1] = matrix[0][column]

        temp2 = matrix[sizeMatrix - 1][sizeMatrix - 1 - column]
        matrix[sizeMatrix - 1][sizeMatrix - 1 - column] = temp1

        temp1 = matrix[sizeMatrix - 1 - column][0]
        matrix[sizeMatrix - 1 - column][0] = temp2

        matrix[0][column] = temp1
    return matrix


matrix = np.random.randint(0, 100, (1, 1))
print(np.rot90(matrix,3))
print(rotateMatrix(matrix, 1))
