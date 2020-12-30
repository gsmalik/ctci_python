import numpy as np

def sort_anagram(array_strings):
    pass
    # Sort each string in array
    my_dict = {}
    for _, string in enumerate(array_strings):
        key = create_string(np.sort(create_list(string)))
        if key in my_dict:
            my_dict[key].append(string)
        else: 
            my_dict[key] = [string]
        

    return [item for sublist in list(my_dict.values()) for item in sublist]

def create_list(string):
    char_list = []
    for char in string:
        char_list.append(char)
    return char_list

def create_string(list_chars):
    string = ""
    for char in list_chars:
        string += char
    return string

test = ['test','bye', 'yo', 'oy','hello','yeb']
print(sort_anagram(create_list(test)))