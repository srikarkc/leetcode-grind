# Classic problem to find if the input string contains only matching parentheses

def matching_parentheses(s):

    stack = []

    matching_brackets = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    for char in s:
        if s in matching_brackets.values():
            stack.append(char)
        elif s in matching_brackets.keys():
            # check if stack is empty or there is a mismatch
            if not stack or stack[-1] != matching_brackets[char]:
                return False
            stack.pop()
        else:
            return False
    
    # If stack is empty, parentheses are balanced
    return not stack 