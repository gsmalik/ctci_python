def count_bit_flips(binary_repr_A, binary_repr_B):
    print(binary_repr_A, binary_repr_B)
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