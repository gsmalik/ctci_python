import igraph
import numpy as np

def findMaxDependency(nodes):
    maxDependency = -1
    for node in nodes:
        if len(node.connected_nodes) > maxDependency:
            startNode = node
            maxDependency = len(node.connected_nodes)
    return startNode

class Node():
    def __init__(self, value):
        self.value = value
        self.connected_nodes = []
        self.visited = False
        self.done = False

    def addNode(self, vertex):
        self.connected_nodes.append(vertex)
    
    def printConnectedNodes(self):
        for node in self.connected_nodes:
            print(node.value)


def createGraph(adjMatrix, num_vertices):
    nodes = []
    for vertex in range(num_vertices):
        nodes.append(Node(vertex))

    for row in range(num_vertices):
        for column in range(num_vertices):
            if adjMatrix[row][column] == 1:
                nodes[row].addNode(nodes[column])
    return nodes

def visitInOrder(node, nodes):
    if node.visited:
        assert False, "Unsolvable Dependencies"
    node.visited = True
    for connection in node.connected_nodes:
        if not connection.done:
            nodes = visitInOrder(connection, nodes)
    print("Finishing", node.value)
    node.done = True
    nodes = removeNode(node, nodes)
    return nodes
    
def removeNode(remove_node, nodes):
    newList = []
    for node in nodes:
        if not node == remove_node:
            newList.append(node)
    return newList

num_vertices = 3
labels = []
for index in range(num_vertices):
    labels.append(str(index))

adj_matrix = np.random.randint(0,2,(num_vertices,num_vertices))
np.fill_diagonal(adj_matrix, 0)

nodes = createGraph(adj_matrix, num_vertices)
while nodes:
    startNode = findMaxDependency(nodes)
    nodes = visitInOrder(startNode, nodes)

g = igraph.Graph.Adjacency((adj_matrix > 0).tolist())
g.vs['label'] = labels
igraph.plot(g, labels=True)





