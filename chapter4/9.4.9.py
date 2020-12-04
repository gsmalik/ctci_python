from binarytree import tree, bst


def appendChildren(node, levelWiseList):
    if node.left:
        levelWiseList.append(node.left)
    if node.right:
        levelWiseList.append(node.right)
    # print("[appendChildren] Updated list:", levelWiseList)
    return levelWiseList


def listLevelWiseNodes(rootNode):
    levelWiseList = [[rootNode]]
    print(levelWiseList)
    index = 0
    while levelWiseList[index]:
        levelWiseList.append([])
        for node in levelWiseList[index]:
            # print("[listLevelWiseNodes] Current node:", node)
            levelWiseList[index + 1] = appendChildren(node, levelWiseList[index + 1])
        index += 1

    return levelWiseList


my_tree = bst(height=5)
print(my_tree)
print(listLevelWiseNodes(my_tree.levels[0][0]))
