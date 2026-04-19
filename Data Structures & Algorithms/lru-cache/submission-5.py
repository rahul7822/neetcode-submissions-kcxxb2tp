class Node:
    def __init__(self, key = -1, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mapping = {}
        self.head = None
        self.tail = None

    def _update_list(self, node, mode):
        # put node at the end of ll
        match mode:
            case "update": # put existing node at the tail
                if self.head != self.tail:
                    if node == self.head: # node is head
                        self.head = self.head.next
                        self.tail.next = node
                        self.tail = self.tail.next
                    elif node != self.tail:
                        prev_node = node.prev
                        next_node = node.next
                        prev_node.next = next_node
                        next_node.prev = prev_node

                        self.tail.next = node
                        self.tail = self.tail.next
            case "insert": # put new node at the tail
                if self.head == None:
                    self.head = self.tail = node
                else:
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = self.tail.next
    
    def _remove_lru(self):
        # move forward the head, delete from mapping
        head_node = self.head
        self.head = self.head.next
        del self.mapping[head_node.key]

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        else:
            # get the val and put the node at the tail of ll
            node = self.mapping[key]
            self._update_list(node, "update")
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            # update the node and put the node at the tail of ll
            node = self.mapping[key]
            node.val = value
            self._update_list(node, "update")
        else:
            node = Node(key, value)
            if len(self.mapping) == self.cap:
                self._remove_lru()
                
            self._update_list(node, "insert")
            self.mapping[key] = node