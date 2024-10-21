# Find if the given word has a palindrome permutation

given_word = 'race car'

def has_plaindrom_per(given_word):
    
    char_counter = {}

    given_word = given_word.replace(" ", "")

    for char in given_word:
        char_counter[char] = char_counter.get(char, 0) + 1

    # Check if the character count is divisible by 2 and if so remove it
    for k, v in char_counter.items():
        if v % 2 == 0:
            char_counter.pop(k)

    # Ensure that the last element is only 1
    if len(char_counter == 1):
        for k, v in char_counter.items():
            if v == 1:
                return True
            
    return False

print(has_plaindrom_per("race car"))
print(has_plaindrom_per('rock'))