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
            
        result = [""]
        for digit in digits:
            letters = digit_map[digit]
            new_result = []
            for letter in letters:
                for res in result:
                    new_result.append(res + letter)
            result = new_result

        return result

