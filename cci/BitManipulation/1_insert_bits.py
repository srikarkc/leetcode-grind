# Given 2 32-bit numbers and i and j

def insert_bits(N, M, i, j):

    left = ~0 << (j + 1)

    right = (1 << i) - 1

    mask = left | right

    N_cleared = N & mask

    M_shifted = M << i

    return N_cleared | M_shifted