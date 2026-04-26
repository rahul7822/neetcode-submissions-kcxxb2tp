class Solution:
    def is_palindrom(self, string):
        i, j = 0, len(string) - 1

        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(index, path):
            if index == len(s):
                result.append(path.copy())
                return

            for i in range(index, len(s)):
                substring = s[index : i + 1]
                if self.is_palindrom(substring):
                    path.append(substring)
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return result