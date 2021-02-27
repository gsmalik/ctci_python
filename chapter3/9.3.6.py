class AnimalShelter():
    """
    A class that implements an animal shelter queues dogs/cats in separate queues.

    Space Complexity
    ----------------
    O(N), where N is the number of total animals in the shelter. If we consider the queue
    space as given, then we can interpret space complexity as O(1) since we do not use
    any other space that is related to current number of animals in the shelter.
    """

    def __init__(self):
        # Queue for dogs
        self.dog_queue = []
        # Queue for cat
        self.cat_queue = []
        # Maintain time. Gets increment everytime a new animal is queued.
        self.time = 0
    
    def enqueue(self, type):
        """
        Function to enqueue an animal.

        Parameters
        ----------
        type: ``str``
            Type of animal. Limited to "cat" and "dog"

        Time Complexity
        ---------------
        O(1)
        """
        assert type in ["cat", "dog"]

        if type == "cat":
            self.cat_queue.append(self.time)
        else:
            self.dog_queue.append(self.time)
        self.time += 1

    def dequeue_dog(self):
        """
        Function to dequeue a dog.

        Time Complexity
        ---------------
        O(1)
        """
        if self.dog_queue:
            print(f"Returning Dog {self.dog_queue[0]}")
            return self.dog_queue.pop(0)
        print("No dogs in shelter")
    
    def dequeue_cat(self):
        """
        Function to dequeue a cat.

        Time Complexity
        ---------------
        O(1)
        """
        if self.cat_queue:
            print(f"Returning Cat {self.cat_queue[0]}")
            return self.cat_queue.pop(0)
        print("No cats in shelter")
    
    def dequeue_any(self):
        """
        Function to dequeue animal with longest stay in shelter currently.

        Time Complexity
        ---------------
        O(1)
        """

        if self.cat_queue or self.dog_queue:
            if not self.cat_queue:
                return self.dequeue_dog()
            if not self.dog_queue:
                return self.dequeue_cat()
            return self.dequeue_dog() if self.cat_queue[0] > self.dog_queue[0] else self.dequeue_cat()

        print("No Animals in shelter")


test = AnimalShelter()
test.enqueue("dog")
test.dequeue_any()
test.dequeue_any()
test.enqueue("cat")
test.dequeue_any()