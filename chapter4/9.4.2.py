class Node():
    def __init__(self, array):
        middle = int(len(array)/2)
        self.value = array[middle]
        print(self.value)
        if len(array) > 1:
            self.left = Node(array[:middle])
        if len(array) > 2:
            self.right = Node(array[middle+1:])


Node([1,2,3,4,5,6,7,8])