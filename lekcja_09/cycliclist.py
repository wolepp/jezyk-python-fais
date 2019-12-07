class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class CyclicList:
    """Klasa reprezentująca całą lisę cykliczną pojedynczo wiązaną."""

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
            node.next = node
        else:
            node.next = self.head
            self.tail.next = node
            self.head = node
        self.length += 1

    def insert_tail(self, node):
        pass

    def search(self, data):     # zwraca node lub None
        pass

    def remove(self, node):
        pass

    # scalanie dwóch list cyklicznych w czasie O(1)
    def merge(self, other):
        pass

    def clear(self):            # czyszczenie listy
        pass
