def find_string(array, string, left, right):
    """
    Function to search for a string in a sorted list of strings, interspersed with
    empty strings

    Parameters
    ----------
    array: list
        List of strings.
    string: str
        String that we are searching for.
    left: int
        Left index of sub array to be searched.
    right: int
        Right index of sub array to be searched.

    Time Complexity
    ---------------
    O(N) worst case because we have to traverse array to find non empty strings when
    binary search leads results in probing an empty string. This is still better than
    linear traversing on average, since binary search can cut down non empty string
    probes to logN.

    Space Complexity
    ----------------
    O(logN) worst case when every time we hit a non empty string doing binary search and
    hence have a recursive depth of logN.
    """
    # find mid point
    mid = (left + right) // 2

    # if only element left to be searched
    if left == right and array[left] != string:
        return False

    # if mid point is empty string
    if array[mid] == "":

        mid_left = mid_right = mid
        # search for first non empty string going left
        while mid_left >= left and array[mid_left] == "":
            mid_left -= 1
        # search for first non empty string going right
        while mid_right <= right and array[mid_right] == "":
            mid_right += 1

        # if search exhausted, return false
        if mid_left < left and mid_right > right:
            return False

        # if left is non empty and right was exhausted, choose left
        if array[mid_left] != "" and mid_right > right:
            mid = mid_left
        # if right is non empty and left was exhausted, choose right
        elif array[mid_right] != "" and mid_left < left:
            mid = mid_right
        # if both become non empty, choose nearest one to mid
        else:
            mid = mid_left if abs(mid - mid_left) < abs(mid - mid_right) else mid_right

    if array[mid] == string:
        return mid
    # recurse into the right direction
    if array[mid] > string:
        return find_string(array, string, left, mid)
    else:
        return find_string(array, string, mid, right)


test = ["a", "b", "", "", "", "c", "d", "", "", "", "f"]
print(find_string(test, "f", 0, len(test) - 1))
