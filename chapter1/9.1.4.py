def palindrome_permutation(string):
    """
    Function to check if string is permutation of palindrome.

    Parameters
    ----------
    string1: ``str``
        String that needs to be checked for permuted palindrome.

    Returns
    -------
    True if string is permuation. False otherwise.

    Time Complexity
    ---------------
    O(N). ASCII list takes constant time to loop. Hence, ignored.

    Space Complexity
    ----------------
    O(1). ASCII length is constant. Hence, ignored.
    """

    # Create an ascii character count.
    asciiList = [0]*128

    # Iterate through each character in string and update respective count.
    # Ignore space character (" ").
    for character in string:
        print(character, ord(character))
        asciiList[ord(character)] += 1 if character != " " else 0

    # For a string to be a combination of palindrome, each character
    # should occur twice except one, which would be middle of palindrom.
    oddOccurences = 0
    for count in asciiList:
        if count % 2 != 0:
            oddOccurences += 1
    if oddOccurences > 1:
        return False
    else:
        return True

print(palindrome_permutation("tactrc a"))
