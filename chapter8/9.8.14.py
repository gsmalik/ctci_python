def find_parenthesis(level, expression, result):

    if len(expression) == 1:
        return int(result == bool(int(expression[0])))

    ways = 0
    for index, symbol in enumerate(expression):
        if result == True:
            if symbol == "^":
                ways = (
                    ways
                    + (
                        find_parenthesis(level + 1, expression[:index], True)  # True
                        * find_parenthesis(
                            level + 1, expression[index + 1 :], False
                        )  # False
                    )
                    + (
                        find_parenthesis(level + 1, expression[:index], False)  # False
                        * find_parenthesis(
                            level + 1, expression[index + 1 :], True
                        )  # True
                    )
                )
            if symbol == "|":
                ways = (
                    ways
                    + (
                        find_parenthesis(level + 1, expression[:index], True)  # True
                        * find_parenthesis(
                            level + 1, expression[index + 1 :], False
                        )  # False
                    )
                    + (
                        find_parenthesis(level + 1, expression[:index], False)  # False
                        * find_parenthesis(
                            level + 1, expression[index + 1 :], True
                        )  # True
                    )
                    + (
                        find_parenthesis(level + 1, expression[:index], True)  # True
                        * find_parenthesis(
                            level + 1, expression[index + 1 :], True
                        )  # True
                    )
                )
            if symbol == "&":
                ways = ways + (
                    find_parenthesis(level + 1, expression[:index], True)  # True
                    * find_parenthesis(level + 1, expression[index + 1 :], True)  # True
                )
        else:
            if symbol == "^":
                ways = (
                    ways
                    + (
                        find_parenthesis(level + 1, expression[:index], True)  # True
                        * find_parenthesis(
                            level + 1, expression[index + 1 :], True
                        )  # True
                    )
                    + (
                        find_parenthesis(level + 1, expression[:index], False)  # False
                        * find_parenthesis(
                            level + 1, expression[index + 1 :], False
                        )  # False
                    )
                )
            if symbol == "|":
                ways = ways + (
                    find_parenthesis(level + 1, expression[:index], False)  # False
                    * find_parenthesis(
                        level + 1, expression[index + 1 :], False
                    )  # False
                )
            if symbol == "&":
                ways = (
                    ways
                    + (
                        find_parenthesis(level + 1, expression[:index], True)  # True
                        * find_parenthesis(
                            level + 1, expression[index + 1 :], False
                        )  # False
                    )
                    + (
                        find_parenthesis(level + 1, expression[:index], False)  # False
                        * find_parenthesis(
                            level + 1, expression[index + 1 :], True
                        )  # True
                    )
                    + (
                        find_parenthesis(level + 1, expression[:index], False)  # False
                        * find_parenthesis(
                            level + 1, expression[index + 1 :], False
                        )  # False
                    )
                )
    return ways


def create_expression_list(string):
    expression = []
    for character in string:
        expression.append(character)
    return expression


test_string = "0&0&0&1^1|0"
test_expression = create_expression_list(test_string)
print(test_expression)
print(find_parenthesis(0, test_expression, True))
