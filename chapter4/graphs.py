class Heap:
    def __init__(self, style):
        assert style in ["min", "max"]
        self.style = style
        self.array = []

    def insert(self, value):
        def __swap_elements(node_index):
            parent_index = (node_index - (1 if node_index % 2 else 2)) // 2
            swap = (
                (
                    self.style == "max"
                    and self.array[parent_index] < self.array[node_index]
                )
                or (
                    self.style == "min"
                    and self.array[parent_index] > self.array[node_index]
                )
            ) and node_index > 0
            if swap:
                self.array[parent_index], self.array[node_index] = (
                    self.array[node_index],
                    self.array[parent_index],
                )
            return [swap, parent_index]

        self.array.append(value)
        current_index = len(self.array) - 1
        while (returned := __swap_elements(current_index))[0]:
            current_index = returned[1]
        print(f"Heap afer inserting {value} is {self.array}")

    def peak(self):
        return self.array[0]

    def remove_top(self):
        def __bubble_down(parent_index):
            if 2 * parent_index + 1 >= len(self.array):
                return [False, parent_index]
            compare_index = (
                2 * parent_index + 1
                if (
                    len(self.array) == 2 * parent_index + 2
                    or (
                        self.array[2 * parent_index + 1]
                        > self.array[2 * parent_index + 2]
                        and self.style == "max"
                    )
                    or (
                        self.array[2 * parent_index + 1]
                        < self.array[2 * parent_index + 2]
                        and self.style == "min"
                    )
                )
                else 2 * parent_index + 2
            )
            swap = (
                (
                    self.style == "max"
                    and self.array[parent_index] < self.array[compare_index]
                )
                or (
                    self.style == "min"
                    and self.array[parent_index] > self.array[compare_index]
                )
                and compare_index < len(self.array)
            )
            if swap:
                self.array[parent_index], self.array[compare_index] = (
                    self.array[compare_index],
                    self.array[parent_index],
                )
            return [swap, compare_index]

        val_return = self.array[0]
        self.array[0] = self.array.pop()
        current_index = 0
        while (returned := __bubble_down(current_index))[0]:
            current_index = returned[1]
        print(f"Heap afer popping {val_return} is {self.array}")


def bfs(start_node, target_node):
    bfs_queue = []
    bfs_queue.append(start_node)

    while bfs_queue:
        current_node = bfs_queue.pop(0)
        print("Visited", current_node.value)
        current_node.visited = True
        for neighbour in current_node.connected_nodes:
            if neighbour == target_node:
                print(f"Found {target_node}")
                return
            if not neighbour.visited:
                bfs_queue.append(neighbour)


def dfs(node):
    print(f"Visited {node.value}")
    node.visited = True
    for neighbour in node.connected_nodes:
        if not neighbour.visited:
            dfs(neighbour)

class Node():
    def __init__(self, value):
        self.value = value
        self.connected_nodes = []
        self.visited = False

    def addNode(self, vertex):
        self.connected_nodes.append(vertex)
    
    def printConnectedNodes(self):
        for node in self.connected_nodes:
            print(node.value)

def create_graph(adj_matrix, num_vertices):
    nodes = []
    for vertex in range(num_vertices):
        nodes.append(Node(vertex))

    for row in range(num_vertices):
        for column in range(num_vertices):
            if adj_matrix[row][column] == 1:
                nodes[row].addNode(nodes[column])
    return nodes
