class Node:
    def __init__(self, key = -1, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_ll_head = None
        self.cache_ll_tail = None
        self.mapping = {} # key -> Node

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        else:
            node = self.mapping[key]
            prev_node = node.prev
            next_node = node.next

            if prev_node != None:
                prev_node.next = next_node
            if next_node != None:
                next_node.prev = prev_node

            self.cache_ll_tail.next = node
            return node.val

    def put(self, key: int, value: int) -> None:
        if len(self.mapping) < self.capacity and key not in self.mapping:
            node = Node(key, value)
            if not self.cache_ll_head:
                self.cache_ll_head = node
                self.cache_ll_tail = node
            else:
                self.cache_ll_tail.next = node
                node.prev = self.cache_ll_tail
                self.cache_ll_tail = node
            self.mapping[key] = node
        elif key in self.mapping:
            if self.cache_ll_head != self.cache_ll_tail:
                node = self.mapping[key]
                prev_node = node.prev
                next_node = node.next

                prev_node.next = next_node
                if next_node != None:
                    next_node.prev = prev_node
                
                node.next = None
                self.cache_ll_tail.next = node
        else:
            head_node = self.cache_ll_head
            head_key = head_node.key
            self.cache_ll_head = self.cache_ll_head.next
            del self.mapping[head_key]
