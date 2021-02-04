from collections import defaultdict


def is_permutation(string1, string2):
    """
    Function to check if 2 strings are permutations of each other.

    Parameters
    ----------
    string1: ``str``
        String that needs to be checked for permuted combination.

    string2: ``str``
        String that needs to be checked for permuted combination.

    Returns
    -------
    True if strings are permutations. False otherwise.

    Time Complexity
    ---------------
    O(N)

    Space Complexity
    ----------------
    O(N)
    """
    # Return False if length of strings is not equal.
    if len(string1) != len(string2):
        return False

    # Create a default dictionary of int type, where if a new key is inserted,
    # the value is initialized with a 0.
    my_dict = defaultdict(int)

    # Loop over both strings by character. We expect count in default dict to be
    # zero for each character if these strings are to be permutations of each
    # other.
    for c1, c2 in zip(string1, string2):
        my_dict[c1] += 1
        my_dict[c2] -= 1

    # Return True if count of each character is zero. Return False otherwise.
    return sum([my_dict[x] == 0 for x in my_dict]) == len(my_dict)


print(is_permutation("test1", "1test"))
print(is_permutation("", ""))
print(is_permutation("test2", "test"))