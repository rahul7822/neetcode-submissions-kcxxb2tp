class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        length = len(self.stack)
        self.stack.append(val)
        if length == 0:
            self.min_stack.append(val)
        else:
            cur_min = min(val, self.min_stack[-1])
            self.min_stack.append(cur_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        length = len(self.stack)
        return self.stack[length - 1]

    def getMin(self) -> int:
        return self.min_stack[-1]
