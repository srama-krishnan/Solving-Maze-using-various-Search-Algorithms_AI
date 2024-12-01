from abc import ABCMeta, abstractmethod
import itertools
import heapq
import queue  # Use Python 3's queue module

from FibonacciHeap import FibHeap

class PriorityQueue():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __len__(self): pass

    @abstractmethod
    def insert(self, node): pass

    @abstractmethod
    def minimum(self): pass

    @abstractmethod
    def removeminimum(self): pass

    @abstractmethod
    def decreasekey(self, node, new_priority): pass


class FibPQ(PriorityQueue):
    def __init__(self):
        self.heap = FibHeap()

    def __len__(self):
        return self.heap.count

    def insert(self, node):
        self.heap.insert(node)

    def minimum(self):
        return self.heap.minimum()

    def removeminimum(self):
        return self.heap.removeminimum()

    def decreasekey(self, node, new_priority):
        self.heap.decreasekey(node, new_priority)


class HeapPQ(PriorityQueue):
    def __init__(self):
        self.pq = []
        self.removed = set()
        self.count = 0

    def __len__(self):
        return self.count

    def insert(self, node):
        # Store the node as a tuple (key, node) to allow comparison using key
        entry = (node.key, node)
        if entry in self.removed:
            self.removed.discard(entry)
        heapq.heappush(self.pq, entry)
        self.count += 1

    def minimum(self):
        # Peek at the minimum element (key, node) and return the Node object
        priority, item = self.pq[0]
        return item

    def removeminimum(self):
        while True:
            # Pop the minimum element (key, node)
            priority, item = heapq.heappop(self.pq)
            if (priority, item) in self.removed:
                self.removed.discard((priority, item))
            else:
                self.count -= 1
                return item  # Return the Node object

    def remove(self, node):
        # Mark a node as removed using its (key, node) tuple
        entry = (node.key, node)
        if entry not in self.removed:
            self.removed.add(entry)
            self.count -= 1

    def decreasekey(self, node, new_priority):
        # Remove the old node and insert it again with the updated priority
        self.remove(node)
        node.key = new_priority
        self.insert(node)

class QueuePQ(PriorityQueue):
    def __init__(self):
        self.pq = queue.PriorityQueue()  # Replace Queue.PriorityQueue() with queue.PriorityQueue()
        self.removed = set()
        self.count = 0

    def __len__(self):
        return self.count

    def insert(self, node):
        entry = node.key, node.value
        if entry in self.removed:
            self.removed.discard(entry)
        self.pq.put(entry)
        self.count += 1

    def minimum(self):
        (priority, item) = self.pq.get_nowait()
        node = FibHeap.Node(priority, item)
        self.insert(node)
        return node

    def removeminimum(self):
        while True:
            (priority, item) = self.pq.get_nowait()
            if (priority, item) in self.removed:
                self.removed.discard((priority, item))
            else:
                self.count -= 1
                return FibHeap.Node(priority, item)

    def remove(self, node):
        entry = node.key, node.value
        if entry not in self.removed:
            self.removed.add(entry)
            self.count -= 1

    def decreasekey(self, node, new_priority):
        self.remove(node)
        node.key = new_priority
        self.insert(node)
