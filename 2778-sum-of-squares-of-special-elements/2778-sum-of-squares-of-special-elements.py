class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        return sum(num**2 for i, num in enumerate(nums) if n % (i + 1) == 0)
