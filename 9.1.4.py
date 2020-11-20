def palindromePermutation(string):
    asciiList = [0]*128
    print(len(asciiList))
    for character in string:
        print(character, ord(character))
        asciiList[ord(character)] += 1
    oddOccurences = 0
    for count in asciiList:
        if count % 2 != 0:
            oddOccurences += 1
    if oddOccurences > 1:
        return False
    else:
        return True

print(palindromePermutation("tactc a"))
