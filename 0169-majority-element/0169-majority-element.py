class Solution:

  def majorityElement(self, nums: list[int]) -> bool:
    candidate = None
    count = 0

    for num in nums:
      if count == 0:
        candidate = num

      # Increment if it matches the candidate, decrement if it doesn't
      count += 1 if num == candidate else -1

    return candidate
