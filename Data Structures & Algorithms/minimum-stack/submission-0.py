class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        length = len(self.stack)
        if length == 0 or val < self.min:
            self.min = val

        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min:
            self.min = min(self.stack)     

    def top(self) -> int:
        length = len(self.stack)
        return self.stack[length - 1]

    def getMin(self) -> int:
        return self.min
