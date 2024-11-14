# Program to swap odd and even bits

# def swap(n: int) -> int:

#     even_mask = 0xAAAAAAAA # ...1010
#     odd_mask = 0x55555555 # ...0101

#     return (n & even_mask >> 1) | (n & odd_mask << 1)
    

def pairwise_swap(n: int) -> int:
    even_bits = n & 0xAAAAAAAA
    odd_bits = n & 0x55555555

    return (even_bits >> 1) | (odd_bits << 1)