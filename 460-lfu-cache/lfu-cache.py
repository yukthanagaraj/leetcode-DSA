class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop(self):
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0

        self.nodes = {}   # key -> node
        self.freq = {}    # frequency -> DLL


    def update(self, node):
        oldFreq = node.freq

        self.freq[oldFreq].remove(node)

        if oldFreq == self.minFreq and self.freq[oldFreq].size == 0:
            self.minFreq += 1

        node.freq += 1

        if node.freq not in self.freq:
            self.freq[node.freq] = DoublyLinkedList()

        self.freq[node.freq].add(node)


    def get(self, key):
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.update(node)

        return node.value


    def put(self, key, value):
        if self.capacity == 0:
            return

        # Update existing key
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self.update(node)
            return

        # Remove LFU if full
        if self.size == self.capacity:
            removed = self.freq[self.minFreq].pop()
            del self.nodes[removed.key]
            self.size -= 1

        # Insert new node
        node = Node(key, value)

        self.nodes[key] = node

        if 1 not in self.freq:
            self.freq[1] = DoublyLinkedList()

        self.freq[1].add(node)

        self.minFreq = 1
        self.size += 1