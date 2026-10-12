"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clones = {}
        def dfs(original):
            # Return the clone if already created
            if original in clones:
                return clones[original]

            # Create and store the clone first
            copy = Node(original.val)
            clones[original] = copy

            # Clone all neighbors
            for neighbor in original.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node) if node else None
        