def mult_numbers(num1, num2):
    """
    Function to multiple 2 positive integers using only addition, subtraction and
    bit shift operators.

    Parameters
    ----------
    num1: int
        First operand.
    num2: int
        Second operand.

    Time Complexity
    ---------------
    O(log(N)), where N is the smaller of the 2 numbers.

    Space Complexity
    ----------------
    O(log(N)), where N is the smaller of the 2 numbers.
    """
    # determine the bigger and smaller number.
    bigger_num, smaller_num = (
        num1 if num1 > num2 else num2,
        num1 if num1 < num2 else num2,
    )

    # exit conditions
    if smaller_num == 1:
        return bigger_num
    if smaller_num == 0:
        return smaller_num
    
    # shift right smaller number and multiply it with bigger number + multiply
    # remaining of the smaller number with bigger number.
    return mult_numbers(bigger_num, smaller_num >> 1) + mult_numbers(
            bigger_num, smaller_num - (smaller_num >> 1)
        )


print(mult_numbers(4, 23))
print(mult_numbers(4, 100))
