class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.counter = 0

    def get(self, key: int) -> int:
        res = self.cache.get(key, -1)
        value = -1 if res == -1 else res[0]
        if value == -1:
            return value
        #update the used key in cache
        self.put(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity or key in self.cache:
            self.cache[key] = (value, self.counter)
        else:
            # delete the LRU entry first
            target_key = None
            least_accessed_key = float("inf")
            for lru_key, lru_value in self.cache.items():
                if lru_value[1] < least_accessed_key:
                    least_accessed_key = lru_value[1]
                    target_key = lru_key

            del self.cache[target_key]
            self.cache[key] = (value, self.counter)

        self.counter += 1
        
        return None
