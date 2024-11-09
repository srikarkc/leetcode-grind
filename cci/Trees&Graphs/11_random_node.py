# Random nodes

import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1

    def insert(self, value):
        if value <= self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = TreeNode(value)
            self.size += 1
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = TreeNode(value)
            self.size += 1

    def find(self, value):
        if value == self.value:
            return self
        elif value < self.value and self.left:
            return self.left.find(value)
        elif value > self.value and self.right:
            return self.right.find(value)
        return None
    
    def get_random_node(self):
        left_size = self.left.size if self.left else 0
        random_index = random.randint(1, self.size)

        if random_index <= left_size:
            return self.left.get_random_node()
        elif random_index == left_size + 1:
            return self
        else:
            return self.right.get_random_node()
        
    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if not self.left and not self.right:
                return None
            elif not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:
                successor = self.right.find_min()
                self.value = successor.value
                self.right = self.right.delete(successor.value)

        self.size = (1 + 
                     (self.left.size if self.left else 0) + 
                     (self.right.size if self.right else 0))
        return self
    
    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current