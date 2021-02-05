def check_rotation(string1, string2):
    """
    Function to check if a string is a rotation of another.

    Parameters
    ----------
    string1: ``str``
        String for which you are checking rotation.

    string2: ``str``
        String you are checking rotation against.


    Returns
    -------
    True if rotation. False otherwise.

    Time Complexity
    ---------------
    O(N), where N is the length of the longer strings. Checking substring can be
    done by iterating through 2 strings character by character.

    Space Complexity
    ----------------
    O(N). We need to concat string1 together, for which we need an additional
    space equal to length of string1.
    """

    def _is_substring(string1, string2):
        """Checks if string2 is a substring of string1."""
        return string2 in string1

    # For strings to be rotation of each other, they need to be of equal length.
    if len(string1) != len(string2):
        return False
    # You can concatenate string 1 back to back so that string2, if it exists,
    # can be found as a whole in "string1 + string1".
    else:
        return _is_substring(string1 + string1, string2)


print(check_rotation("waterbottle", "lewaterbott"))
