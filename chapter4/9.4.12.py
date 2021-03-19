from binarytree import tree, bst


def depth_first_traversal(node, sums, hashtable):
    """Just your everyday DFT"""
    sums = [x + node.val for x in sums]
    sums.append(node.val)
    hashtable = update_hashtable(sums, hashtable)
    if node.left:
        hashtable = depth_first_traversal(node.left, sums, hashtable)
    if node.right:
        hashtable = depth_first_traversal(node.right, sums, hashtable)
    return hashtable


def update_hashtable(sums, hashtable):
    """
    Updates hashtable. if key exists, increments value else creates key.
    """
    for val in sums:
        if val in hashtable:
            hashtable[val] += 1
        else:
            hashtable[val] = 1
    return hashtable


def count_sum_paths(root_node):
    """
    Function to create a hashtable where a keys in the hashtable are unique sum values
    found in the tree and corresponding values are the count of number of times that
    sum can be uniquely created.

    Parameters
    ----------
    root_node: `Node`
        Root node of tree.

    Returns
    -------
    A hash table comprising of unique key(sums)-value(counts) pairs.

    Time Complexity
    ---------------
    O(N), where N is number of nodes in the tree. We use DFT here.

    Space Complexity
    ----------------
    If we count hashtable in space complexity, we can sum((N/2^k)*(log(N) - (k-1)),
    where k goes from 1 to log(N) and N is number of nodes. If we assume hastable as
    part of output, then space complexity is maximum depth of recursion DFT stack,
    which is log(N).
    """
    return depth_first_traversal(root_node, [], {})


test = tree(3)
print(test)
print(count_sum_paths(test.levels[0][0]))
