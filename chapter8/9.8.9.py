def permute_parens(permutation, list_permutations, left_rem, right_rem):
    if left_rem == right_rem == 0:
        list_permutations.append(permutation)
        return list_permutations
    elif right_rem < left_rem or left_rem * right_rem < 0:
        return list_permutations
    else:
        list_permutations = permute_parens(
            permutation + "(", list_permutations, left_rem - 1, right_rem
        )
        list_permutations = permute_parens(
            permutation + ")", list_permutations, left_rem, right_rem - 1
        )
        return list_permutations


n = 3
print(permute_parens("", [], n, n))
