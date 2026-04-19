class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(left - right)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    dr = stack.pop()
                    nr = stack.pop()
                    stack.append(round(nr / dr))
                case _:
                    stack.append(int(token))

        return stack[0]