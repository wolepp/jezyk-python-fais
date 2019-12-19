class Node:
    """Klasa reprezentująca węzeł listy dwukierunkowej."""

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DoubleList:
    """Klasa reprezentująca całą listę dwukierunkową."""

    def __init__(self):
        self.length = 0   # może to trzymać w polu data wartownika?
        self.nil = Node()   # wartownik
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def is_empty(self):
        # return self.length == 0
        return self.nil.next == self.nil

    def count(self):
        return self.length

    def insert_head(self, node):
        node.next = self.nil.next
        node.prev = self.nil
        self.nil.next.prev = node
        self.nil.next = node
        self.length += 1

    def insert_tail(self, node):
        node.next = self.nil
        node.prev = self.nil.prev
        self.nil.prev.next = node
        self.nil.prev = node
        self.length += 1

    def remove_head(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.nil.next
        # Teraz ogólny schemat usuwania węzła.
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1
        return node

    def remove_tail(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.nil.prev
        # Teraz ogólny schemat usuwania węzła.
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1
        return node

    def find_max(self):
        """Zwraca łącze do węzła z największym kluczem."""
        if self.is_empty():
            return None
        max_node = node = self.nil.next
        while node.next != self.nil:
            node = node.next
            if node.data > max_node.data:
                max_node = node
        return max_node

    def find_min(self):
        """Zwraca łącze do węzła z najmniejszym kluczem."""
        if self.is_empty():
            return None
        min_node = node = self.nil.next
        while node.next != self.nil:
            node = node.next
            if node.data < min_node.data:
                min_node = node
        return min_node

    def remove(self, node):
        """Usuwa wskazany węzeł z listy."""
        if self.is_empty():
            raise ValueError("pusta lista")

        # gdzieś w środku listy
        if node.prev is not self.nil and node.next is not self.nil:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
        elif node.next is self.nil:                 # na końcu listy
            self.remove_tail()
        elif node.prev is self.nil:                 # na początku listy
            self.remove_head()
        node.next = node.prev = None

    def clear(self):
        """Czyszczenie listy."""
        self.nil.next = self.nil
        self.nil.prev = self.nil
        self.length = 0
