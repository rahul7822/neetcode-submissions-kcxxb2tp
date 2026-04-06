class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in temperatures]

        stack = []
        for i, temperature in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((temperature, i))
            else:
                while len(stack) > 0 and stack[-1][0] < temperature:
                    top = stack[-1]
                    result[top[1]] = i - top[1]
                    stack.pop()
                    
                stack.append((temperature, i))

        
        return result

        