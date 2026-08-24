class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(index, row, col):
            if index == len(word):
                return True
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                board[row][col] != word[index]
            ):
                return False
        
            temp = board[row][col]
            board[row][col] = '#'

            found = (
                dfs(index + 1, row + 1, col) or
                dfs(index + 1, row - 1, col) or
                dfs(index + 1, row, col + 1) or
                dfs(index + 1, row, col - 1)
            )

            board[row][col] = temp

            return found
            
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(0, row, col):
                    return True
        return False

             