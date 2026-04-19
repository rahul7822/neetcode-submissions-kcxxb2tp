class TimeMap:

    def __init__(self):
        self.store = dict()
        
    def _binary_search(self, items, timestamp):
        l, r = 0, len(items) - 1

        while l <= r:
            m = (l + r) // 2

            mid_right = m + 1 if m < r else r
            mid_left = m - 1 if m > l else l

            if mid_left == mid_right:
                return mid_left

            if items[m][0] == timestamp:
                return m

            if items[m][0] > timestamp:
                r = m - 1
            elif items[m][0] < timestamp and items[mid_right][0] > timestamp:
                return m
            else:
                l = m + 1
            
        return -1


    def set(self, key: str, value: str, timestamp: int) -> None:
        does_key_exist = self.store.get(key, False)
        if does_key_exist == False:
            self.store[key] = [(timestamp, value)]
        else:
            self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        does_key_exist = self.store.get(key, False)
        if does_key_exist == False:
            return ""
        else:
            items_list = self.store.get(key)

            # if items_list[0][0] > timestamp:
            #     return "";

            index = self._binary_search(items_list, timestamp)
            return items_list[index][1]

        
