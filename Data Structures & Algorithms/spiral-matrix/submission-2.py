class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            for col in range(left, right+1):
                res.append(matrix[top][col])
            top += 1

            for col in range(top, bottom + 1):
                res.append(matrix[col][right])
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            if left <= right:
                for col in range(bottom, top - 1, -1):
                    res.append(matrix[col][left])
                left += 1

        return res

