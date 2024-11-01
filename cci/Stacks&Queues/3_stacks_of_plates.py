class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, value):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if not self.stacks:
            raise Exception("Stack empty")
        
        value = self.stacks[-1].pop()

        if len(self.stacks[-1]) == 0:
            self.stacks.pop()

        return value
    
    def pop_at(self, index):
        if index < 0 or index >= len(self.stacks):
            raise Exception("Invalid stack index")
        
        value = self.stacks[index].pop()

        if len(self.stacks[index]) == 0:
            self.stacks.pop(index)

        return value