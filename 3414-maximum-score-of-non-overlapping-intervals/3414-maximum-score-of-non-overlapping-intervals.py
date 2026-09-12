from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # 1. Store intervals with original indices, sorted by START time
        A = sorted((s, e, w, i) for i, (s, e, w) in enumerate(intervals))
        n = len(A)
        
        # Extract start times for binary searching later
        starts = [x[0] for x in A]
        
        # 2. DP table structure: dp[i][k] stores (max_weight, index_list)
        # Going from right to left (from n down to 0)
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            start, end, weight, idx = A[i]
            
            # Find the next interval that starts AFTER the current interval ends
            nxt = bisect_left(starts, end + 1)
            
            for k in range(1, 5):
                # Scenario A: Skip the current interval
                w1, idx1 = dp[i + 1][k]
                
                # Scenario B: Take the current interval
                w2, idx2 = dp[nxt][k - 1]
                w2 = w2 + weight
                idx2_combined = [idx] + idx2
                
                # Compare decisions
                if w1 > w2:
                    dp[i][k] = (w1, idx1)
                elif w2 > w1:
                    dp[i][k] = (w2, sorted(idx2_combined))
                else:
                    # Tie-breaker: choose the lexicographically smaller sorted index list
                    sorted_combined = sorted(idx2_combined)
                    if not idx1 or (sorted_combined < idx1):
                        dp[i][k] = (w2, sorted_combined)
                    else:
                        dp[i][k] = (w1, idx1)
                        
        # Return the indices array from the optimal choice at the beginning
        return dp[0][4][1]
