class PriorityQueue:

    def __init__(self, cmpfunc=lambda a, b: (a > b) - (a < b)):  # w python3 brak cmp
        self.items = []
        self.cmpfunc = cmpfunc

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        """Sprawdza czy kolejka jest pusta"""

        return not self.items

    def insert(self, item):
        """Wkłada item do kolejki"""

        self.items.append(item)

    def remove(self):
        """Zdejmuje element z kolejki i go zwraca"""

        maxi = 0
        for i in range(1, len(self.items)):
            if self.cmpfunc(self.items[i], self.items[maxi]) == 1:
                maxi = i
        return self.items.pop(maxi)
