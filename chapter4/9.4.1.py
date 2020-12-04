import numpy as np
import igraph
import string

class node():
    def __init__(self, value):
        self.value = value
        self.connected_nodes = []
        self.visited = False

    def addNode(self, vertex):
        self.connected_nodes.append(vertex)
    
    def printConnectedNodes(self):
        for node in self.connected_nodes:
            print(node.value)

class binaryNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.visited = False

    def addNodeLeft(self, vertex):
        self.left = vertex

    def addNodeRight(self, vertex):
        self.right = vertex

    def printConnectedNodes(self):
        print(self.left, self.right)

def createGraph(adjMatrix, num_vertices):
    nodes = []
    for vertex in range(num_vertices):
        nodes.append(node(vertex))

    for row in range(num_vertices):
        for column in range(num_vertices):
            if adjMatrix[row][column] == 1:
                nodes[row].addNode(nodes[column])
    return nodes

def createBinarySearchTree(array):
    nodes = []
    for element in array:
        nodes.append(binaryNode(element))
    

    bstQueue = []
    bstQueue.append(nodes[0])

    while bstQueue:
        currentNode = 

def breadthFirstSearch(rootNode):
    bfsQueue = []
    bfsQueue.append(rootNode)

    while bfsQueue:

        currentNode = bfsQueue.pop(0)
        print("Visited", currentNode.value)
        currentNode.visited = True
        for neighbour in currentNode.connected_nodes:
            if not neighbour.visited:
                bfsQueue.append(neighbour)



num_vertices = 7
labels = []
for index in range(num_vertices):
    labels.append(str(index))

adj_matrix = np.random.randint(0,2,(num_vertices,num_vertices))

print(adj_matrix)

nodes = createGraph(adj_matrix, num_vertices)
breadthFirstSearch(nodes[0])
g = igraph.Graph.Adjacency((adj_matrix > 0).tolist())
g.vs['label'] = labels

igraph.plot(g, labels=True)