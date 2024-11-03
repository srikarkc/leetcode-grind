# Animal Shelter

class Animal:
    def __init__(self, name):
        self.name = name
        self.timestamp = None

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalShelter:
    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []
        self.timestamp = 0

    def enque(self, animal):
        animal.timestamp = self.timestamp
        self.timestamp += 1

        if isinstance(animal, Dog):
            self.dog_queue.append(animal)
        if isinstance(animal, Cat):
            self.cat_queue.append(animal)

    def dequeue(self):
        if not self.dog_queue or self.cat_queue:
            raise Exception("Animal shelter is currently empty.")
        
        if not self.dog_queue:
            return self.cat_queue.pop(0)
        if not self.cat_queue:
            return self.dog_queue.pop(0)
        
        if self.dog_queue[0].timestamp < self.cat_queue[0].timestamp:
            return self.dog_queue.pop(0)
        else:
            return self.cat_queue.pop(0)
        
    def dequeDog(self):
        if not self.dog_queue:
            raise Exception("Dog Queue is empty.")
        return self.dog_queue.pop(0)
    
    def dequeCat(self):
        if not self.cat_queue:
            raise Exception("Cat queue is empty.")
        return self.cat_queue.pop(0)