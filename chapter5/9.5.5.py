def check_power_of_2(number):
    """
    Function to check if a number is a power of 2 or zero.
    """
    return (number & (number - 1)) == 0


print(check_power_of_2(0))
print(check_power_of_2(1))
print(check_power_of_2(8))
print(check_power_of_2(123))
print(check_power_of_2(256))