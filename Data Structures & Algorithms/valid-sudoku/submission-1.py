class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        s1_dict = {}
        s2_dict = {}
        s3_dict = {}
        s4_dict = {}
        s5_dict = {}
        s6_dict = {}
        s7_dict = {}
        s8_dict = {}
        s9_dict = {}

        for i in range(9):
            r_dict = {}
            c_dict = {}
            for j in range(9):
                if board[i][j] in r_dict or board[j][i] in c_dict:
                    return False
                else:
                    if board[i][j] != ".":
                        r_dict[board[i][j]] = 1
                    if board[j][i] != ".":
                        c_dict[board[j][i]] = 1

                # 1st
                if i < 3 and j < 3:
                    if board[i][j] in s1_dict:
                        return False
                    elif board[i][j] != ".":
                        s1_dict[board[i][j]] = 1

                # 2nd
                if i < 3 and (j >= 3 and j < 6):
                    if board[i][j] in s2_dict:
                        return False
                    elif board[i][j] != ".":
                        s2_dict[board[i][j]] = 1

                # 3rd
                if i < 3 and (j >= 6 and j < 9):
                    if board[i][j] in s3_dict:
                        return False
                    elif board[i][j] != ".":
                        s3_dict[board[i][j]] = 1

                # 4th
                if (i >= 3 and i < 6) and j < 3:
                    if board[i][j] in s4_dict:
                        return False
                    elif board[i][j] != ".":
                        s4_dict[board[i][j]] = 1

                # 5th
                if (i >= 3 and i < 6) and (j >= 3 and j < 6):
                    if board[i][j] in s5_dict:
                        return False
                    elif board[i][j] != ".":
                        s5_dict[board[i][j]] = 1

                # 6th
                if (i >= 3 and i < 6) and (j >= 6 and j < 9):
                    if board[i][j] in s6_dict:
                        return False
                    elif board[i][j] != ".":
                        s6_dict[board[i][j]] = 1

                # 7th
                if (i >= 6 and i < 9) and j < 3:
                    if board[i][j] in s7_dict:
                        return False
                    elif board[i][j] != ".":
                        s7_dict[board[i][j]] = 1

                # 8th
                if (i >= 6 and i < 9) and (j >= 3 and j < 6):
                    if board[i][j] in s8_dict:
                        return False
                    elif board[i][j] != ".":
                        s8_dict[board[i][j]] = 1

                # 9th
                if (i >= 6 and i < 9) and (j >= 6 and j < 9):
                    if board[i][j] in s9_dict:
                        return False
                    elif board[i][j] != ".":
                        s9_dict[board[i][j]] = 1

        return True

        