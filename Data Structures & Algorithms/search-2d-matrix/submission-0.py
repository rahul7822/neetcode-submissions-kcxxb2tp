class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # rows
        n = len(matrix[0]) # columns

        # find the particular row where the target will lie
        rowIndex = self.findRow(m, n, matrix, target)

        if rowIndex == -1:
            return False

        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2

            if target == matrix[rowIndex][m]:
                return True
            elif target > matrix[rowIndex][m]:
                l = m + 1
            else:
                r = m - 1
        
        return False


    def findRow(self, m, n, matrix, target):
        t, b = 0, m - 1

        while t <= b:
            m = (t + b) // 2

            if target >= matrix[m][0] and target <= matrix[m][n-1]:
                return m
            elif target < matrix[m][0]:
                b = m - 1
            else:
                t = m + 1

        return -1




        