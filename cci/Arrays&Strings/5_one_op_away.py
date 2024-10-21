# Check if 2 strings are one operation away from each other

# Assume that they are lowercase and that s2 is smaller than s1

# def check_one_away(s1, s2):

#     if abs(len(s1) - len(s2)) > 1:
#         return False
    
#     if len(s1) == len(s2):
#         return one_edit_replace(s1, s2)
    
#     if len(s1) + 1 == len(s2):
#         return one_edit_insert(s1, s2)
#     elif len(s2) + 1 == len(s1):
#         return one_edit_insert(s2, s1)
    
#     return False
    
# def one_edit_replace(s1, s2):
#     flag = False
#     for i, j in zip(s1, s2):
#         if s1[i] != s2[j]:
#             if flag == True:
#                 return False
#             flag = True
#     return True
    
# def one_edit_insert(s1, s2):
#     index1 = 0
#     index2 = 0
#     while index1 < len(s1) and index2 < len(s2):
#         if s1[index1] != s2[index2]:
#             if index1 != index2:
#                 return False
#             index2 += 1
#         else:
#             index1 += 1
#             index2 += 1
#     return True


# print(check_one_away("pale", "pal"))            

# Better with just a single method

def check_one_away(s1, s2):
    # Case 1: Length difference greater than 1 means more than one edit away
    if abs(len(s1) - len(s2)) > 1:
        return False

    # Determine which is the shorter and which is the longer string
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    index1 = 0  # Pointer for the shorter string
    index2 = 0  # Pointer for the longer string
    found_difference = False

    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            # If already found a difference, return False
            if found_difference:
                return False
            found_difference = True

            # If lengths are different, move pointer for the longer string
            if len(s1) != len(s2):
                index2 += 1
                continue
        
        # If characters match, move both pointers
        index1 += 1
        index2 += 1

    return True