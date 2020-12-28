def make_change(ammount, denomination, index):
    if ammount == 0:
        return 1
    if ammount < 0 or index > len(denomination)-1:
        return 0
    current_denomination = denomination[index]
    count = 0
    ways=0
    while current_denomination*count <= ammount:
        ways += make_change(ammount-current_denomination*count, denomination, index+1)
        print("ways",ways)
        count += 1
    return ways

denomination = [1, 10, 25]
ammount = 27
print(make_change(ammount, denomination, 0))
