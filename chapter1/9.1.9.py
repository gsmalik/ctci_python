def checkRotation(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        return isSubstring(string1+string1, string2)

def isSubstring(string1, string2):
    return (string2 in string1)

print(checkRotation('waterbottle', 'lewaterbott'))