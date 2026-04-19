class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            match ch:
                case ")":
                    if len(stack) > 0 and stack.pop() != "(":
                        return False
                case "}":
                    if len(stack) > 0 and stack.pop() != "{":
                        return False
                case "]":
                    if len(stack) > 0 and stack.pop() != "[":
                        return False
                case _:
                    stack.append(ch)
        
        if len(stack) > 0:
            return False
        else:
            return True

        