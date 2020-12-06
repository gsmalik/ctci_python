def reverse_string(string):
    return string[::-1]


i = 0
j = 3
N = "1010101011"
M = "0110"

assert j - i + 1 == len(M)

# Reverse String
N = reverse_string(N)
M = reverse_string(M)

N = N[:i] + M + N[j + 1 :]

N = reverse_string(N)

print(N)