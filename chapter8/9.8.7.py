# Create empty list to store permutations
list_permutations = []


def permute_string(current_string, avail_chars):
    """
    Function to create unique permutations by appending permutations of characters to
    a string.

    Parameters
    ----------
    current_string: str
        Current string to which new permutations will be appended to.
    avail_chars: list
        List of characters out of which new permutations can be created.

    Time Complexity
    ---------------
    O(N!), where N is the number of available characters. You can count the number
    of times 'permute_string' is called by creating a global empty test list and
    appending a 0 to it every time at the start of this function call. You can then
    divide the len of this list by the factorial of number of characters and see
    that it will be a constant as you keep increasing the number of characters.

    Space Complexity
    ----------------
    O(N), where N is the number of available characters.
    """
    # If there are no available characters, then no new permutions can be created
    # and you can append this current string to the list of permutations.
    if not avail_chars:
        list_permutations.append(current_string)
        return

    # Create new permutations by iterating through characters and appending them
    # to current string and creating permutations through remaining characters.
    for index, character in enumerate(avail_chars):
        permute_string(
            current_string + character, avail_chars[:index] + avail_chars[index + 1 :]
        )


permute_string("", ["a", "b", "c", "d"])
print(list_permutations)