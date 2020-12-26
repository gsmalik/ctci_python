def move_disks(num_disks, origin, buffer, destination):
    if num_disks <= 0:
        return
    move_disks(num_disks-1, origin, destination, buffer)
    print("Moved disk #", num_disks, "from", origin, "to", destination)
    move_disks(num_disks-1, buffer, origin, destination)

move_disks(5,0,1,2)