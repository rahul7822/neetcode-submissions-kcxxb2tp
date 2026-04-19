import math

class MaxHeap:
    def __init__(self):
        self.heap = [] # distance, point

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
        self._heapify_up(self.length() - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)][0] < self.heap[index][0]:
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

        if left < heap_len and self.heap[left][0] > self.heap[target][0]:
            target = left
        if right < heap_len and self.heap[right][0] > self.heap[target][0]:
            target = right

        if target != index:
            self.heap[target], self.heap[index] = self.heap[index], self.heap[target]
            self._heapify_down(target)

class Solution:
    def distance(self, point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = MaxHeap()

        for i in range(0, k):
            max_heap.insert((self.distance(points[i]), points[i]))

        for i in range(k, len(points)):
            dist = self.distance(points[i])
            if max_heap.peek()[0] > dist:
                max_heap.insert(dist, points[i])

        result = list(map(lambda x : x[1], max_heap.heap))
        return result