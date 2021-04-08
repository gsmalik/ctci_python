import numpy as np

list_ways = []


def place_queen(list_previous_queens, N):
    """
    Function to place n queens such that no 2 queens lie along a diagonal, share a
    column or row.

    Parameters
    ----------
    list_previous_queens: list
        List of placed queens, with each index correpsonding to the indexed numbered
        column.
    N: int
        Size of chess board, where board dimension is N x N.

    Time complexity
    ---------------
    O(N^3), where N is the size of the chessboard.

    Space Complexity
    ----------------
    O(N), where N is the size of the chessboard.

    """
    # check if already placed queens are failing constraints
    if failed_constraints(list_previous_queens):
        return
    # if all queens are place and we have not violated constraints, this means
    # we have a valid placement. add it to list of valid placements.
    if len(list_previous_queens) == N:
        list_ways.append(list_previous_queens)
        return

    # try each row for this queen
    for row in range(N):
        place_queen(list_previous_queens + [row], N)


def failed_constraints(list_placement):
    # iterate through each column and check its constrains with the last column.
    # we only need to check constraints with last column because all the other
    # columns would be already satisfying their constraints with each other by
    # design.
    # for index, placement in enumerate(list_placement):
    for index in range(len(list_placement) - 1):
        if list_placement[-1] == list_placement[index] or (
            len(list_placement) - 1 - index
        ) == abs(list_placement[index] - list_placement[-1]):
            return True
    return False


N = 4
test = np.zeros((N, N))
place_queen([], N)
print(list_ways)
