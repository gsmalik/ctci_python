from binarytree import tree, bst


def find_combinations(root):
    """
    Function to find all combinations that can result in the given BST.

    Parameters
    ----------
    root: ``BinaryNode``
        Root node of BST.

    Returns
    -------
    A list of all possible combinations that can result in given BST

    Time Complexity
    ---------------
    Way too complex. But looks like a form of O(2^N), where N is the number of
    nodes in the BST.

    Space Complexity
    ----------------
    TODO: Attempt space complexity calculations.
    Way too complex? Attempt this again
    """
    # If root is none, return empty combination.
    if root is None:
        return [[]]

    # Recursively find combinations of arrays that could have created the BST on
    # left of root.
    left_combinations = find_combinations(root.left)
    # Recursively find combinations of arrays that could have created the BST on
    # right of root.
    right_combinations = find_combinations(root.right)

    # We have left and right combinations. `left_combinations` is a list of
    # arrays and so is `right_combinations`. Each array in `left_combination`
    # can be combined with each array in `right_combination` to get the BST under
    # `root`. So, let us combine them and create a list of combined arrays.
    combinations = []
    for l_combination in left_combinations:
        for r_combination in right_combinations:
            for x in interweave(l_combination, r_combination):
                combinations.append(x)

    # Remember that in a BST, the root node is inserted first. So insert the root
    # node at start of every combination in `combinations`
    if combinations:
        combinations = [[root.value] + x for x in combinations]
    else:
        combinations = [[root.value]]
    return combinations


def interweave(left, right):
    """
    Function to interweave left and right arrays, while preserving relative order of
    elements within arrays and returning all interweaving combinations.

    Parameters
    ----------
    left: ``list/np.ndarray``
        First of two arrays that will be weaved with the second.

    right: ``list/np.ndarray``
        Second of two arrays that will be weaved with the second.

    Returns
    -------
    A list of all interweaved combinations.

    Time Complexity
    ---------------
    O(2*(l+r-1)C(r) + 4*(l+r-2)C(r) + 8*(l+r-3)C(r) + ... )
    = O(2^(N) + 2^(N-1) + 2^(N-2) + ..) = O(2^N), where l and r are the number of
    elements in `left` and `right` respectively and N is (l+r).

    Space Complexity
    ----------------
    O(l+r). Note that we do not account for the interweaved arrays in space complexity
    since that is part of the question and we add new combinations to it in-place,
    without using any additional storage. The space complexity is determined by the
    depth of recursion stack, which at worst can be (l+r) deep, when calling interweave
    in a depth first search style. For example, draw the interweave(left[1:, right])
    stack trace.
    """
    if left and right:
        # Recursively create list of combinations where left[0] is first element
        left_firsts = [[left[0]] + x for x in interweave(left[1:], right)]
        print(len(interweave(left[1:], right)))
        # Recursively create list of combinations where right[0] is first element
        right_firsts = [[right[0]] + x for x in interweave(left, right[1:])]
        print(len(interweave(left, right[1:])))

        # Add all combinations to list. This appends the two lists together
        return left_firsts + right_firsts

    # If at least one of `left` or `right` is empty
    return [left] if left else [right] if right else []


my_tree = bst(height=3)
print(my_tree)
print(find_combinations(my_tree.levels[0][0]))