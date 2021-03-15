class Heap:
    """
    A class that implements a heap using a complete binary tree.

    Parameters
    ----------
    style: ``str``
       Wether the heap has to act as a min` heap or a `max` heap.

    Space Complexity
    ----------------
    O(N), where N is the number of nodes in the heap.
    """

    def __init__(self, style):
        assert style in ["min", "max"]
        self.style = style
        self.array = []

    def insert(self, element):
        """
        Function to insert element in the heap

        Parameters
        ----------
        element: ``FP32``
            Element that needs to be inserted in the heap.

        Time Complexity
        ---------------
        O(log(N)), determined by the ``__bubble_up`` function.
        """

        def __bubble_up(node_index):
            """
            Function to bubble up elements to find correction of element in the
            heap

            Parameters
            ----------
            node_index: ``int``
                Index of element in the array which is used to represent the binary
                heap

            Time Complexity
            ---------------
            O(log(N)), where N is the number of nodes in the heap. You move up a level
            each time you bubble up. In worst case, the element could be the min/max
            and might need to be bubbled all the way to the top.
            """
            # Find out parent index of the node
            parent_index = (node_index - (1 if node_index % 2 else 2)) // 2
            # Determine if you need to swap. You do not need to compare the
            # element with its sibling, only its parent. This is because the heap
            # relationship is already satisfied between the parent and its
            # sibling.
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

            # Swap parent and node if needed.
            if swap:
                self.array[parent_index], self.array[node_index] = (
                    self.array[node_index],
                    self.array[parent_index],
                )
            # Return wether you swapped and the new index of the node, which is
            # parent index (only applicable when swap is True).
            return [swap, parent_index]

        # Add element to end of heap array.
        self.array.append(element)

        # Keep bubbling up element until necessary
        current_index = len(self.array) - 1
        while (returned := __bubble_up(current_index))[0]:
            current_index = returned[1]
        print(f"Heap after inserting {element} is {self.array}")

    def peak(self):
        """Returns value of element at top of heap."""
        return self.array[0]

    def remove_top(self):
        """
        Function to remove element in top of heap and rearrange heap

        Time Complexity
        ---------------
        O(log(N)), determined by the ``__bubble_down`` function.
        """

        def __bubble_down(parent_index):
            """
            Function to bubble down elements to find correction of element in the
            heap

            Parameters
            ----------
            parent_index: ``int``
                Index of element in the array which is used to represent the binary
                heap

            Time Complexity
            ---------------
            O(log(N)), where N is the number of nodes in the heap. You move down a
            level each time you bubble up. In worst case, the element could need to
            be bubbled all the way down.
            """
            # Assert that there is room to bubble down to
            if 2 * parent_index + 1 >= len(self.array):
                return [False, parent_index]

            # Determine which sibling we will compare with to decide wether to bubble
            # down or not.
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

            # Determine wether we need to swap or not.
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

            # Make the swap if needed
            if swap:
                self.array[parent_index], self.array[compare_index] = (
                    self.array[compare_index],
                    self.array[parent_index],
                )
            # Return information about wether we made the swap and what the new index
            # is (only applicable when swap is made).
            return [swap, compare_index]

        # Pop the element at the top
        val_return = self.array[0]

        # Make the last element in the heap as the top element in the heap
        self.array[0] = self.array.pop()

        # Keep bubbling down as needed
        current_index = 0
        while (returned := __bubble_down(current_index))[0]:
            current_index = returned[1]
        print(f"Heap after popping {val_return} is {self.array}")


def bfs(start_node, target_node):
    """
    Function to perform breadth first search over a graph

    Parameters
    ----------
    start_node: ``Node``
        The starting node from which BFS will be launched
    target_node: ``Node``
        The node being searched for

    Time Complexity
    ---------------
    O(N), where N is the number of nodes in the graph. In the worst case, the target
    node could be the last node found over bread first search.

    Space Complexity
    ---------------
    O(N), where N is the number of nodes in the graph. In the worst case, the target
    node could be the last node found over bread first search.
    """
    # Create a queue and add the starting node to it
    bfs_queue = []
    bfs_queue.append(start_node)

    while bfs_queue:
        # Pop from front of queue
        current_node = bfs_queue.pop(0)
        print("Visited", current_node.value)
        # Mark it as true to avoid deadlocks in cyclic graphs
        current_node.visited = True
        # Add all of its unvisited neighbors to queue
        for neighbor in current_node.connected_nodes:
            # Return if node found
            if neighbor == target_node:
                print(f"Found {target_node}")
                return
            if not neighbor.visited:
                bfs_queue.append(neighbor)


def dfs(start_node, target_node):
    """
    Function to perform depth first search over a graph

    Parameters
    ----------
    start_node: ``Node``
        The starting node from which BFS will be launched
    target_node: ``Node``
        The node being searched for

    Time Complexity
    ---------------
    O(N), where N is the number of nodes in the graph. In the worst case, the target
    node could be the last node found over depth first search.

    Space Complexity
    ---------------
    O(log(N)), where N is the number of nodes in the graph. In the worst case, the target
    node could be in last level of the tree.
    """
    print(f"Visited {start_node.value}")
    # Mark the starting node as visited
    start_node.visited = True
    # Traverse through neighbors of this node and perform DFS on each.
    for neighbor in start_node.connected_nodes:
        # Return if node found
        if neighbor == target_node:
            print(f"Found {target_node}")
            return
        if not neighbor.visited:
            dfs(neighbor, target_node)


class Node:
    def __init__(self, value):
        self.value = value
        self.connected_nodes = []
        self.visited = False

    def addNode(self, vertex):
        self.connected_nodes.append(vertex)

    def printConnectedNodes(self):
        for node in self.connected_nodes:
            print(node.value)


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def printConnectedNodes(self):
        print(f"Left: {self.left} with value {self.left.value}")
        print(f"Right: {self.right} with value {self.right.value}")


def create_bst(array, parent_node):
    root = Node(array[len(array) // 2])
    root.parent = parent_node
    root.left = create_bst(array[: len(array) // 2], root) if len(array) > 1 else None
    root.right = (
        create_bst(array[len(array) // 2 + 1 :], root) if len(array) > 2 else None
    )
    return root


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(
        f"Visited {node.value} with parent {node.parent.value if node.parent else 'no parent'}"
    )
    in_order(node.right)


def create_graph(adj_matrix, num_vertices):
    nodes = []
    for vertex in range(num_vertices):
        nodes.append(Node(vertex))

    for row in range(num_vertices):
        for column in range(num_vertices):
            if adj_matrix[row][column] == 1:
                nodes[row].addNode(nodes[column])
    return nodes
