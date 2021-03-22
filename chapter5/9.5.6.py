def count_bit_flips(binary_repr_A, binary_repr_B):
    """
    Function to count number of bits to flip to make the 2 given numbers equal.

    Parameters
    ----------
    binary_repr_A: str
        Binary representation of first number.
    binary_repr_B: str
        Binary representation of second number.

    Returns
    -------
    Number of bit flips needed to make the 2 numbers equal.

    Time Complexity
    ---------------
    O(N), where N is the number of bits in the number with a longer binary
    representation.

    Space Complexity
    ----------------
    O(1).
    """
    # Make the 2 representations equal by extending the MSB of the shorter string if
    # needed.
    binary_repr_A = (
        f"{binary_repr_A[0]*(len(binary_repr_B)-len(binary_repr_A)) if (len(binary_repr_B)-len(binary_repr_A)) > 0 else ''}"
        + binary_repr_A
    )
    binary_repr_B = (
        f"{binary_repr_B[0]*(len(binary_repr_A)-len(binary_repr_B)) if (len(binary_repr_A)-len(binary_repr_B)) > 0 else ''}"
        + binary_repr_B
    )

    # Iterate bits and count flips needed
    flip = 0
    for char_A, char_B in zip(binary_repr_A, binary_repr_B):
        if char_A != char_B:
            flip += 1

    return flip


A = 29
binary_repr_A = "{0:032b}".format(A)
B = 15
binary_repr_B = "{0:032b}".format(B)

print(count_bit_flips(binary_repr_A, binary_repr_B))