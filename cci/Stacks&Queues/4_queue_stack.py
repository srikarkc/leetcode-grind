# Queue with Stacks

class QueueStack:
    def __init__(self):
        self.in_queue = []
        self.out_queue = []

    def push(self, value):
        self.in_queue.append(value)
    
    def pop(self):
        while not self.out_queue:
            while self.in_queue:
                self.out_queue.append(self.in_queue.pop())
        
        if not self.out_queue:
            raise Exception("Queue is empty!")
        
        return self.out_queue.pop()
    
    def peek(self):
        if not self.out_queue:
            while self.in_queue:
                self.out_queue.append(self.in_queue.pop())

        if not self.out_queue:
            raise Exception("Queue is empty!")
        
        return self.out_queue[-1]
    
    def is_empty(self):
        return not self.in_queue and not self.out_queue