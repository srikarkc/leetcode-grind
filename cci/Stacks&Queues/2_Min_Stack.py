# Design a stack with push, pop, & min all in O(1)

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            raise Exception("Stack is empty")
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value
    
    def peek(self):
        if not self.stack:
            raise Exception("Stack is empty")
        return self.stack[-1]
    
    def get_min(self):
        if not self.min_stack:
            raise Exception("Stack is empty")
        return self.min_stack[-1]