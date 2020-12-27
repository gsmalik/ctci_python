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

print(permute_string(['a','b','c','d','e']))

