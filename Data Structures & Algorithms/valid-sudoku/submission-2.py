class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == '.':
                    continue
                box = (r//3, c//3)

                if (value in row[r] or value in col[c] or value in boxes[box]):
                    return False
                row[r].add(value)
                col[c].add(value)
                boxes[box].add(value)
        return True
        