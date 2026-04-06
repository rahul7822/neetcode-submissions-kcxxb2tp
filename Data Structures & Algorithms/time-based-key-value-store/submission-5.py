class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp, value)]
        else:
            self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        else:
            items = self.store[key]

            result = ""
            l, r = 0, len(items) - 1

            while l <= r:
                m = (l + r) // 2

                if items[m][0] > timestamp:
                    r =  m - 1
                else:
                    result = items[m][1]
                    l = m + 1
            
            return result

        
