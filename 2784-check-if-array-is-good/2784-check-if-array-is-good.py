from collections import Counter

class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = len(nums) - 1
        cnt = Counter(nums)
        
        # 'n' must appear exactly 2 times
        # Every number from 1 to n-1 must appear exactly 1 time
        return cnt[n] == 2 and all(cnt[i] == 1 for i in range(1, n))
