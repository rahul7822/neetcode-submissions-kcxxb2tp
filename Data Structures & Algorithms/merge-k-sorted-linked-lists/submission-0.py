# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)][0].val > self.heap[index][0].val:
            parent = self.parent(index)
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def remove(self):
        if len(self.heap) == 0:
            return None
        
        root = self.heap[0]
        value = self.heap.pop()
        if len(self.heap) != 0:
            self.heap[0] = value
            self._heapify_down(0)
        
        return root

    def _heapify_down(self, index):
        left = self.left(index)
        right = self.right(index)
        heap_len = len(self.heap)

        target = index

        if left < heap_len and self.heap[left][0].val < self.heap[target][0].val:
            target = left

        if right < heap_len and self.heap[right][0].val < self.heap[target][0].val:
            target = right

        if target != index:
            self.heap[target], self.heap[index] = self.heap[index], self.heap[target]
            self._heapify_down(target)


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        dummy = ListNode()
        cur = dummy

        min_heap = MinHeap()

        for i in range(len(lists)):
            ll = lists[i]
            while ll:
                min_heap.insert((ll, i)) # ListNode, list_index
                ll = ll.next

        while min_heap.peek():
            root = min_heap.remove()
            node = root[0]
            cur.next = node
            cur = cur.next

        cur.next = None

        return dummy.next




        