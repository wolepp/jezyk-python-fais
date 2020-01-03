import random


class RandomQueue:
    """Implementacja kolejki losowej."""

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            raise Exception('Kolejka jest pusta')
        idx = random.randrange(len(self.items))
        self.items[idx], self.items[-1] = self.items[-1], self.items[idx]
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def clear(self):
        self.items = []
