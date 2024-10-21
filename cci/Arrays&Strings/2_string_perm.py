def string_perm(string1, string2):
    if len(string1) != len(string2):
        return False
    return sorted(string1) == sorted(string2)

print(string_perm("hel", "leh"))
print(string_perm("hello", "hel"))