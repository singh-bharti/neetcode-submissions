class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        rowZero = False
        colZero = False

        for j in range(COLS):
            if matrix[0][j] == 0:
                rowZero = True
        
        for i in range(ROWS):
            if matrix[i][0] == 0:
                colZero = True
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # Zero rows
        for i in range(1, ROWS):
            if matrix[i][0] == 0:
                for j in range(1, COLS):
                    matrix[i][j] = 0
        # Zero columns
        for j in range(1, COLS):
            if matrix[0][j] == 0:
                for i in range(1, ROWS):
                    matrix[i][j] = 0
        # Zero first row
        if rowZero:
            for j in range(COLS):
                matrix[0][j] = 0

        # Zero first column
        if colZero:
            for i in range(ROWS):
                matrix[i][0] = 0

        
        