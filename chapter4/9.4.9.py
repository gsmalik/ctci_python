from binarytree import tree, bst

def find_combinations(root):
    if root is None:
        return [[]]

    left_combinations = find_combinations(root.left)
    right_combinations = find_combinations(root.right)

    combinations = []
    for l_combination in left_combinations:
        for r_combination in right_combinations:
            for x in mix_n_match(l_combination, r_combination):
                combinations.append(x)

    if combinations:
        combinations = [[root.value] + x for x in combinations]
    else:
        combinations = [[root.value]]
    return combinations

def mix_n_match(left, right):
    if left and right:
        # Make first element left
        left_firsts = [[left[0]] + x for x in mix_n_match(left[1:], right)]
        # Make first element right
        right_firsts = [[right[0]]+x for x in mix_n_match(left, right[1:])]

        # Add all combinations to list
        return left_firsts +right_firsts

    return [left] if left else [right] if right else []

my_tree = bst(height=2)
print(my_tree)
print(find_combinations(my_tree.levels[0][0]))