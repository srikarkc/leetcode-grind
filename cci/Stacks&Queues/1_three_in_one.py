class ThreeInOne:
    def __init__(self, stack_size):
        self.num_stacks = 3
        self.stack_size = stack_size
        self.values = [0] * (self.num_stacks * stack_size)
        self.sizes = [0] * self.num_stacks

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size
    
    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0
    
    def index_of_top(self, stack_num):
        offset = stack_num * self.num_stacks
        return offset + self.sizes(stack_num) - 1
    
    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise Exception(f"Stack {stack_num} is full.")
        self.sizes[stack_num] += 1
        self.values[self.index_of_top(stack_num)] = value
    
    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception(f"Stack {stack_num} is empty.")
        top_index = self.index_of_top(stack_num)
        value = self.values[top_index]
        self.values[top_index] = 0
        self.sizes[stack_num] -= 1
        return value
    
    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception(f"Stack {stack_num} is empty.")
        top_index = self.index_of_top(stack_num)
        return self.values[top_index]