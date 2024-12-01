class FibHeap:

    #### Node Class ####
    class Node:
        def __init__(self, key, value):
            # key value degree mark / prev next child parent
            self.key = key
            self.value = value
            self.degree = 0
            self.mark = False
            self.parent = self.child = None
            self.previous = self.next = self

        def issingle(self):
            return self == self.next

        def insert(self, node):
            if node is None:
                return

            self.next.previous = node.previous
            node.previous.next = self.next
            self.next = node
            node.previous = self

        def remove(self):
            self.previous.next = self.next
            self.next.previous = self.previous
            self.next = self.previous = self

        def addchild(self, node):
            if self.child is None:
                self.child = node
            else:
                self.child.insert(node)
            node.parent = self
            node.mark = False
            self.degree += 1

        def removechild(self, node):
            if node.parent != self:
                raise AssertionError("Cannot remove child from a node that is not its parent")

            if node.issingle():
                if self.child != node:
                    raise AssertionError("Cannot remove a node that is not a child")
                self.child = None
            else:
                if self.child == node:
                    self.child = node.next
                node.remove()

            node.parent = None
            node.mark = False
            self.degree -= 1

        # Add comparison method for compatibility with heapq
        def __lt__(self, other):
            return self.key < other.key

    #### End of Node Class ####

    def __init__(self):
        self.minnode = None
        self.count = 0
        self.maxdegree = 0

    def isempty(self):
        return self.count == 0

    def insert(self, node):
        self.count += 1
        self._insertnode(node)

    def _insertnode(self, node):
        if self.minnode is None:
            self.minnode = node
        else:
            self.minnode.insert(node)
            if node.key < self.minnode.key:
                self.minnode = node

    def minimum(self):
        if self.minnode is None:
            raise AssertionError("Cannot return minimum of empty heap")
        return self.minnode

    def merge(self, heap):
        if heap.minnode is None:
            return

        self.minnode.insert(heap.minnode)
        if self.minnode is None or (heap.minnode is not None and heap.minnode.key < self.minnode.key):
            self.minnode = heap.minnode
        self.count += heap.count

    def removeminimum(self):
        if self.minnode is None:
            raise AssertionError("Cannot remove from an empty heap")

        removed_node = self.minnode
        self.count -= 1

        # Assign all old root children as new roots
        if self.minnode.child is not None:
            c = self.minnode.child
            while True:
                c.parent = None
                c = c.next
                if c == self.minnode.child:
                    break
            self.minnode.child = None
            self.minnode.insert(c)

        # If we have removed the last key
        if self.minnode.next == self.minnode:
            if self.count != 0:
                raise AssertionError("Heap error: Expected 0 keys, count is " + str(self.count))
            self.minnode = None
            return removed_node

        # Merge any roots with the same degree
        logsize = 100
        degreeroots = [None] * logsize
        self.maxdegree = 0
        currentpointer = self.minnode.next

        while True:
            currentdegree = currentpointer.degree
            current = currentpointer
            currentpointer = currentpointer.next
            while degreeroots[currentdegree] is not None:
                other = degreeroots[currentdegree]
                # Swap if required
                if current.key > other.key:
                    temp = other
                    other = current
                    current = temp

                other.remove()
                current.addchild(other)
                degreeroots[currentdegree] = None
                currentdegree += 1

            degreeroots[currentdegree] = current
            if currentpointer == self.minnode:
                break

        # Remove current root and find new minnode
        self.minnode = None
        newmaxdegree = 0
        for d in range(logsize):
            if degreeroots[d] is not None:
                degreeroots[d].next = degreeroots[d].previous = degreeroots[d]
                self._insertnode(degreeroots[d])
                if d > newmaxdegree:
                    newmaxdegree = d

        self.maxdegree = newmaxdegree
        return removed_node

    def decreasekey(self, node, newkey):
        if newkey > node.key:
            raise AssertionError("Cannot decrease a key to a greater value")
        elif newkey == node.key:
            return

        node.key = newkey
        parent = node.parent

        if parent is None:
            if newkey < self.minnode.key:
                self.minnode = node
            return
        elif parent.key <= newkey:
            return

        while True:
            parent.removechild(node)
            self._insertnode(node)

            if parent.parent is None:
                break
            elif not parent.mark:
                parent.mark = True
                break
            else:
                node = parent
                parent = parent.parent
                continue
