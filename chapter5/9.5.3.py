def flip_bit_win(string):
    max_len = cur_len = 0
    broken_seq = False
    for index, char in enumerate(string):
        if char == "1" :
            cur_len += 1
        if char == "0":
            if broken_seq:
                cur_len = 0
                broken_seq = False
            else:
                cur_len += 1
                broken_seq = True
        if cur_len > max_len:
            place = index
            max_len = cur_len
    return max_len




number = 1775
binary_repr = '{0:032b}'.format(number)
max_len = max(flip_bit_win(binary_repr), flip_bit_win(binary_repr[::-1]))
print(max_len)