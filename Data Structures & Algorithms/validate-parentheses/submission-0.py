class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            match ch:
                case ")":
                    if stack.pop() != "(":
                        return False
                case "}":
                    if stack.pop() != "{":
                        return False
                case "]":
                    if stack.pop() != "[":
                        return False
                case _:
                    stack.append(ch)
        
        return True

        