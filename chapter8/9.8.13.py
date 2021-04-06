import numpy as np


stacks = {}


def find_max_height_sorted(boxes, index):
    """
    Function to calculate tallest possible stack

    Parameters
    ----------
    boxes: list
        A list of boxes, sorted by height, where each box is represented as a tuple of (L,W,H)

    index: int
        Tallest stack possible using only boxes[index:].

    Time Complexity
    ---------------
    O(N), where N is the number of boxes.

    Space Complexity
    ----------------
    O(N), where N is the number of boxes.
    """
    # with the largest box (boxes[0]) at bottom, we can iterate through the rest
    # of the boxes (boxes[i]), finding maximum height with them at bottom and
    # then, if boxes[0] and boxes[i] are compatible, we can form a new stack with
    # boxes[0] at bottom, under boxes[i]. we can update max_height if this stack
    # is tallest.
    max_height = boxes[index][2]
    for i in range(index + 1, len(boxes)):
        if compatible(boxes[index], boxes[i]):
            # use cache if available
            height = stacks[i] if i in stacks else find_max_height_sorted(boxes, i)
            if height + boxes[index][2] > max_height:
                max_height = height + boxes[index][2]

    # if this index has not been cached, we cache it
    if not index in stacks:
        stacks[index] = max_height
    return max_height


def find_max_height(boxes):
    """
    Function to calculate tallest possible stack

    Parameters
    ----------
    boxes: list
        A list of boxes, where each box is represented as a tuple of (L,W,H)

    Time Complexity
    ---------------
    O(Nlog(N)), where N is the number of boxes.

    Space Complexity
    ----------------
    O(N), where N is the number of boxes.
    """
    boxes = sorted(boxes, key=lambda x: -x[2])
    return find_max_height_sorted(boxes, 0)


def compatible(box_under, box_over):
    return (
        box_under[0] > box_over[0]
        and box_under[1] > box_over[1]
        and box_under[2] > box_over[2]
    )


box_details = [(3, 4, 5), (1, 2, 4), (7, 7, 7), (7, 7, 1000), (10, 9, 15), (1, 2, 3)]

print(find_max_height(box_details))
