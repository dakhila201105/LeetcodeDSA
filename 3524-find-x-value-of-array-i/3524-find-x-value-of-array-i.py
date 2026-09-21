class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        # ans[x] will store the number of subarrays whose product % k == x
        ans = [0] * k
        
        # dp[r] tracks the count of valid subarrays ending at the 
        # previous index whose cumulative product % k == r
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            
            # 1. Start a new subarray consisting only of the current element
            new_dp[num_mod] = 1
            
            # 2. Extend all valid subarrays that ended at the previous index
            for i in range(k):
                if dp[i] > 0:
                    new_mod = (i * num_mod) % k
                    new_dp[new_mod] += dp[i]
            
            # 3. Accumulate the counts discovered at the current index into the total
            for i in range(k):
                ans[i] += new_dp[i]
                
            # Roll over the DP tracker for the next iteration
            dp = new_dp
            
        return ans
