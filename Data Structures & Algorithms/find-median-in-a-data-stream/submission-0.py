class MinHeap:
    def __init__(self):
        self.heap = []

    def length(self):
        return len(self.heap)
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        return None

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1
    
    def right(self, index):
        return 2 * index + 2

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(self.length() - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            parent = self.parent(index)
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
    
    def remove(self):
        if self.heap:
            root = self.heap[0]
            val = self.heap.pop()
            if self.heap:
                self.heap[0] = val
                self._heapify_down(0)
            return root
        return None

    def _heapify_down(self, index):
        left = self.left(index)
        right = self.right(index)
        heap_len = self.length()

        largest = index
        if left < heap_len and self.heap[largest] > self.heap[left]:
            largest = left
        if right < heap_len and self.heap[largest] > self.heap[right]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest) 

class MaxHeap:
    def __init__(self):
        self.heap = []

    def length(self):
        return len(self.heap)

    def peek(self):
        if self.heap:
            return self.heap[0]
        return None

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1
    
    def right(self, index):
        return 2 * index + 2

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(self.length() - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            parent = self.parent(index)
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
    
    def remove(self):
        if self.heap:
            root = self.heap[0]
            val = self.heap.pop()
            if self.heap:
                self.heap[0] = val
                self._heapify_down(0)
            return root
        return None

    def _heapify_down(self, index):
        left = self.left(index)
        right = self.right(index)
        heap_len = self.length()

        smallest = index
        if left < heap_len and self.heap[smallest] < self.heap[left]:
            smallest = left
        if right < heap_len and self.heap[smallest] < self.heap[right]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest) 

class MedianFinder:

    def __init__(self):
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()
        self.total = 0

    def addNum(self, num: int) -> None:
        self.max_heap.insert(num)

        if self.max_heap.length() - self.min_heap.length() > 1:
            max_root = self.max_heap.remove()
            self.min_heap.insert(max_root)

        while self.min_heap.peek() and self.max_heap.peek() and self.min_heap.peek() < self.max_heap.peek():
            max_root = self.max_heap.remove()
            self.min_heap.insert(max_root)
        
        self.total += 1

    def findMedian(self) -> float:
        if self.total % 2 == 0:
            return float((self.max_heap.peek() + self.min_heap.peek()) / 2)
        else:
            if self.max_heap.length() > self.min_heap.length():
                return float(self.max_heap.peek())
            else:
                return float(self.min_heap.peek())

        
        