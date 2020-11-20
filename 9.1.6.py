def compressString(string1):

    newString = []
    lastCharacter = ''
    compressed = False
    for character in string1:
        if character != lastCharacter:
            count = 1
            lastCharacter = character
            newString.append(character)
            newString.append('1')
        else:
            count += 1
            compressed = True
            newString[-1] = count
    return newString if compressed else string1

print(compressString("aabcccaaafs"))