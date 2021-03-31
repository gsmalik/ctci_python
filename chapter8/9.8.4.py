from copy import deepcopy as copy


def create_subsets(array):
    if len(array) == 1:
        return [[], [array[0]]]
    subsets = create_subsets(array[1:])
    cloned_subsets = subsets[:]

    for subset in subsets:
        cloned_subsets.append(subset + [array[0]])

    return cloned_subsets


num_elements = 3
subsets = create_subsets([x for x in range(num_elements)])
print(subsets, len(subsets))