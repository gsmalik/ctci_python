def flip_bit_win(string):
    """
    A function to determine index for bit flip to generate longest sequence of `1`s.

    Parameters
    ----------
    string: `str`
        The input bit string.

    Time Compexity
    --------------
    O(N), where N is the number of bits in the string.

    Space Complexity
    ----------------
    O(1).
    """
    # Set a maximum length to keep track of maximum length.
    # Set current length to keep track of current sequence length.
    max_len = cur_len = 0
    # Flag to determine if current sequence is broken.
    broken_seq = False
    # Loop over string
    for index, char in enumerate(string):
        # Increment current sequence length if current bit is 1.
        if char == "1":
            cur_len += 1
        if char == "0":
            # If sequence was already broken by pervious zero, this means that we
            # have maxed out extension of current sequence using a bit flip.
            if broken_seq:
                cur_len = 0
                broken_seq = False
            # If sequence is not broken, that means we can flip this 0 bit to 1
            # and keep extending current sequence.
            else:
                cur_len += 1
                broken_seq = True
        # Update max sequence length if current length exceeds previous best.
        if cur_len > max_len:
            place = index
            max_len = cur_len
    return max_len


number = 1775
binary_repr = "{0:032b}".format(number)
max_len = max(flip_bit_win(binary_repr), flip_bit_win(binary_repr[::-1]))
print(max_len)
