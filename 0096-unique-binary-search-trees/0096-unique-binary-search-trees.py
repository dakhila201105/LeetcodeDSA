class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] will store the number of unique BSTs that can be formed with i nodes
        p = [0] * (n + 1)
        
        # Base cases: 
        # 1 way to make a BST with 0 nodes (empty tree)
        # 1 way to make a BST with 1 node
        p[0] = 1
        p[1] = 1
        
        # Fill the DP table sequentially up to n nodes
        for i in range(2, n + 1):
            # Try placing each node 'j' as the root of the tree
            for j in range(1, i + 1):
                # Left subtree has (j - 1) nodes, right subtree has (i - j) nodes
                p[i] += p[j - 1] * p[i - j]
                
        return p[n]
