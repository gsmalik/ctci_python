from binarytree import tree, bst


def depth_first_search(node, sums, hashtable):
    sums = [x + node.val for x in sums]
    sums.append(node.val)
    hashtable = update_hashtable(sums, hashtable)
    if node.left:
        hashtable = depth_first_search(node.left, sums, hashtable)
    if node.right:
        hashtable = depth_first_search(node.right, sums, hashtable)
    return hashtable


def update_hashtable(sums, hashtable):
    for val in sums:
        if val in hashtable:
            hashtable[val] += 1
        else:
            hashtable[val] = 1
    return hashtable


def count_sum_paths(rootNode):
    return depth_first_search(rootNode, [], {})


test = tree(3)
print(test)
print(count_sum_paths(test.levels[0][0]))
