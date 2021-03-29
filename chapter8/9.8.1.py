# We use this to store results of recursive sub-problems that we have already solved.
num_ways = {}


def calculate_ways(num_steps, use_cache=True):
    """
    Function to calculate number of different ways to scale given number of steps.

    Parameters
    ----------
    num_steps: int
        Number of steps that need to be scaled.
    use_cache: bool
        Wether to use stored results of repeating recursive sub-problems.

    Returns
    -------
    Total number of ways to scale given steps.

    Time Complexity
    ---------------
    O(3^N) if not using cache. O(N) otherwise.

    Space Complexity
    ----------------
    O(N).
    """
    # Use stored result if we have already solved this problem in the recursive
    # stack previously.
    if num_steps in num_ways and use_cache:
        return num_ways[num_steps]

    # If my number of steps is negative, that means that the current combination
    # of steps was not a valid combination. If number of steps is 0, that means
    # combination is valid.
    if num_steps <= 0:
        return int(num_steps == 0)

    # Calculate number of ways for this unique problem by iteratively trying each
    # of 1,2,3 as a first steps and adding up possible ways.
    ways = 0
    for steps in (3, 2, 1):
        ways += calculate_ways(num_steps - steps, use_cache)

    # Store result
    num_ways[num_steps] = ways

    return ways


# Notice that 100 is much faster than 25 since we are caching results in the case
# of 100 and solving repeating sub problems every time in case of 25.
print(calculate_ways(100, True))
print(calculate_ways(25, False))