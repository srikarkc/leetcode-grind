# Sort stack - smallest items on top

def sort_stack(stack):
    temp_stack = []

    while stack:
        current = stack.pop()

        while temp_stack and temp_stack[-1] > current:
            stack.append(temp_stack.pop())

        temp_stack.append(current)

    while temp_stack:
        stack.append(temp_stack.pop())

    return stack