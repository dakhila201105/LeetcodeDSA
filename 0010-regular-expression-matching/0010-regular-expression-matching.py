class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Cache to store results of (i, j) subproblems
        memo = {}
        
        def dfs(i: int, j: int) -> bool:
            # Check cache first
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base Case: If we consumed the entire pattern
            if j == len(p):
                return i == len(s)
            
            # Check if the current characters match (handling the '.' wildcard)
            current_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # Case 1: The next character in pattern is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Decision 1: Skip the '*' and its preceding element (match 0 times)
                # Decision 2: Use the '*' if there's a current match (move pointer in string 's')
                res = dfs(i, j + 2) or (current_match and dfs(i + 1, j))
            
            # Case 2: Standard matching without '*'
            else:
                res = current_match and dfs(i + 1, j + 1)
                
            memo[(i, j)] = res
            return res

        return dfs(0, 0)
