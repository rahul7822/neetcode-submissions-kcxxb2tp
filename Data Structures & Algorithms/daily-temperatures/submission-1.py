class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                top = stack[-1]
                result[top[1]] = i - top[1]
                stack.pop()

            stack.append((t, i))

        return result

        