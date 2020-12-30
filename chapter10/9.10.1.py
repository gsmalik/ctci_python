import numpy as np

def merge_arrays(array_a, len_a, array_b):
    len_merged_array = len_a + len(array_b)
    index_array_merged = len_merged_array - 1
    index_array_a = len_a - 1
    index_array_b = len(array_b) - 1

    while index_array_b >= 0:
        if index_array_a >= 0 and array_a[index_array_a] > array_b[index_array_b]:
            array_a[index_array_merged] = array_a[index_array_a]
            index_array_a -= 1
        else:
            array_a[index_array_merged] = array_b[index_array_b]
            index_array_b -= 1
        index_array_merged -= 1
    return array_a


len_a = 10
len_b = 5
test_a = np.sort(np.random.randint(0, 100, (len_a + len_b)))
test_b = np.sort(np.random.randint(0, 100, (len_b)))
print("array a", test_a)
print("array b", test_b)
print(merge_arrays(test_a, len_a, test_b))
