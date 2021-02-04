def check_within_one_edit(string1, string2):
    """
    Function to check if 2 strings are one edit away from each pther.

    Parameters
    ----------
    string1: ``str``
        String that needs to be checked for one edit condition.

    string2: ``str``
        String that needs to be checked for one edit condition.

    Returns
    -------
    True if strings are one edit away from each other. False otherwise.

    Time Complexity
    ---------------
    O(N). Remember, one of these strings can only be longer than one character.
    Hence, time complexity is still  O(N), where N is length of shorter string.

    Space Complexity
    ----------------
    O(1).
    """

    def _determine_string_rel(string1, string2):
        if len(string1) >= len(string2):
            return string1, string2
        else:
            return string2, string1

    # One edit mandates difference between lengths of strings be <= 1.
    if abs(len(string1) - len(string2)) > 1:
        return False

    # Determine longer and shorter string between the 2 strings.
    long_string, short_string = _determine_string_rel(string1, string2)

    long_string_index = 0
    count = 0
    # Loop over the shorter string and compare characters
    for character in short_string:
        if character != long_string[long_string_index]:
            count += 1
            # If length is not equal, then that means that a character is inserted,
            # hence, jump this character.
            if len(long_string) != len(short_string):
                long_string_index += 1
        long_string_index += 1
    return not count > 1


print(check_within_one_edit("pale", "ple"))
print(check_within_one_edit("pale", "plee"))
print(check_within_one_edit("pales", "pale"))
print(check_within_one_edit("pale", "able"))
print(check_within_one_edit("pale", "bake"))