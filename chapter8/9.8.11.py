def make_change(amount, list_denomination):
    """
    Function to count different ways of making change of given amount with given
    denomination.

    Parameters
    ----------
    amount: int
        The amount of change.
    list_denomination: list
        The list of denomination to use to make change.
    
    Time Complexity
    ---------------
    O(C^N), where C is the amount and N is the number of different denominations. Note
    that this is a very loose upper bound. We basically first think, for example in
    case of [1,5,10,25] for making 100, that we can have 100 branches for 1, then
    for each branch, we will have [5,10,25] and we can have 100 branches for 5 and then
    100 branches for 10 and then 100 for 25, with an upper bound of 100^4. This is 
    very loose.

    Space Complexity
    ----------------
    O(N), where N is the number of different denominations.
    """
    # exit condition if amount is less than 0 or list of denomination is empty.
    if amount <= 0 or not list_denomination:
        return int(amount == 0)

    # initialise number of ways
    ways = 0

    # keep increasing count of first denomination until the left amount becomes
    # negative. calculate ways of calculating said left amount with remaining
    # denominations in list.
    num = 0
    while num * list_denomination[0] <= amount:
        ways = ways + make_change(
            amount - num * list_denomination[0], list_denomination[1:]
        )
        num = num + 1
    return ways


denomination = [1, 10, 25]
amount = 33
print(make_change(amount, denomination))
