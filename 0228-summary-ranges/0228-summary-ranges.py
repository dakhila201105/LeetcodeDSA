from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
            
        result = []
        n = len(nums)
        i = 0
        
        while i < n:
            start = nums[i]
            
            # Keep moving forward if the numbers are consecutive
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1
                
            # If the range has more than one element, format with "->"
            if start != nums[i]:
                result.append(f"{start}->{nums[i]}")
            else:
                result.append(str(start))
                
            # Move to the next sequence
            i += 1
            
        return result
