from collections import deque

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
        while index > 0 and self.heap[self.parent(index)].freq < self.heap[index].freq:
            parent = self.parent(index)
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def remove(self):
        if self.heap:
            root = self.heap[0]
            last = self.heap.pop()
            if self.heap:
                self.heap[0] = last
                self._heapify_down(0)
            return root
        return None
    
    def _heapify_down(self, index):
        left = self.left(index)
        right = self.right(index)
        heap_len = self.length()

        maximum = index
        if left < heap_len and self.heap[left].freq > self.heap[maximum].freq:
            maximum = left
        if right < heap_len and self.heap[right].freq > self.heap[maximum].freq:
            maximum = right

        if maximum != index:
            self.heap[index], self.heap[maximum] = self.heap[maximum], self.heap[index]
            self._heapify_down(maximum)

class Task:
    def __init__(self, task, freq, n):
        self.task = task
        self.freq = freq
        self.n = n

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = MaxHeap()
        cooldown_queue = deque()
        tasks_freq = {}
        cycles = 0

        for task in tasks:
            tasks_freq[task] = tasks_freq.get(task, 0) + 1

        for task, freq in tasks_freq.items():
            max_heap.insert(Task(task, freq, n))

        while len(cooldown_queue) != 0 or max_heap.length() != 0:
            task_node = max_heap.remove()
            if task_node != None:
                task_node.freq -= 1
                if task_node.freq > 0:
                    cooldown_queue.append(task_node)

            push_to_heap = False
            for i, item in enumerate(cooldown_queue):
                if item.n <= 0:
                    push_to_heap = True
                item.n -= 1
            
            if index_to_delete:
                task_node = cooldown_queue.popleft()
                if task_node.freq > 0:
                    task_node.n = n
                    max_heap.insert(task_node)
            
            cycles += 1


        return cycles