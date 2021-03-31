import numpy as np


# create a list to hold all feasible paths from source coordinates to destination
# coordinates
paths = []
def find_paths(src_row, src_col, dst_row, dst_col, grid, current_path):
    """
    Function to find all feasible paths between source and destination on a 2D grid.

    Parameters
    ----------
    src_row: int
        Starting row index.
    src_col: int
        Starting column index.
    dst_row: int
        Target row index.
    dst_col: int
        Target column index.
    grid: np.2darray
        A 2D numpy array where 1 at a particular grid coordinate means that it is blocked.
    current_path: list
        Current path that lead to reaching the source coordinates.

    Time Complexity
    ---------------
    O(2^(r+c)).

    Space Complexity
    ----------------
    O(r+c)

    """
    # append current source coordinates to the current path
    current_path.append((src_row, src_col))

    # return successfully if destination coordinates reached
    if src_row == dst_row and src_col == dst_col:
        paths.append(current_path)
        return

    # abandon current path and return if we have reached coordinates from which
    # we cannot reach destination coordinates
    if src_row > dst_row or src_col > dst_col or grid[src_row][src_col] == 1:
        return

    # move in the direction of destination coordinates by going right. remember
    # that 'current_path' is a list and hence mutable and will be changed in place
    # so pass a copy of 'current_path'
    find_paths(src_row, src_col + 1, dst_row, dst_col, grid, current_path[:])

    # move in the direction of destination coordinates by going down. remember
    # that 'current_path' is a list and hence mutable and will be changed in place
    # so pass a copy of 'current_path'
    find_paths(src_row + 1, src_col, dst_row, dst_col, grid, current_path[:])


r = 3
c = 3
grid = np.random.randint(0, 2, (r, c))
grid[0, 0] = 0
grid[r - 1, c - 1] = 0
print(grid)
# grid = update_grid(grid)
find_paths(0, 0, r - 1, c - 1, grid, [])
print(paths)
# print(grid[0][0].paths)
