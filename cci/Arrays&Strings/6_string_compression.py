# Counts of repeated characters

def string_comp(input_string):
    if len(input_string) == 0:
        return ""
    
    output_string = []
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i-1]:
            count += 1
        else:
            output_string.append(input_string[i-1])
            output_string.append(str(count))
            count = 1

    # add the last character and its count
    output_string.append(input_string[-1])
    output_string.append(str(count))

    compressed_string = ''.join(output_string)

    return compressed_string if len(compressed_string) < len(input_string) else input_string


print(string_comp("aaabbbcccc"))