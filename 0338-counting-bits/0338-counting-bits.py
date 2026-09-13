class Solution:
    def countBits(self, n: int) -> list[int]:
        # Initialize an array of size n + 1 with 0s
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # ans[i] = ans[i // 2] + (1 if i is odd else 0)
            ans[i] = ans[i >> 1] + (i & 1)
            
        return ans
