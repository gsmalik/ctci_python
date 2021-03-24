import numpy as np


def draw_line(byte_array, width, x1, x2, y):
    print(f"Drawing line using pixel bits {byte_array[y*width+x1:y*width+x2+1]}")


width = 16
height = 8
test = np.random.randint(0, 2, (height * width))
print(test)
draw_line(test, width, 1, 8, 3)
