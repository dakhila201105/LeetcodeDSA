class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        sq_nums = [x * x for x in nums]
        sq_nums.sort()
        n = len(nums)
        mid = n // 2
        return sum(sq_nums[mid:]) - sum(sq_nums[:mid])
