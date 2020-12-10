def calculate_ways_top_bottom(num_steps):
    ways = 0
    if num_steps <= 1:
        return 1
    for steps in (3, 2, 1):
        if num_steps >= steps:
            # print(steps, num_steps)
            ways += calculate_ways_top_bottom(num_steps - steps)

    return ways


def calculate_ways_bottom_top(num_steps):
    arr = []
    for index in range(num_steps):
        if index == 0:
            arr.append(1)
        elif index == 1:
            arr.append(2)
        elif index == 2:
            arr.append(1+arr[index-1]+arr[index-2])
        else:
            arr.append(arr[index-1]+arr[index-2]+arr[index-3])
    return arr[num_steps-1]
    
print(calculate_ways_top_bottom(4))
print(calculate_ways_bottom_top(4))
