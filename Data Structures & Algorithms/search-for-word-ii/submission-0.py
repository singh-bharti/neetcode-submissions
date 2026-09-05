class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        #add in trie
        for word in words:
            cur = root

            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.word = word

        result = []
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, node):
            char = board[r][c]

            if char not in node.children:
                return 
            next_node = node.children[char]

            #found a complete word
            if next_node.word:
                result.append(next_node.word) 
                next_node.word = None
            
            #mark the cell as visted
            board[r][c] = '#'

            #explore four directions
            if r > 0 and board[r - 1][c] != '#':
                dfs(r - 1, c, next_node)
            if r < rows - 1 and board[r + 1][c] != '#':
                dfs(r + 1, c, next_node)
            if c > 0 and board[r][c - 1] != '#':
                dfs(r, c - 1, next_node)
            if c < cols - 1 and board[r][c + 1] != '#':
                dfs(r, c + 1, next_node)

            board[r][c] = char

            #remove empty Trie
            if not next_node.children and next_node.word is None:
                del node.children[char]
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return result


        