digit_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "qprs",
    "8": "tuv",
    "9": "wxyz",
    }

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        result = []

        def backtrack(index, cur_str):
            if len(cur_str) == len(digits):
                result.append(cur_str)
                return

            letters = digit_map[digits[index]]
            for ch in letters:
                backtrack(index + 1, cur_str + ch)

        backtrack(0, "")

        return result

