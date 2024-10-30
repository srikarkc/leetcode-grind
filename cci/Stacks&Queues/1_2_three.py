# Flexible 3 in 1

class FlexibleThreeInOne:
    def __init__(self, capacity):
        self.array = [0] * capacity
        self.stack_top = [-1, -1, -1]
        self.capacity = capacity
        self.sizes = [0, 0, 0]
        self.total_size = 0

    def is_full(self):
        return self.total_size == self.capacity
    
    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0
    
    def next_index(self, index):
        return (index + 1) % self.capacity
    
    def prev_index(self, index):
        return (index - 1 + self.capacity) % self.capacity
    
    def expand_stack(self, stack_num):
        next_stack = (stack_num + 1) % 3
        if self.sizes[next_stack] == 0:
            return
        
        i = self.stack_top[next_stack]
        while _ in range(self.sizes[next_stack]):
            next_i = self.next_index[i]
            self.array[next_i] = self.array[i]
            i = self.prev_index[i]
        self.stack_top[next_stack] = self.next_index[self.stack_top[next_stack]]

    def push(self, stack_num, value):
        if self.is_full:
            raise Exception("Array is full")
        
        if self.sizes(stack_num) > 0 and self.next_index(self.stack_top[stack_num]) == self.stack_top[(stack_num + 1) % 3]:
            self.expand_stack(stack_num)
        
        if self.sizes[stack_num] == 0:
            self.stack_top[stack_num] = (self.stack_top[(stack_num - 1) % 3] + 1)
        else:
            self.stack_top[stack_num] = self.next_index(self.stack_top[stack_num])

        self.array[self.stack_top[stack_num]] = value
        self.sizes[stack_num] += 1
        self.total_size += 1

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception(f"Stack {stack_num} is empty")
        
        value = self.array[self.stack_top[stack_num]]
        self.array[self.stack_top[stack_num]] = 0
        self.stack_top[stack_num] = self.prev_index(self.stack_top[stack_num])
        self.sizes[stack_num] -= 1
        self.total_size -= 1
        return value
    
    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception(f"Stack {stack_num} is empty")
        return self.array[self.stack_top[stack_num]]