class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

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
        
        box_dict = {}
        for i in range(3):
            for j in range(3):
                if board[i][j] in box_dict:
                    return False
                elif board[i][j] != ".":
                    box_dict[board[i][j]] = 1

        #1. ########
        box_dict = {}
        for i in range(3, 6):
            for j in range(3):
                if board[i][j] in box_dict:
                    return False
                elif board[i][j] != ".":
                    box_dict[board[i][j]] = 1

        box_dict = {}
        for i in range(6, 9):
            for j in range(3):
                if board[i][j] in box_dict:
                    return False
                elif board[i][j] != ".":
                    box_dict[board[i][j]] = 1
        #2. #######
        box_dict = {}
        for i in range(3):
            for j in range(3, 6):
                if board[i][j] in box_dict:
                    return False
                elif board[i][j] != ".":
                    box_dict[board[i][j]] = 1

        box_dict = {}
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j] in box_dict:
                    return False
                elif board[i][j] != ".":
                    box_dict[board[i][j]] = 1

        box_dict = {}
        for i in range(6, 9):
            for j in range(3, 6):
                if board[i][j] in box_dict:
                    return False
                elif board[i][j] != ".":
                    box_dict[board[i][j]] = 1
        #3. ########
        box_dict = {}
        for i in range(3):
            for j in range(6, 9):
                if board[i][j] in box_dict:
                    return False
                elif board[i][j] != ".":
                    box_dict[board[i][j]] = 1

        box_dict = {}
        for i in range(3, 6):
            for j in range(6, 9):
                if board[i][j] in box_dict:
                    return False
                elif board[i][j] != ".":
                    box_dict[board[i][j]] = 1

        box_dict = {}
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j] in box_dict:
                    return False
                elif board[i][j] != ".":
                    box_dict[board[i][j]] = 1
        

        return True

        