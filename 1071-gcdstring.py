str1 = "ABABAB"
str2 = "ABAB"

output = ""

for i in range(len(str2)):
    if str1[:i] == str2[:i]:
        output = str1[:i]

print(output)