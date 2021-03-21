def next_num(binary_repr, find_largest=True):
    """
    Function to find the next largest or smallest number with the same number of '1'
    bits in its binary representation.

    Parameters
    ----------
    binary_repr: str
        Binary representation of string with MSB at index 0.
    find_largest: bool
        If set, function returns next largest. Else, returns next smallest.

    Returns
    -------
    Next largest or smallest binary representation of number with same number of '1'
    bits.

    Time Complexity
    ---------------
    O(D), where D is the index of the first trailing 1 trailed by a 0 (next smallest)
    or first 0 trailed by 1 (next largest).

    Space Complexity
    ---------------
    O(D), where D is the index of the first trailing 1 trailed by a 0 (next smallest)
    or first 0 trailed by 1 (next largest).
    """
    # If we are finding next largest, then we have to find the first '-' after
    # finding a '1' while going from right to left (LSB)
    if find_largest:
        char_to_find = "0"
    # Other way around when finding next smallest
    else:
        char_to_find = "1"

    # Reverse binary repr for natural feeling iteration
    binary_repr = binary_repr[::-1]

    # See if we found the trailing character at zero bit index
    trailing_char_not_found = binary_repr[0] != str(int(not (int(char_to_find))))
    index = 1

    # We also keep a track of 0s and 1s we have encountered so far for later calculation
    num_ones = int(binary_repr[0] == "1")

    # We have to find the character we are looking for and also need to ensure we have
    # found the trailing character.
    while (
        binary_repr[index] != char_to_find or trailing_char_not_found
    ) and index < 32:
        if binary_repr[index] == str(int(not (int(char_to_find)))):
            trailing_char_not_found = False
        num_ones += int(binary_repr[index] == "1")
        index += 1

    # If 1/0 lie at index 31, then the number itself is the largest/smallest for those
    # number of '1's.
    if index == 31:
        return binary_repr[::-1]

    # Flip the bit at current index, which contains the character we need to find.
    binary_repr = (
        binary_repr[:index]
        + str(int(not (int(char_to_find))))
        + binary_repr[index + 1 :]
    )

    # Create a mask of 0s for largest and 1s for smallest which is equal to number of
    # bits before index.
    mask = f"{0 if find_largest else 1}" * index

    # Set the mask
    binary_repr = mask + binary_repr[index:]

    # In the case of finding next largest, by flipping a 0 bit to 1 and adding 0s
    # after that, we already have a number that is greater than our original number.
    # Now, we need to add 1s to the zeroed out bits to make sure final number has
    # equal number of 1 bits. To do this, we should make the LSBs equal to 1 because
    # this will make sure that the final number is just bigger than our original
    # number, which is what what we want while making sure that the new final number
    # has equal amount of 1 bits.
    if find_largest:
        binary_repr = "1" * (num_ones - 1) + binary_repr[num_ones - 1 :]

    # In the case of finding next smallest, by flipping a 1 bit to 0 and adding 1s
    # after that, we already have a number that is smaller than our original number.
    # Now, we need to add 0s to the 'one'd out bits to make sure final number has
    # equal number of 1 bits. To do this, we should make the LSBs equal to 0 because
    # this will make sure that the final number is just smaller than our original
    # number, which is what what we want while making sure that the new final number
    # has equal amount of 1 bits.
    else:
        binary_repr = (
            "0" * (index - (num_ones + 1)) + binary_repr[index - (num_ones + 1) :]
        )

    # Flip it back for easier reading
    return binary_repr[::-1]


number = int("011011001111100", 2)
binary_repr = "{0:032b}".format(number)
print(next_num(binary_repr, True))

number = int("010011110000011", 2)
binary_repr = "{0:032b}".format(number)
print(next_num(binary_repr, False))