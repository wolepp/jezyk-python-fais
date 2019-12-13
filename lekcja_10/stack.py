class Stack:
    """
    Tablicowa implementacja stosu.

    Stos o rozmiarze size, może przechowywać liczby całkowite od 0 do size-1.
    """

    def __init__(self, size):
        self.items = size * [None]
        self.exists = size * [0]
        self.size = size
        self.index = 0

    def __str__(self):
        return str(self.items[:self.index])

    def is_empty(self):
        return not sum(self.exists)

    def is_full(self):
        return self.index == self.size-1

    def push(self, item):
        if not 0 <= item <= self.size-1:
            raise ValueError('Wartość musi być liczbą całkowitą z przedziału [0, '+self.size-1+']')
        if self.exists[item]:
            return
        if self.is_full():
            raise Exception('Stos jest pełny')
        self.items[self.index] = item
        self.exists[item] = 1
        self.index += 1

    def pop(self):
        if self.is_empty():
            raise Exception('Stos jest pusty')
        item = self.items[self.index]
        self.items[self.index] = None
        self.index -= 1
        self.exists[item] = 0
        return item
