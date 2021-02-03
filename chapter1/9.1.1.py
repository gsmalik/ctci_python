def is_unique(string):
    """
    Function to check if each character in string is unique.

    Parameters
    ----------
    string: ``str``
        String that needs to be checked for character uniqueness.

    Returns
    -------
    True if string is unique. False otherwise.

    Time Complexity
    ---------------
    O(N)

    Space Complexity
    ----------------
    O(N)
    """
    # Create a dictionary to mimic a hash table for O(1) lookup and insertion.
    my_dict = {}
    # Loop through each character in string
    for character in string:
        # Return False if character already exists in dictionary.
        if character in my_dict.keys():
            return False
        # Add it to dictionary if character not encountered before
        else:
            my_dict[character] = True
    return True


print(is_unique("uniq"))
print(is_unique(""))
print(is_unique("not_uniq"))