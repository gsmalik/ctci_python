import numpy as np


stacks = []


def create_stack(boxes):
    # sort according to height
    boxes = boxes[np.argsort(-boxes[:, 0])]

    # remove boxes that do not satisfy width and length
    index = 0
    removed_indices = []
    stack_boxes = boxes
    print(stack_boxes)
    while index < np.shape(stack_boxes)[0] - 1:
        if (
            stack_boxes[index][1] < stack_boxes[index + 1][1]
            or stack_boxes[index][2] < stack_boxes[index + 1][2]
        ):
            removed_indices.append(stack_boxes[index + 1])
            stack_boxes = np.delete(stack_boxes, index + 1, 0)
        else:
            index += 1
    print(removed_indices)
    if len(removed_indices) == np.shape(boxes)[0]:
        stacks.append(1)
        return
    else:
        stacks.append(np.shape(boxes)[0] - len(removed_indices))
        # Create stack out of remaining boxes
        if removed_indices:
            create_stack(np.array(removed_indices))


num_boxes = 3
box_details = np.random.randint(1, 20, (num_boxes, 3))
create_stack(box_details)
print("Box Specification\n", box_details)
print("Possible Stacks:", stacks)
print("Heighest Stacl:", max(stacks))

