# create a global list to append final parenthesis combinations to.
list_parens = []


def gen_parens(current_parens, open_rem, close_rem):
    """
    Function to generate valid combinations of parenthesis.

    Parameters
    ----------
    current_parens: str
        The current string representation of parenthesis, to add combinations to.
    open_rem: int
        Number of open parenthesis that can be added to a combination.
    close_rem: int
        Number of close parenthesis that can be added to a combination.

    Time Complexity
    ---------------
    Time complexity for this is a tad hard since the trees will not be balanced as it
    will depend on wether we can add an opening/closing bracket or not. A very loose
    bound will be O(2^N), where N is the number of brackets allowed.

    Space Complexity
    ----------------
    O(N), where N is the number of brackets allowed.
    """

    # exit condition is when we have no more brackets to add.
    if open_rem == close_rem == 0:
        list_parens.append(current_parens)
        return
    # we can always add an open bracket if we have them available.
    if open_rem > 0:
        gen_parens(current_parens + "(", open_rem - 1, close_rem)
    # we only add a closing bracket when their count exceeds that of opening
    # brackets
    if close_rem > open_rem:
        gen_parens(current_parens + ")", open_rem, close_rem - 1)


n = 4
gen_parens("", n, n)
print(list_parens)