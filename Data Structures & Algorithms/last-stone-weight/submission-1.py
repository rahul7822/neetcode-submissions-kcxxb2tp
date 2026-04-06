class MaxHeap:
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

        target = index

        if left < heap_len and self.heap[left] > self.heap[target]:
            target = left
        if right < heap_len and self.heap[right] > self.heap[target]:
            target = right

        if index != target:
            self.heap[index], self.heap[target] = self.heap[target], self.heap[index]
            self._heapify_down(target)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = MaxHeap()
        for weight in stones:
            max_heap.insert(weight)

        while max_heap.length() > 1:
            x = max_heap.remove()
            y = max_heap.remove()

            if x != y:
                max_heap.insert(abs(x - y))

        result = max_heap.remove()
        if result == None:
            return 0
        return result