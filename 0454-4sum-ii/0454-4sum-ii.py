from collections import Counter


class Solution:

  def fourSumCount(
      self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
  ) -> int:
    # Store the frequency of all sums from the first two arrays
    sum_counts = Counter(a + b for a in nums1 for b in nums2)

    # For each pair from the last two arrays, add the matching complement count
    total_tuples = sum(sum_counts[-(c + d)] for c in nums3 for d in nums4)

    return total_tuples
