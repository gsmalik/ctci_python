def reverse_string(string):
    """
    Reverses string. Just needed for easier pythonic implementations. Do not
    consider for asymptotic analysis.
    """
    return string[::-1]


def insert_into(binary_1, binary_2, i, j):
    """
    Inserts one binary string into another.

    Parameters
    ----------
    binary_1: str
        Binary number in which to insert
    binary_2: str
        Binary number to insert.
    i: int
        Index to start insertion.
    j: int
        Index to end insertion.
    Time Complexity
    ---------------
    O(num_bits(binary_1)). You will `OR` each bit of `binary_1` with `binary_2` and a mask.

    Space Complexity
    ----------------
    O(1).
    """
    # Make sure exact space between i and j to insert binary_2
    assert len(binary_2) == j-i+1 
    
    # Convert binary numbers into lists for easier addressing.
    binary_1 = list(reverse_string(binary_1))
    binary_2 = list(reverse_string(binary_2))
    

    for index, bit in enumerate(binary_1): 
        if  i <= index <= j:
            binary_1[index] = binary_2[index-i]
        else:
            binary_1[index] = binary_1[index]

    return reverse_string(''.join(list(binary_1)))

i = 0
j = 3
N = "1010101011"
M = "0110"

print(insert_into(N, M, i, j))