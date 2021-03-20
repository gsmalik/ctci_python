def num_to_binary(num):
    """
    Converts a given number to fixed point 32 bit representation.

    Parameters
    ----------
    num: FP32
        Number to get representation of.

    Time Complexity
    ---------------
    O(1). We do fixed work.

    Space Complexity
    ----------------
    O(1).
    """
    assert 0 < num < 1
    binary_repr = ""
    for bits in range(1, 33):
        if num - 2 ** (-bits) >= 0:
            binary_repr += "1"
            num -= 2 ** (-bits)
        else:
            binary_repr += "0"
    if num != 0:
        raise ArithmeticError
    return binary_repr


num = 0.125
print(num_to_binary(num))
num = 0.1252
print(num_to_binary(num))
