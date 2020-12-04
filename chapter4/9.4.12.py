from binarytree import tree, bst

def DFS(node, sums, hashTable):
    sums = [x + node.val for x in sums]
    sums.append(node.val)
    hashTable = updateHashTable(sums, hashTable)
    if node.left:
        hashTable = DFS(node.left, sums, hashTable)
    if node.right:
        hashTable = DFS(node.right, sums, hashTable)
    return hashTable

def updateHashTable(sums, hashTable):
    for val in sums:
        if val in hashTable:
            hashTable[val] += 1
        else:
            hashTable[val] = 1
    return hashTable


def listSumPaths(rootNode):
    return (DFS(rootNode, [], {}))


test = tree(3)
print(test)
print(listSumPaths(test.levels[0][0]))
