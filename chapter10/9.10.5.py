def find_string(array, string, left, right):
    # Return if left most element matches
    if array[left] == string:
        return left
    # Return if right most element matches
    if array[right] == string:
        return right
    # Return if length is 1 since no match
    if left == right:
        return False

    # Calculate mid point
    mid = left + (right - left) // 2

    # Return if mid point matches
    if array[mid] == string:
        return mid

    # If mid point is empty string
    if array[mid] == "":

        # Keep searching for left/right most non empty string
        mid_right = mid + 1
        mid_left = mid - 1
        while mid_left > 0 and array[mid_left] == "":
            mid_left -= 1
        while mid_right < len(array) - 1 and array[mid_right] == "":
            mid_right += 1

        # Update mid point if string lies left or right
        if array[mid_left] != "" and array[mid_left] >= string:
            mid = mid_left
        elif array[mid_right] != "" and array[mid_right] <= string:
            mid = mid_right
        # There will be no match. Return false
        else:
            return False

    # Recurse into appropriate direction
    if array[mid] >= string:
        return find_string(array, string, left, mid)
    else:
        return find_string(array, string, mid, right)


test = ["a", "b", "", "", "", "c", "d", "", "", "", "f"]
print(find_string(test, "f", 0, len(test) - 1))
