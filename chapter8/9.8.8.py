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
    O(N!), where N is the number of available characters.

    Space Complexity
    ----------------
    O(N^2), where N is the number of available characters.
    """
    # If there are no available characters, then no new permutions can be created
    # and you can append this current string to the list of permutations.
    if not avail_chars:
        list_permutations.append(current_string)
        return

    # Iterate through avail_chars and create a dictionary to track if a character
    # can been used. True means its available to use and False means not.
    dict_avail = {}
    for character in avail_chars:
        dict_avail[character] = True

    # Create new permutations by iterating through characters and appending them
    # to current string and creating permutations through remaining characters.
    for index, character in enumerate(avail_chars):
        if dict_avail[character]:
            dict_avail[character] = False
            permute_string(
                current_string + character,
                avail_chars[:index] + avail_chars[index + 1 :],
            )


permute_string("", ["a", "a", "b", "b", "c"])
print(list_permutations)