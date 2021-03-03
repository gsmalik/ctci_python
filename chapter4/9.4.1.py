import numpy as np
# You need to install ``python-igraph`` and ``cairocffi``
import igraph
import string
import graphs

def find_route(node_1, node_2):
    """
    Function to find wether there is a route between given nodes.

    Parameters
    ----------
    node_1: ``Node``
        One of the two nodes to find route between.

    node_2: ``Node``
        Second of the two nodes to find route between.


    Time Complexity
    ---------------
    O(N), where N is the number of vertices in graph.

    Space Complexity
    ---------------
    O(N), where N is the number of vertices in graph.
    """
    print("Checking for path from node_1 to node_2")
    graphs.bfs(node_1, node_2)
    print("Checking for path from node_2 to node_1")
    graphs.bfs(node_2, node_1)

num_vertices = 7
src_node = 0
target_node = 4

# Used for visualizing the graph
labels = []
for index in range(num_vertices):
    labels.append(str(index))

# Create a random adjacency matrix for graph connectivity.
adj_matrix = np.random.randint(0,2,(num_vertices,num_vertices))
# Just keeping things a bit more interesting by preventing direct edges.
adj_matrix[src_node][target_node] = 0
print(adj_matrix)

# Create graph using ``adj_matrix`` and return a list
# of nodes in the graph for easy access to each node.
nodes = graphs.create_graph(adj_matrix, num_vertices)

# Find route between the nodes
find_route(nodes[src_node], nodes[target_node])
# Visualize graph for confirmation.
g = igraph.Graph.Adjacency((adj_matrix > 0).tolist())
g.vs['label'] = labels

igraph.plot(g, labels=True)