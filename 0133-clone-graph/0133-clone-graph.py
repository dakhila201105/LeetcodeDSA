"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        old_to_new = {}
        
        def dfs(current):
            if current in old_to_new:
                return old_to_new[current]
            
            copy = Node(current.val)
            old_to_new[current] = copy
            
            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
        
        return dfs(node)