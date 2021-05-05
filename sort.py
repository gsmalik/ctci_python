import numpy as np


def bubble_sort(array):
    """
    Function to sort an array using bubble sort.

    Parameters
    ----------
    array: list/np.1darray
        Array that needs to be sorted

    Returns
    -------
        Sorted array.

    Time Complexity
    ---------------
    O(N^2), where N is the number of elements in the array.

    Space Complexity
    ----------------
    O(1). Input space not considered.
    """
    # set a variable to track if latest iteration through array resulted in swaps
    clean_pass = False
    while not clean_pass:
        # set clean_pass to True for this iteration
        clean_pass = True
        # iterate through array
        for i in range(len(array) - 1):
            # swap if needed and update clean_pass
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
                clean_pass = False
    return array


def counting_sort(array, radix_position):
    """
    Function to sort an array using counting sort.

    Parameters
    ----------
    array: list/np.1darray
        Array that needs to be sorted.
    radix_position: int
        Radix position that needs to be used for sorting. For example, in an array of
        [123,456,121,004], a radix_position of 1 means [2,5,2,0] would be used to sort
        the array.

    Time Complexity
    ---------------
    O(N). You go through the array linearly thrice. Once for creating frequency array,
    second for accumulating frequency and finally for sorting.

    Space Complexity
    ----------------
    O(N). The frequency array is constant space and you use a new array of same size as
    original array for creating the sorted array.
    """
    # Create freq. count array of len 11
    # 11 because 10 (0-9) + 1 (if length of number is less than radix position)
    freq = np.zeros((11), dtype=np.int32)

    # Create freq of each based element
    for element in array:
        # create string representation of array and reverse it because originally
        # 0th radix bit lies at end etc
        element_str = str(element)[::-1]
        # if the length of integer is smaller than the radix position, it would be
        # the smallest and needs to come first. hence we keep it at 0. hence,
        # frequency of '0' will be at index 1, frequency of '1' will be at index
        # 2 and so on.
        if len(element_str) > radix_position:
            freq[int(element_str[radix_position])+1] += 1
        else:
            freq[0] += 1

    # create cumulative freq of each based element
    for index, _ in enumerate(freq[:-1]):
        freq[index + 1] += freq[index]

    # create array to write sorted values to
    sorted_array = np.zeros(len(array), dtype=np.int64)

    # assign each element to it place according to its cumulative freq.
    # you go in reverse because if using radix sort, then positions smaller than
    # radix_position have already been sorted so the larger of the numbers on the
    # already sorted radix positions need to be assigned the higher cumulative
    # frequency index.
    for element in reversed(array):
        element_str = str(element)[::-1]
        if len(element_str) > radix_position:
            index = int(element_str[radix_position]) + 1
        else:
            index = 0
        # subtract 1 because indexing starts from zero.
        sorted_array[freq[index] - 1] = element
        freq[index] -= 1
    return sorted_array

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
        array = counting_sort(array, index)
        print(array)
        base *= 10
        index += 1
    return array

def quick_sort(array):
    """
    Time Complexity
    ---------------
    O(NlogN) best and O(N^2) as worst, where N is the number of elements in the
    array. Worst happens when actual position of pivot is at starting/ending of array.
    Hence next sort is of size N-1, then N-2 etc. Best happens when actual position of
    pivot is in the middle of array. Hence, next sort is of size N/2, then N/4 and so
    on.

    Space Complexity
    ----------------
    O(N) in worst case and O(logN) in best case, where N is the number of elements
    in the array. Remember that each recursive call adds 1 pointer to the stack. In
    worst case, we would end up making n recursive calls, with each call using up O(1)
    space, which gets destroyed after that call is finished. Hence, at the last
    recursive call, we would have n calls on the stack and 1 temp variable to swap.
    Thus, in worst case, we would consume O(N) space. In best case, we would have
    O(logN) calls, thus consuming O(logN) space.
    """

    def sort_update_pivot_index(array, pivot_index):
        """
        A function to sort the array and move the pivot element such that elements less
        than pivot element are left of the new pivot index and elements greater than the
        pivot element are right of the new pivot index.

        Note that the array is not necessarily sorted. Just that the pivot is moved to an index
        such that elements smaller to the left of it and bigger to the right of it.
        """
        # i will become the new pivot element
        i = -1
        # iterate through array
        for j in range(len(array)):
            # if current element is less than our original pivot index, then it should
            # stay to the left of the final pivot index (i). Note that the pivot element
            # is still going to be the same, just that we are changing the index.
            if array[j] < array[pivot_index]:
                i += 1
                array[j], array[i] = array[i], array[j]
        array[pivot_index], array[i + 1] = array[i + 1], array[pivot_index]

        return array, i + 1

    if len(array) < 2:
        return array

    # sort array around pivot and update pivot index. now we have an array where
    # elements less than array[pivot_index] are to the left of pivot_index and
    # elements greater than array[pivot_index] are to the right of pivot_index
    array, pivot_index = sort_update_pivot_index(array, len(array) - 1)

    # quick sort on left side
    array[0:pivot_index] = quick_sort(array[0:pivot_index])
    # quick sort on right
    array[pivot_index + 1 :] = quick_sort(array[pivot_index + 1 :])

    return array


def merge_sort(array):
    """
    Time Complexity
    ---------------
    O(NlogN), where N is the number of elements in the array. At every level, it takes
    n total steps to sort l arrays of size n/l. There are a total of logN levels.

    Space Complexity
    ----------------
    O(N), where N is the number of elements in the array. At every level, you will have
    2 new sorted sub-arrays that can be merged using original array. Once merged, the
    sub-arrays are destroyed. When merging 2 sub-arrays at level l, you will have 2
    sub arrays, with each being of size N/2^(l+1), hence consuming an extra space of
    size N/2^l. At level 0, this means you will have 2 sub arrays of size N. Also, dont
    forget to think about your stack depth, although you will see that it is smaller
    than n. In merge sort, you will have a max recursive stack depth of O(logN) at
    level logN. But at this stage, your sub array sizes will be 0 since this is last
    level. At level log(N)-1, your sub array sizes will be 2 and recursive depth of
    log(N)-1. Thus, at level 0, your temp array will be of size N and recursive depth
    of 0. Thus, overall space complexity is O(N).
    """

    # Return as-is if len is 1
    if len(array) == 1:
        return array

    # Split array into left and right down the middle
    middle = len(array) // 2
    left_array = merge_sort(array[:middle])
    right_array = merge_sort(array[middle:])

    l_index = r_index = 0

    # Merge element by element until one array all merged in
    while l_index < len(left_array) and r_index < len(right_array):
        left_element = left_array[l_index]
        right_element = right_array[r_index]
        if left_element < right_element:
            array[l_index + r_index] = left_element
            l_index += 1
        else:
            array[l_index + r_index] = right_element
            r_index += 1

    # merge rest of elements
    array[l_index + r_index :] = (
        left_array[l_index:] if l_index < len(left_array) else right_array[r_index:]
    )

    return array


def heap_sort(array):
    """
    Time Complexity
    ---------------
    O(NlogN). Creating the first heap of entire array takes O(N) time (see your notes
    about heaps about why N). Then, you will basically pop the first element as your
    minimum and put the last element in its place. Then pop that and put the next last
    element in its place and so on.

    Notice that when you are popping and putting the last element at top, this element
    might need to bubble down. Worst case it bubbles down to last level. Remember that
    the last N/2 elements of the array will all lie in the same level: log(N). Hence,
    for the first N/2 such moves, each of these 'last' elements might move to the last
    level, which will still be log(N). So, it will take N/2*log(N) time to move down
    the last N/2 elements. Then the next N/4 elements (level above) will take log(N)-1
    time, then N/8 elements will take log(N)-2 time and so on. Hence overall time can
    become N/2*log(N) + N/4*(log(N) - 1) + N/8*(log(N) - 2) + ...This reduces roughly
    to O(NlogN). The derivation is a bit complex but you can see it in your notes.

    Space Complexity
    ----------------
    S = O(1). Just using a temp variable to do swaps. Everything is in-place.
    """

    def create_max_heap(array):
        """
        Function to convert array into a max heap.

        Parameters
        ----------
        array: list/np.1darray
            Array that needs to be converted to a max heap.

        Time Complexity
        ---------------
        O(N), as explained above.

        Space Complexity
        ----------------
        O(1).
        """
        for i in range(len(array) // 2, -1, -1):
            array = max_heapify(i, array)
        return array

    def max_heapify(parent_index, array):
        """
        Function to make sure a particular element of the array satisfies the property
        of a max heap.

        Parameters
        ----------
        parent_index: int
            Index of element in the array that needs to be checked for max heap
            compliance.
        array: list/np.1darray
            Array to which the element of intereset belongs.

        Time Complexity
        ---------------
        O(logN), where N is the number of elements in the array. In worst case, you
        might have the smallest number at the top of the max heap, which will need to
        bubbled down, which can take logN steps. Remember that in the context of heap
        sort, the length of array keeps decreasing by 1 every time you do a swap. But
        whatever the current length is (denoted as N in this context), it can take at
        worst logN steps.

        Space Complexity
        ----------------
        O(1).
        """
        # return without doing anything if array is empty
        if len(array) == 0:
            return array
        while True:
            # calculate indices of potential children
            child1_index = 2 * parent_index + 1
            child2_index = 2 * parent_index + 2

            # check if children exist
            child1_exists = child1_index <= len(array) - 1
            child2_exists = child2_index <= len(array) - 1

            # determine index with which parent index will be swapped.
            new_index = parent_index
            if child1_exists:
                new_index = (
                    child1_index
                    if array[new_index] < array[child1_index]
                    else new_index
                )

            if child2_exists:
                new_index = (
                    child2_index
                    if array[new_index] < array[child2_index]
                    else new_index
                )

            # do the swap
            array[parent_index], array[new_index] = (
                array[new_index],
                array[parent_index],
            )

            # if no swap happended, as captured by the condition, we can exit
            if new_index == parent_index:
                break
            # if swap happened and parent was bubbled down, then we need to make
            # sure that max heap is compliance is met between bubbled down parent
            # and new children. hence, continue with looping.
            else:
                parent_index = new_index

        return array

    # create a max heap out of array
    array = create_max_heap(array)

    # swap first element (largest) with last (smallest) and bubble down smallest
    # from top to its correct position. do not take the swapped largest elements,
    # into account when max_heapifying since they are already at their correct
    # postion. The first time, you have the largest element at the top which you
    # send to last, second time you have the second largest element at top which
    # you send to second last and so on. hence they are already at their correct
    # positions and don't need to be taken into account when max heapifying.
    for index in range(len(array) - 1, 0, -1):
        # swap root and last element
        array[0], array[index] = array[index], array[0]

        # max heapify rest of array
        array[:index] = max_heapify(0, array[:index])

    return array


def insertion_sort(array):
    """
    Time Complexity
    ---------------
    O(N^2), where N is the number of elements in the array. If we have a descending
    array, then element at index 1 will be swapped with 0. Then index at 2 will swap
    with 1 and then 0. Index 3 with 2,1 and 0 and so on. So, worst case, it can take
    N^2 swaps.

    Space Complexity
    ----------------
    O(1). Only a temp variable used for swaps.
    """
    # iterate through array, for each index we make sure that everything up to
    # index-1 is sorted.
    for index in range(len(array) - 1):
        # if index is not sorted, we start bubbling element at index down until
        # it is at the correct position. note that since all elements up till
        # index-1 are sorted, we are just inserting the element at 'index' in its
        # correct position. the relative position between the elements up till
        # 'index-1' is unchanged.
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


def bucket_sort(array, num_buckets):
    """
    Function to sort a given array using bucket sort.

    Parameters
    ----------
    array: list/np.1darray
        Array that needs to be sorted.

    num_buckets: int
        Num of buckets to use.

    Time Complexity
    ---------------
    O(N) in best. O( max(N,K*t_sorting_algorithm(N/K) )) in average case.
    O( t_sorting algorithm(N) ) in worst case. N is the number of elements in the array
    and K is the number of buckets. It takes N steps to assign each element to bucket.
    In average case, since elements are uniformly distributed, each bucket should have
    N/K elements. So, you will sort each bucket containing N/K elements. Hence it
    should take O(max(N, K*t_sorting_algorithm(N/K)) time on average. In best case,
    each bucket will only have one element, thus no sorting required, leading to O(N) best
    case time.

    Space Complexity
    ----------------
    At one time, you will only be sorting one bucket and then just storing the final
    sorted bucket. Sorted buckets total will have a total of N elements obviously so we
    need O(N) space to store sorted buckets. Coming back to sorting a bucket, once a
    bucket is sorted, we can destroy the intermediate space. So, in worst case, all
    elements can belong to same bucket. Thus space complexity will be
    O( max(N, s_sorting_algorithm(N)) ). In average case, each bucket will have N/K
    elements and we will only sort one bucket at a time. Thus space complexity will be
    O( max(M, s_sorting_algorithm(N/K)) ). In best case, there will be 1 element in
    each case, thus requiring no sorting and consuming only O(n) space.
    """
    low = min(array)
    high = max(array)

    assert high > low

    # Create number of buckets
    bucket = [[] for _ in range(num_buckets)]

    # Normalize value and assign it to a bucket
    for value in array:
        bucket_index = int(((value - low) / (high - low))) * (num_buckets - 1)
        bucket[bucket_index].append(value)

    # Sort each non empty bucket individually using merge sort
    bucket = [merge_sort(value) for value in bucket if value]

    # Return sorted buckets
    return [item for sublist in bucket for item in sublist]