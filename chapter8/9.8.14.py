def find_parenthesis_combinations(expression, expected_bool):
    """
    Function to calculate different parenthesis combinations to evaluate expression to
    the expected boolean value.

    Parameters
    ----------
    expression: str
        Expression to find combinations for.

    expected_bool: bool
        Expected boolean value the expression needs to evaluate to.

    Time Complexity
    ---------------
    Too complicated I think. But should be 4^N roughly speaking, where N is the number
    of binary operators in the expression. The 4 comes from calculating left_false,
    left_true, right_false and right_true. But the tree will not be balanced. So this
    is a loose upper bound.

    Space Complexity
    ----------------
    O(N), where N is the number of binary operators in the expression
    """
    # exit condition
    if len(expression) == 1:
        return int(expected_bool == bool(int(expression[0])))

    # initialise number of ways for expression to evaluate to the expected bool
    num_ways = 0

    # iterate through operator symbols
    for index, symbol in enumerate(expression):
        # find all possible ways of evaluating left side and right side to True and False
        if symbol in ["^", "|", "&"]:
            left_false = find_parenthesis_combinations(expression[:index], False)
            left_true = find_parenthesis_combinations(expression[:index], True)
            right_false = find_parenthesis_combinations(expression[index + 1 :], False)
            right_true = find_parenthesis_combinations(expression[index + 1 :], True)

        # find number of ways for each symbol
        if symbol == "^":
            num_ways = num_ways + (
                (left_false * right_true) + (left_true * right_false)
                if expected_bool
                else ((left_true * right_true) + (left_false * right_false))
            )

        if symbol == "|":
            num_ways = num_ways + (
                left_true * right_false
                + left_true * right_true
                + left_false * right_true
                if expected_bool
                else left_false * right_false
            )

        if symbol == "&":
            num_ways = num_ways + (
                left_true * right_true
                if expected_bool
                else left_false * right_false
                + left_false * right_true
                + left_true * right_false
            )

    return num_ways


def create_expression_list(string):
    expression = []
    for character in string:
        expression.append(character)
    return expression


test_string = "0&0&0&1^1|0"
test_expression = create_expression_list(test_string)
print(test_expression)
print(find_parenthesis_combinations(test_expression, True))