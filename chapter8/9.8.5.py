def sort_nums(num1, num2):
    # retuns bigger, smaller
    if num1 > num2:
        return num1, num2
    else:
        return num2, num1


def mult_numbers(num1, num2, rec=0):
    bigger_num, smaller_num = sort_nums(num1, num2)

    if smaller_num == 1:
        return bigger_num
    elif smaller_num == 0:
        return smaller_num
    else:
        return mult_numbers(bigger_num, smaller_num >> 1, rec + 1) + mult_numbers(
            bigger_num, smaller_num - (smaller_num >> 1), rec + 1
        )


print(mult_numbers(17, 23))

