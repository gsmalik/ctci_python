import numpy as np


def sort_anagram(array_strings):
    """
    Function to group anagrams together.

    Parameters
    ----------
    array_strings: list
        List of strings in which anagrams need to be grouped together

    Time Complexity
    ---------------
    NSlog(S), where N is the number of strings in 'array_strings' and S is the length
    of each string.

    Space Complexity
    ----------------
    NS, where N is the number of strings in 'array_strings' and S is the length
    of each string.
    """
    # sort each string and create a hash table using the sorted string as key
    # and all strings having same key (sorted string) will be anagrams
    my_dict = {}
    for string in array_strings:
        # create key
        key = "".join(np.sort([s for s in string]))
        # append if key exists, create new entry otherwise
        if key in my_dict:
            my_dict[key].append(string)
        else:
            my_dict[key] = [string]

    # the hash table can now be returned by treating all its values, distributed
    # over different keys, as a list. the string that came first in the
    # 'array_strings' will be the first key and so on. so reading the hash table
    # in order will preserve original order of 'array_strings' will grouping
    # anagrams together.
    return [item for sublist in list(my_dict.values()) for item in sublist]


test = ["test", "bye", "yo", "oy", "hello", "yeb"]
print(sort_anagram(create_list(test)))
