import numpy as np

def print_duplicates(array):
    mem = np.zeros(32000)

    for num in array:
        if mem[num] == 1:
            print(num)
        else:
            mem[num] = 1

test = np.random.randint(0,32000, (np.random.randint(0,5000,(1))+32000))
print_duplicates(test)