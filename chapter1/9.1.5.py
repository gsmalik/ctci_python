def checkOneAway(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False

    longString, shortString = determineLongShortString(string1, string2)

    countDifferent = 0
    for index, character in enumerate(longString):
        if index == len(shortString):
            countDifferent += 1
        elif character != shortString[index]:
            countDifferent += 1
    return not countDifferent > 1

def determineLongShortString(string1, string2):
    if len(string1) >= len(string2):
        return string1, string2
    else:
        return string2, string1

print(checkOneAway("ples ", "ple"))