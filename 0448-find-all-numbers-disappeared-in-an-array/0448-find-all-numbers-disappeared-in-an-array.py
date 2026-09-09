class Solution:

  def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    # Step 1: Mark visited indices by negating the values
    for num in nums:
      index = abs(num) - 1
      if nums[index] > 0:
        nums[index] = -nums[index]

    # Step 2: Collect all indices that remain positive
    result = []
    for i in range(len(nums)):
      if nums[i] > 0:
        result.append(i + 1)

    return result
