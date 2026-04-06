class MinHeap:
    def __init__(self):
        self.heap = []

    def length(self):
        return len(self.heap)

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def peek(self):
        if self.heap:
            return self.heap[0]
        return None

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

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
        heap_len = len(self.heap)

        target = index

        if left < heap_len and self.heap[left] < self.heap[target]:
            target = left

        if right < heap_len and self.heap[right] < self.heap[target]:
            target = right

        if target != index:
            self.heap[target], self.heap[index] = self.heap[index], self.heap[target]
            self._heapify_down(target)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        min_heap = MinHeap()

        for num in nums:
            min_heap.insert(num)

        while min_heap.length() > k:
            min_heap.remove()

        self.min_heap = min_heap
        self.k = k

    def add(self, val: int) -> int:
        self.min_heap.insert(val)
        if self.min_heap.length() > self.k:
            self.min_heap.remove()
        
        return self.min_heap.peek()
