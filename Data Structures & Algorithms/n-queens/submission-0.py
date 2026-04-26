class Solution:
    def _is_safe(self, row, col, board):
        # no Q in the upper rows for same column
        r = row - 1
        while r >= 0:
            if board[r][col] == "Q":
                return False
            r -= 1

        # no Q in the upper left diagonal
        r = row - 1
        c = col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        # no Q in the upper right diagonal
        r = row - 1
        c = col + 1
        while r >= 0 and c < len(board):
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                res = ["".join(item) for item in board]
                result.append(res)
                return

            for col in range(n):
                if self._is_safe(row, col, board):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

        backtrack(0)
        return result