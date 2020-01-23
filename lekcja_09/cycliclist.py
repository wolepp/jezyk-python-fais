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
        # przechowuje tail, aby zmniejszyc zlozonosc obliczeniowa wielu dzialan
        # np. insert_tail jest wtedy O(1), zamiast O(N) - nie trzeba dochodzic
        # do wezla poprzedzajacego tail
        self.length = 0

    def is_empty(self):
        """Sprawdza czy lista jest pusta"""

        return self.head is None

    def count(self):
        """Zwraca liczbę elementów"""

        return self.length

    def insert_head(self, node):
        """Wstawia node na pozycję head do listy"""

        if self.length == 0:
            self.head = self.tail = node
            self.head.next = self.head
        else:
            node.next = self.head
            self.tail.next = node
            self.head = node
        self.length += 1

    def insert_tail(self, node):
        """Wstawia node na pozycję tail do listy"""

        if self.length == 0:
            self.head = self.tail = node
            node.next = node
        else:
            node.next = self.head
            self.tail.next = node
            self.tail = node
        self.length += 1

    def search(self, data):
        """Zwraca węzeł, którego zawartość jest równa data.

        Jeżeli taki węzeł nie istnieje, zwraca None.
        """

        if self.length == 0:
            return None
        node = self.head
        while node.data != data:
            if node.next is self.head:
                return None
            node = node.next
        return node

    def remove(self, node):
        """Usuwa węzeł node z listy"""

        if self.is_empty():
            raise ValueError("pusta lista")
        if self.length == 1 and self.head == node:
            self.head = self.tail = None
        elif node == self.head:       # usuwanie heada
            self.tail.next = node.next
            self.head = node.next
        else:
            prev = self.head
            while prev.next != node:
                if prev.next == self.head:  # początek listy - element nie istnieje
                    return
                prev = prev.next
            if node == self.tail:   # usuwanie taila
                self.tail = prev
            prev.next = node.next
        self.length -= 1

    def merge(self, other):
        """Scala dwie listy w czasie O(1)"""

        if other.is_empty():
            return
        if self.is_empty():
            self.head = other.head
        else:
            self.tail.next = other.head
        self.tail = other.tail
        self.tail.next = self.head
        self.length += other.count()
        other.clear()

    def clear(self):
        """Czyści listę"""

        self.head = None
        self.tail = None
        self.length = 0
