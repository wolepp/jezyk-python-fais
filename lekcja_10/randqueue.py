import random


class RandomQueue:
    """Implementacja kolejki losowej."""

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def insert(self, item):
        """Wkłada item do kolejki"""

        self.items.append(item)

    def remove(self):
        """Usuwa losowy element z kolejki i go zwraca

        Złożoność O(1)
        """

        if self.is_empty():
            raise Exception('Kolejka jest pusta')
        idx = random.randrange(len(self.items))
        self.items[idx], self.items[-1] = self.items[-1], self.items[idx]
        return self.items.pop()

    def is_empty(self):
        """Sprawdza czy koleja jest pusta"""

        return not self.items

    def is_full(self):
        """Sprawdza czy koleja jest pełna

        Kolejka nigdy nie jest pełna - wartości przechowywane są w tablicy,
        której rozmiar ograniczony jest przez sys.maxsize.
        """

        return False

    def clear(self):
        """Czyści kolejkę"""

        self.items = []
