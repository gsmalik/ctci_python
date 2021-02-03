def urlify(string, len_string):
    """
    Function to replace space character with '%20'.

    Parameters
    ----------
    string: ``list``
        List of string that needs to be converted to url, with appropriate space at end.

    len_string: ``int``
        Length of string, without accounting for whitespaces at end for url.

    Returns
    -------
    url version of string.

    Time Complexity
    ---------------
    O(N)

    Space Complexity
    ----------------
    O(1)
    """

    def _list_to_string(l):
        """
        Convert a list to a string.
        """
        s = ""
        for char in l:
            s += char
        return s

    # Create an index at the every end of the complete url list.
    replace_index = len(string) - 1

    # Start iterating from the index at which the non-url list ends.
    for char_index in reversed(range(len_string)):
        # If white space, introduce "%20" backwards, starting from replace index.
        if string[char_index] == " ":
            string[replace_index] = "0"
            string[replace_index - 1] = "2"
            string[replace_index - 2] = "%"
            replace_index -= 3
        # Otherwise, just move the non-space character to the replace index.
        else:
            string[replace_index] = string[char_index]
            replace_index -= 1
    
    # Return the updates list as a string.
    return _list_to_string(string)


test = "mr john smith"
print(urlify(list(test + " " * test.count(" ") * 2), len(test)))
