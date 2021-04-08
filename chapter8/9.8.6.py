def move_disks(num_disks, origin, buffer, destination):
    """
    Function to implement towers of hanoi problem.

    Parameters
    ----------
    num_disks: int
        Number of disks to move, starting from top.
    origin: int
        Index of rod to use as origin.
    buffer: int
        Index of rod to use as buffer while moving disks.
    origin: int
        Index of rod to move disks to.

    Time Complexity
    ---------------
    O(2^N), where N is the number of disks.

    Space Complexity
    ----------------
    O(N), where N is the number of disks.
    """
    # exit condition
    if num_disks <= 0:
        return
    # move top 'num-1' disks from origin to buffer using destination as buffer.
    move_disks(
        num_disks=num_disks - 1, origin=origin, buffer=destination, destination=buffer
    )
    print("Moved disk #", num_disks, "from", origin, "to", destination)
    # move top 'num-1' disks from buffer to destination using origin as buffer.
    move_disks(
        num_disks=num_disks - 1, origin=buffer, buffer=origin, destination=destination
    )


move_disks(5, 0, 1, 2)
