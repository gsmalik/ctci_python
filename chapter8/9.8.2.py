import numpy as np
import copy


class Node:
    def __init__(self, r, c, obstacle):
        self.r = r
        self.c = c
        self.paths = []
        self.down = None
        self.right = None
        self.obstacle = obstacle


def find_path(r_start, c_start, r_goal, c_goal):
    if grid[r_start][c_start].paths:
        return grid[r_start][c_start]

    if r_start == r_goal and c_start == c_goal:
        grid[r_goal][c_goal].paths = [[(r_goal, c_goal)]]
        return grid[r_goal][c_goal]

    cannot_move = True
    # If moving down is possible
    if r_start + 1 < np.shape(grid)[0]:
        if not grid[r_start + 1][c_start].obstacle:
            cannot_move = False
            # Add this current Node to start of each path for the node below
            add_begining_node(
                grid[r_start][c_start], find_path(r_start + 1, c_start, r_goal, c_goal)
            )

    if c_start + 1 < np.shape(grid)[1]:
        # If moving right is possible
        if not grid[r_start][c_start + 1].obstacle:
            cannot_move = False
            # Add this current Node to start of each path for the node below
            add_begining_node(
                grid[r_start][c_start], find_path(r_start, c_start + 1, r_goal, c_goal)
            )

    # If cannot move
    if cannot_move:
        return None
    else:
        return grid[r_start][c_start]


def add_begining_node(node, neighbour_node):
    if neighbour_node:
        temp_paths = copy.deepcopy(neighbour_node.paths)
        for each_path in temp_paths:
            each_path.insert(0, (node.r, node.c))
            node.paths.append(each_path)

def update_grid(grid):
    rows, columns = np.shape(grid)
    array = np.ndarray((rows, columns), dtype=np.object)
    for r in range(rows):
        for c in range(columns):
            array[r][c] = Node(r, c, bool(grid[r][c]))
    return array


r = 3
c = 3
grid = np.random.randint(0, 2, (r, c))
grid[0, 0] = 0
grid[r - 1, c - 1] = 0
print(grid)
grid = update_grid(grid)
find_path(0, 0, r - 1, c - 1)
print(grid[0][0].paths)
