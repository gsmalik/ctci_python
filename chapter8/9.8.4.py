from copy import deepcopy as copy

def create_subset(array):
    if len(array) == 1:
        return [(), (array[0],)]
    else:
        len_min_1_subset = create_subset(array[:-1])
        return clone_array(len_min_1_subset, array[-1])

def clone_array(subset, element):

    cloned_array = copy(subset)
    for tup in subset:
        cloned_array.append(tup + (element,))
    return cloned_array

num_elements = 5
print(create_subset([x for x in range(num_elements)]))