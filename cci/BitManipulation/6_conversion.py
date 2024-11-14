# determine the number of bits to flip to convert integer A to integer B

def convert(A: int, B: int) -> int:
    xor_result = A ^ B

    count = 0
    while xor_result:
        count += xor_result & 1
        xor_result >>= 1

    return count


# alternative built-in method

def convert_short(A, B):
    xor_result = A ^ B
    return bin(xor_result).count('1')
