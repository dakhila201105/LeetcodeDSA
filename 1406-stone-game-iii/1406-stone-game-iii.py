class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n+1)  # dp[n] = 0
        
        for i in range(n-1, -1, -1):
            take, best = 0, float('-inf')
            for k in range(3):
                if i + k < n:
                    take += stoneValue[i+k]
                    best = max(best, take - dp[i+k+1])
            dp[i] = best
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
