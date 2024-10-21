# myString = "hel"

# unique = True

# for i in range(len(myString)):
#     for j in range(i+1, len(myString)):
#         if myString[i] == myString[j]:
#             unique = False

# print(f"Is unique: {unique}")

def is_unique_chars(s):
    checker = 0
    for char in s:
        # Get the position of the character in the alphabet (0 for 'a', 1 for 'b', etc.)
        val = ord(char) - ord('a')
        # Check if the bit at position 'val' is already set
        if (checker & (1 << val)) > 0:
            return False
        # Set the bit at position 'val'
        checker |= (1 << val)
    return True

# Test the function
print(is_unique_chars("hel"))  # Output: True
print(is_unique_chars("hello"))  # Output: False
