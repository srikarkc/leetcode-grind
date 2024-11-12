# given a real number between 0 & 1 - represent as a binary string

def binary_to_string(x):
    if x <= 0 or x >= 1:
        return "ERROR"
    
    binary_str = "0."

    while x > 0:
        if len(binary_str) >= 32:
            return "ERROR"
        
    x *= 2
    if x >= 1:
        binary_str += "1"
        x -= 1
    else:
        binary_str += "0"

    return binary_str