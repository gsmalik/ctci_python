def swap_even_odd(number):
    """
    Function to swap even and odd bits in binary representation of given number.

    Parameters
    ----------
    number: int
        The number whose binary representation's even and odd bits need to be swapped.

    Returns
    -------
    Swapped number in integer form.

    Time Complexity
    ---------------
    O(1).

    Space Complexity
    O(1).
    """
    # Convert number to binary representation
    number = "{0:032b}".format(number)
    # Create a mask that zeroes out even bits
    mask_zeros_even = ""
    # Create a mask that zeroes out odd bits
    mask_zeros_odd = ""
    for x in range(len(number)):
        mask_zeros_even += f"{1 if x%2 else 0}"
        mask_zeros_odd += f"{0 if x%2 else 1}"

    # Reverse masks to align with number's binary representation
    mask_zeros_even = mask_zeros_even[::-1]
    mask_zeros_odd = mask_zeros_odd[::-1]

    # Perform bitwise AND with the even mask and then right shift resultant number.
    # Perform bitwise AND with the odd mask and then left shift resultant number.
    # Perform bitwise OR on the 2 binary numbers.
    return int(
        bin((int(mask_zeros_even, 2) & int(number, 2)) >> 1)[2 : len(number) + 2], 2
    ) | int(
        bin(((int(mask_zeros_odd, 2) & int(number, 2)) << 1))[2 : len(number) + 2], 2
    )


number = 10
print(swap_even_odd(number))