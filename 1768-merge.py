# Merge strings alternatively

word1 = "Hello"

word2 = "World"

output = ""

min_len = min(len(word1), len(word2))

for i in range(min_len):
    output += word1[i] + word2[i]

output += word1[min_len:] + word2[min_len:]

print(output)