class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        s1_set = set()
        s2_set = set()
        s3_set = set()
        s4_set = set()
        s5_set = set()
        s6_set = set()
        s7_set = set()
        s8_set = set()
        s9_set = set()

        for i in range(9):
            r_set = set()
            c_set = set()
            for j in range(9):
                if board[i][j] in r_set or board[j][i] in c_set:
                    return False
                else:
                    if board[i][j] != ".":
                        r_set.add(board[i][j])
                    if board[j][i] != ".":
                        c_set.add(board[j][i])

                # 1st
                if i < 3 and j < 3:
                    if board[i][j] in s1_set:
                        return False
                    elif board[i][j] != ".":
                        s1_set.add(board[i][j])

                # 2nd
                if i < 3 and (j >= 3 and j < 6):
                    if board[i][j] in s2_set:
                        return False
                    elif board[i][j] != ".":
                        s2_set.add(board[i][j])

                # 3rd
                if i < 3 and (j >= 6 and j < 9):
                    if board[i][j] in s3_set:
                        return False
                    elif board[i][j] != ".":
                        s3_set.add(board[i][j])

                # 4th
                if (i >= 3 and i < 6) and j < 3:
                    if board[i][j] in s4_set:
                        return False
                    elif board[i][j] != ".":
                        s4_set.add(board[i][j])

                # 5th
                if (i >= 3 and i < 6) and (j >= 3 and j < 6):
                    if board[i][j] in s5_set:
                        return False
                    elif board[i][j] != ".":
                        s5_set.add(board[i][j])

                # 6th
                if (i >= 3 and i < 6) and (j >= 6 and j < 9):
                    if board[i][j] in s6_set:
                        return False
                    elif board[i][j] != ".":
                        s6_set.add(board[i][j])

                # 7th
                if (i >= 6 and i < 9) and j < 3:
                    if board[i][j] in s7_set:
                        return False
                    elif board[i][j] != ".":
                        s7_set.add(board[i][j])

                # 8th
                if (i >= 6 and i < 9) and (j >= 3 and j < 6):
                    if board[i][j] in s8_set:
                        return False
                    elif board[i][j] != ".":
                        s8_set.add(board[i][j])

                # 9th
                if (i >= 6 and i < 9) and (j >= 6 and j < 9):
                    if board[i][j] in s9_set:
                        return False
                    elif board[i][j] != ".":
                        s9_set.add(board[i][j])

        return True

        