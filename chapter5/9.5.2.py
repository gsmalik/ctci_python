number = 0.1252

assert 0 < number < 1

bits=0
binary_repr = []
while number != 0 and bits < 32:
    bits+=1
    if number - 2**(-bits) >= 0:
        binary_repr.append("1")
        number -= 2**(-bits)
    else:
        binary_repr.append("0")

assert len(binary_repr) <= 32
print(binary_repr)