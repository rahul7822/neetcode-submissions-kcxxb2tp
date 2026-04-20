class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        word_len = len(word)
        visited = set()

        def does_exist(r, c, i):
            if i == word_len:
                return True
            if i >= word_len or r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or board[r][c] != word[i]:
                return False
            visited.add((r, c))
            result = (does_exist(r, c + 1, i + 1) or does_exist(r + 1, c, i + 1) or does_exist(r - 1, c, i + 1) or does_exist(r, c - 1, i + 1))
            visited.remove((r, c))
            return result

        for i in range(rows):
            for j in range(cols):
                visited = set()
                if does_exist(i, j, 0):
                    return True

        return False