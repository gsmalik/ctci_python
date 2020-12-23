import numpy as np


def bubble_sort(array):
    """
    T = O(n).

    S = 1. Input space not considered. Only one temp variable needed
    """
    clean_pass = 0
    while clean_pass == 0:
        clean_pass = 1
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                clean_pass = 0
    return array


def counting_sort(array, position, k):
    """
    T = O(n+k).

    S = O(n+k). Input space not considered. One freq. array of k size and
    one sorted array of n size
    """
    # Assert base 10 or greater
    # Create freq. count array
    freq = np.zeros((k), dtype=np.int32)

    # Create freq of each based element
    for element in array:
        element_str = str(element)[::-1]
        if len(element_str) > position:
            freq[int(element_str[position])] += 1
        else:
            freq[0] += 1

    # Create cumulative freq of each based element
    for index, _ in enumerate(freq[:-1]):
        freq[index + 1] += freq[index]

    # Create array to write sorted values to
    sorted_array = np.zeros(len(array), dtype=np.int64)

    # Assign each element to it place according to its cumulative freq.
    for element in reversed(array):
        # subtract 1 because indexing starts from zero.
        element_str = str(element)[::-1]
        if len(element_str) > position:
            index = int(element_str[position])
        else:
            index = 0
        sorted_array[freq[index] - 1] = element
        freq[index] -= 1
    return sorted_array


def quick_sort(array):
    """
    T = O(nlogn) best and O(n^2) as worst. Worst happens when actual
    position of pivot is at starting/ending of array. Hence next sort
    is of size n-1, then n-2 etc. Best happens when actual position
    of pivot is in the middle of array. Hence, next sort is of size
    n/2, then n/4 and so on.
    """

    def identifySplit_movePivot(array, pivot_index):
        i = -1
        j = 0
        while j < len(array):
            if array[j] < array[pivot_index]:
                i += 1
                array[j], array[i] = array[i], array[j]
            j += 1
        array[pivot_index], array[i + 1] = array[i + 1], array[pivot_index]

        return array, i + 1

    if len(array) < 2:
        return array

    # find split position and move pivot element to its sorted position
    array, pivot_index = identifySplit_movePivot(array, len(array) - 1)
    # quick sort on 0:split-1 (inclusive)
    array[0:pivot_index] = quick_sort(array[0:pivot_index])
    # quick sort on split+1:len(array) (inclusive)
    array[pivot_index + 1 : len(array)] = quick_sort(
        array[pivot_index + 1 : len(array)]
    )

    return array


def merge_sort(array):
    """
    T = O(nlogn). At every level, it takes n total steps to sort l arrays of size
    n/l. There are a total of logn levels

    S = O(n). At every level, you need to create a new array to merge the 2
    sub-arrays. Once merged, the sub-arrays are destroyed. You create l temporary
    arrays, each of size n/l at level l. All levels below it are destroyed.
    Hence, you only use additional space of O(n).
    """

    # Return as-is if len is 1
    if len(array) == 1:
        return array

    # Split array into left and right down the middle
    middle = len(array) // 2
    left_array = merge_sort(array[:middle])
    right_array = merge_sort(array[middle:])

    # Create an empty list to merge left, right arrays
    merged_array = []
    l_index = r_index = 0

    # Merge element by element until one array all merged in
    while l_index < len(left_array) and r_index < len(right_array):
        left_element = left_array[l_index]
        right_element = right_array[r_index]
        if left_element < right_element:
            merged_array.append(left_element)
            l_index += 1
        else:
            merged_array.append(right_element)
            r_index += 1

    # Merge elements of remaining array
    if l_index < len(left_array):
        for element in left_array[l_index:]:
            merged_array.append(element)

    if r_index < len(right_array):
        for element in right_array[r_index:]:
            merged_array.append(element)

    return np.array(merged_array)


def radix_sort(array):
    """
    T = O(Dn), where D is the maximum number of digits in base 10 represetantion.
    For each digit place, it takes O(n+10)=O(n) steps to sort. We sort for D digit
    places, thus equalling O(Dn).

    S = O(n). For each digit place, we use O(N+10) = O(n) space. The returned array
    is itself used as input for the next digit place sort. Hence, using O(n) space.
    """
    base = 1
    index = 0
    while sum(x // base == 0 for x in array) != len(array):
        array = counting_sort(array, index, 10)
        base *= 10
        index += 1
    return array