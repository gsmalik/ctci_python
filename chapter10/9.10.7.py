import numpy as np


def vectorize_integers(array, dtype_range, allowed_mem_bits):
    """
    Assumes dtype of integers to be 32 bits
    """
    bvr = np.zeros(allowed_mem_bits)

    # O(array_size)
    for num in array:
        bvr[int(num / int(dtype_range / allowed_mem_bits))] += 1

    # O(mem_size)
    for index, count in enumerate(bvr):
        if count < dtype_range / allowed_mem_bits:
            break

    # We have 80 mil bit that now can be used to bit vectorize a space of roughly
    # 2**31/80m = 27 bits
    bvr[: int(dtype_range / allowed_mem_bits)] = 0

    # O(array_size)
    for num in array:
        if (
            index * int(dtype_range / allowed_mem_bits)
            <= num
            < (index + 1) * int(dtype_range / allowed_mem_bits)
        ):
            bvr[num - (index) * int(dtype_range / allowed_mem_bits)] = 1

    # O(2**31/mem_size)
    for i, bit in enumerate(bvr[: int(dtype_range / allowed_mem_bits)]):
        if bit == 0:
            return index * int(int(dtype_range / allowed_mem_bits)) + i


dtype_range = 2**20
test = np.random.choice(range(dtype_range), 1000000, replace=False)
print(test)
print(vectorize_integers(test, dtype_range,2 ** 10))

assert vectorize_integers(test, dtype_range, 2 ** 10) not in test
