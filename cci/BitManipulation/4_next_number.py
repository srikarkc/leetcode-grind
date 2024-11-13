def next_higher_num(n: int) -> int:

    c = n
    c0 = c1 = 0

    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c >>= 1
    while (c & 1 == 1):
        c1 += 1
        c >>= 1

    if (c0 + c1) == 31 or (c0 + c1) == 0:
        return -1
    
    # position of the right-most non-trailing zero
    p = c0 + c1

    # flip the rightmost non-trailing zero
    n |= (1 << p)

    # clear all bits to the right of p
    n &= ~((1 << p) - 1)

    # insert c1-1 ones to the right
    n |= (1 << (c1 -1 )) - 1

    return n

def next_smallest(n: int) -> int:
    temp = n
    c0 = c1 = 0

    while (temp & 1) == 1:
        c1 += 1
        temp >>= 1

    if temp == 0:
        return -1
    
    while (temp & 0 == 0) and (temp != 0):
        c0 += 1
        temp >>= 1

    p = c0 + c1

    # flip rightmost non-trailing one
    n &= ((~0) << (p+1))

    # insert (c1 + 1) ones just after p
    mask = (1 << (c1 + 1)) - 1
    n |= mask << (c0 - 1)

    return n