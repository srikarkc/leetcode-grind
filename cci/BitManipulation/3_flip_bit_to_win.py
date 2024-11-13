def flip_bits_to_win(n: int) -> int:
    if ~n == 0:
        return n.bit_length()
    
    current_length = 0
    previous_length = 0
    max_length = 1

    while n != 0:
        if (n & 1) == 1:
            current_length += 1
        else:
            previous_length = current_length if (n & 2) else 0
            current_length = 0
        max_length = max(max_length, previous_length + current_length + 1)
        n >>= 1

    return max_length