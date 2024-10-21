# Replace all spaces in the string with %20

# print(''.join("he llo  ".strip().replace(' ', '%20')))

# def urlify(string):
#     return ''.join(string.strip().replace(' ', '%20'))

# Better solution that handles the true_length

def urlify(string, true_length):
    trimmed_string = string[:true_length]
    return trimmed_string.replace(' ', '%20')

print(urlify('Mr John Smith  ', 13))