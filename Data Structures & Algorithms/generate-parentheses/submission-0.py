class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(b_str, open_c, close_c):
            if len(b_str) == 2 * n:
                result.append(b_str)
                return

            if open_c < n:
                backtrack(b_str + "(", open_c + 1, close_c)

            if close_c < open_c:
                backtrack(b_str + ")", open_c, close_c + 1)

        backtrack("", 0, 0)
        return result