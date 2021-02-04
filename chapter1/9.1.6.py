def compress_string(string):
    """
    Function to check if 2 strings are one edit away from each other.

    Parameters
    ----------
    string: ``str``
        String that needs to be compressed

    Returns
    -------
    Compressed string if compressed length will be shorter. Returns original
    string otherwise.

    Time Complexity
    ---------------
    O(N). We only loop over the string character by character once.

    Space Complexity
    ----------------
    O(1). We replace in-place. Hence, only need constant space for replacement
    variables.
    """

    def _list_to_string(l):
        """
        Convert a list to a string.
        """
        s = ""
        for char in l:
            s += str(char)
        return s

    def _return_original_string(string):
        """Determines if original string would be shorter than compresses string."""
        # Loop over string and compare compressed length with original length
        len_compressed_string = 0
        last_character = ""
        for character in string:
            if character != last_character:
                len_compressed_string += 2
                last_character = character
        if len_compressed_string >= len(string):
            return True

    # Check if original string would be shorter than compressed string.
    if _return_original_string(string):
        return string

    # Compress string in-place.
    index = 0
    list_string = list(string)
    last_character = list_string[0]
    count = 1
    for character in list_string[1:]:
        # If new character encountered, compress in-place by writing previous
        # character's compressed representation
        if character != last_character:
            list_string[index] = last_character
            index += 1
            list_string[index] = count
            index += 1
            count = 1
            last_character = character
        # Maintain a count if previous character is same as current character.
        else:
            count += 1
        print(index, character, count)

    # Compress remaining character is ending characters of the string were all
    # the same. For example, 'eee', 'ff'. We won't do this if last character in
    # the string was a new character. For example, 'ef', 'cd' etc.
    if character == last_character:
        list_string[index] = last_character
        index += 1
        list_string[index] = count

    return _list_to_string(list_string[: index + 1])


print(compress_string("abbcccdeffffffff"))