class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0         # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None
        self.current = None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        current = self.current
        if current:
            self.current = self.current.next
            return current
        raise StopIteration
        
    def __str__(self):
        return '[' + ', '.join([str(node) for node in self]) + ']'

    def is_empty(self):
        return self.length == 0

    def count(self):      # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):          # klasy O(N)
        """Skraca listę o jej ogon i go zwraca."""
        if self.length == 0:
            raise ValueError("pusta lista")
        tail = self.tail
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            node = self.head
            while node.next is not self.tail:
                node = node.next
            node.next = None
            self.tail = node
        return tail

    def merge(self, other):         # klasy O(1)
        """Węzły z listy other są przepinane do listy self na jej koniec."""
        if other.length == 0:
            return
        if self.length == 0:
            self.head = other.head
        else:
            self.tail.next = other.head
        self.tail = other.tail
        self.length += other.count()
        # czyszczenie listy other
        other.clear()

    def clear(self):            # czyszczenie listy
        """Czyści listę."""
        self.head = self.tail = None
        self.length = 0

    def search(self, data):   # klasy O(N)
        """Zwraca łącze do węzła o podanym kluczu lub None."""
        if self.length == 0:
            return None
        node = self.head
        while node.data != data:
            if node.next is None:
                return None
            node = node.next
        return node

    def find_min(self):         # klasy O(N)
        """Zwraca łącze do węzła z najmniejszym kluczem."""
        if self.length == 0:
            return None
        min_node = node = self.head
        while node.next:
            node = node.next
            if node.data < min_node.data:
                min_node = node
        return min_node

    def find_max(self):         # klasy O(N)
        """Zwraca łącze do węzła z największym kluczem."""
        if self.length == 0:
            return None
        max_node = node = self.head
        while node.next:
            node = node.next
            if node.data > max_node.data:
                max_node = node
        return max_node

    def reverse(self):          # klasy O(N)
        """Odwracanie kolejności węzłów na liście."""
        current = self.head
        prev_node = None
        while current is not None:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head, self.tail = self.tail, self.head
