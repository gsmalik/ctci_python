def permute_string(list_char):
    if len(list_char)==1:
        return list_char
    return create_list(list_char[0], permute_string(list_char[1:]))

def create_list(character, permutations):
    new_list = []
    for comb in permutations:
        for index in range(len(comb)+1):
            new_list.append(comb[:index]+character+comb[index:])
    return new_list

def remove_duplicates(string_chars):
    new_list = []
    for character in string_chars:
        if character not in new_list:
            new_list.append(character)
    return new_list


test_string = ['a','b','c','d','e', 'e', 'a', 'b']

print(permute_string(remove_duplicates(test_string)))

