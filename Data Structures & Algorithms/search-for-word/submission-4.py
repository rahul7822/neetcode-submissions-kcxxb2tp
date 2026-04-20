class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        word_len = len(word)

        def does_exist(r, c, i):
            if i == word_len:
                return True

            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False

            tmp = board[r][c]
            board[r][c] = "#"

            found = (does_exist(r, c + 1, i + 1) or does_exist(r + 1, c, i + 1) or does_exist(r - 1, c, i + 1) or does_exist(r, c - 1, i + 1))

            board[r][c] = tmp

            return found

        for i in range(rows):
            for j in range(cols):
                if does_exist(i, j, 0):
                    return True

        return False