def next_num(binary_repr, find_largest=True):
    if find_largest:
        char_to_find = "1"
    else:
        char_to_find = "0"

    binary_repr = binary_repr[::-1]
    found_char = False
    for index, char in enumerate(binary_repr):
        if char == char_to_find:
            found_char = True
        if char == str(int(not(int(char_to_find)))) and found_char:
            break

    if index == 31:
        return binary_repr[::-1]


    binary_repr = (
        binary_repr[: index - 1]
        + str(int(not (int(binary_repr[index - 1]))))
        + str(int(not (int(binary_repr[index]))))
        + binary_repr[index + 1 :]
    )

    # Count number of 0s and 1s below index-2:0 (inclusive)
    num_zeros = sum([char == "0" for char in binary_repr[0 : index - 1]])
    num_ones = sum([char == "1" for char in binary_repr[0 : index - 1]])
    bits_flip = min(num_zeros, num_ones)

    list_zeros_indices = [
        index for index, char in enumerate(binary_repr[: index - 1]) if char == "0"
    ]
    list_zeros_indices = list_zeros_indices[0:bits_flip] if find_largest else list_zeros_indices[-bits_flip:]
    list_ones_indices = [
        index for index, char in enumerate(binary_repr[: index - 1]) if char == "1"
    ][-bits_flip:]
    list_ones_indices = list_ones_indices[-bits_flip:] if find_largest else list_ones_indices[0:bits_flip]

    for zeros_to_flip, ones_to_flip in zip(list_zeros_indices, list_ones_indices):
        binary_repr = (
            binary_repr[:zeros_to_flip]
            + str(int(not (int(binary_repr[zeros_to_flip]))))
            + binary_repr[zeros_to_flip+1:ones_to_flip]
            + str(int(not (int(binary_repr[ones_to_flip]))))
            + binary_repr[ones_to_flip+1:]
        )

    # Replace all numbers below index
    return binary_repr[::-1]


number = 1
binary_repr = "{0:032b}".format(number)
print(binary_repr)
print(next_num(binary_repr, True))
