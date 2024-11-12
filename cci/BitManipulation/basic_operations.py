def get_bit(num, i):
    """
    Returns the bit at position i in num.
    """
    mask = 1 << i
    return (num & mask) != 0

def set_bit(num, i):
    """
    Sets the bit at position i in num to 1.
    """
    mask = 1 << i
    return num | mask

def clear_bit(num, i):
    """
    Clears the bit at position i in num (sets it to 0).
    """
    mask = ~(1 << i)
    return num & mask

def update_bit(num, i, bit_is_1):
    """
    Updates the bit at position i in num to the value bit_is_1.
    If bit_is_1 is True, set the bit to 1; if False, set it to 0.
    """
    # Clear the bit at position i
    mask = ~(1 << i)
    num_cleared = num & mask
    # Set the bit to the desired value
    return num_cleared | (bit_is_1 << i)

# Testing the functions
num = 0b1011  # 11 in binary

# Get bit at position 1
print(f"Get bit at 1: {get_bit(num, 1)}")  # Expected: True

# Set bit at position 2
print(f"Set bit at 2: {bin(set_bit(num, 2))}")  # Expected: 0b1111

# Clear bit at position 3
print(f"Clear bit at 3: {bin(clear_bit(num, 3))}")  # Expected: 0b0011

# Update bit at position 1 to 0
print(f"Update bit at 1 to 0: {bin(update_bit(num, 1, 0))}")  # Expected: 0b1001

# Update bit at position 2 to 1
print(f"Update bit at 2 to 1: {bin(update_bit(num, 2, 1))}")  # Expected: 0b1111
