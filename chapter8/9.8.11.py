def make_change(amount, list_denomination):
    if amount <= 0 or not list_denomination:
        return int(amount == 0)
    ways = 0
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
