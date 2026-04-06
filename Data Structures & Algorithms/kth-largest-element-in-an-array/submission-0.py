class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def length(self):
        return len(self.heap)

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
            last_val = self.heap.pop()
            if self.heap:
                self.heap[0] = last_val
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

        if target != index:
            self.heap[target], self.heap[index] = self.heap[index], self.heap[target]
            self._heapify_down(target)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = MaxHeap()

        for num in nums:
            max_heap.insert(num)

        while k > 1:
            max_heap.remove()
            k -= 1

        return max_heap.remove()


        