class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        for row in range(ROWS):
            for col in range(row+1, ROWS):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in range(ROWS):
            matrix[row].reverse()



        
        