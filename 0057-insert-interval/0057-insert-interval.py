class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # Phase 1: Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        # Phase 2: Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Append the merged new interval
        result.append(newInterval)
        
        # Phase 3: Add all remaining intervals that start after the new interval ends
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result
