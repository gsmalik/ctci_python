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


def heap_sort(array):
    """
    T = O(nlogn) = O(log(n!)). Creating the first heap of entire array takes O(n)
    time (weird derivation. See https://www.youtube.com/watch?v=k72DtCnY4MU). Then
    each time you have to heapify the top element (after swap), that will take log(n-1)
    for first, then log(n-2) for second and so on. Adding all this, it becomes O(log(n!))
    which can be written as O(nlogn) loosely. Not super sure why everyone says time
    complexity is nlogn whereas it should be log(n!).

    S = O(1). Just using a temp variable to do swaps. Everything is in-place.
    """

    def heapify_complete_array(array):
        # Hepaify upper half of elements of array. Upper half enough because
        # we will swap with children (2*index+1, 2*index+2) inside this, which
        # lie in lower half.
        for index in range(len(array) // 2, -1, -1):
            array = heapify(array, index)
        return array

    def heapify(array, node_index):

        orig_index = node_index
        left_child_index = 2 * node_index + 1
        right_child_index = 2 * node_index + 2

        # Decide which node to swap with. Will swap with bigger child, if exists.
        if (
            left_child_index < len(array)
            and array[left_child_index] > array[node_index]
        ):
            node_index = left_child_index

        if (
            right_child_index < len(array)
            and array[right_child_index] > array[node_index]
        ):
            node_index = right_child_index

        # Do the swap. Heapify the current element. Note the current element is the
        # orgiginal element. It has just been moved and we are calling heapify on its
        # latest position
        if node_index != orig_index:
            array[orig_index], array[node_index] = array[node_index], array[orig_index]
            array = heapify(array, node_index)
        return array

    len_array = len(array)

    # Heapigy entire array once
    array = heapify_complete_array(array)
    for index in range(len_array - 1, -1, -1):
        # Swap first (max) and last element (of array size index+1).
        array[0], array[index] = array[index], array[0]

        # Heapify remaining array to find next max element
        array[:index] = heapify(array[:index], 0)

    return array


def insertion_sort(array):
    """
    T = O(n^2). If we have a descending array, then element at index 1
    will be swapped with 0. Then index at 2 will swap with 1 and then 0.
    Index 3 with 2,1 and 0 and so on. So, worst case, it can take n^2
    swaps.

    S = O(1). Only a temp variable used for swaps.
    """
    for index in range(len(array) - 1):
        if array[index] > array[index + 1]:
            # move index + 1 to proper index
            pin_index = index + 1
            while pin_index > 0 and array[pin_index] < array[pin_index - 1]:
                array[pin_index], array[pin_index - 1] = (
                    array[pin_index - 1],
                    array[pin_index],
                )
                pin_index -= 1
    return array


def bucket_sort(array, num_buckets, low, high):
    """
    T = O(n) in best. O(k*sorting_elements(n/k)) in average case.
    O(sorting algorithm) in worst case. It takes n steps to assign each
    element to bucket. In average case, since elements are uniformly
    distributed, each bucket should have n/k elements. Hence it should
    take O(k*sorting_elements(n/k)) time on average. In best case,
    each bucket will only have one element, thus no sorting required,
    leading to O(n) best case time.

    S = At one time, you will only be sorting one bucket and then just
    storing the final sorted bucket. Sorted buckets total will have a
    total of n elements obviosuly so we need O(n) space to store sorted
    buckets. Coming back to sorting a bucket, once a bucket is sorted
    we can destroy the intermediate space. So, in worst case, all elements
    can belong to same bucket. Thus space complexity will be
    O(n)+space_complexity(sorting_algorithm(n)). In average case, each bucket
    will have n/k elements and we will only sort one bucket at a time. Thus
    space complexity will be O(n)+space_complexity(sorting_algorithm(n/k)). In
    best case, there will be 1 element in each case, thus requiring no sorting
    and consuming only O(n) space.
    """
    # Create number of buckets
    bucket = []
    for _ in range(num_buckets):
        bucket.append([])

    # Nomalize value and assign it to a bucket
    for value in array:
        assert ((value - low) / (high - low)) * num_buckets >= 0
        bucket[int(((value - low) / (high - low)) * num_buckets)].append(value)

    # Sort each bucket individually using merge sort
    for index, value in enumerate(bucket):
        bucket[index] = merge_sort(value)

    # Return sorted buckets
    return np.array([item for sublist in bucket for item in sublist])


test = np.random.randint(50, 100, (10))
print(bucket_sort(test, 5, 50, 100))
