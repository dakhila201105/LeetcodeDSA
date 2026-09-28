class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        fst = {c: s.find(c) for c in set(s)}
        lst = {c: s.rfind(c) for c in set(s)}
        intervals = []
        
        for c in set(s):
            beg, end = fst[c], lst[c]
            bad, idx = False, beg
            while idx <= end:
                end = max(end, lst[s[idx]])
                if fst[s[idx]] < beg:
                    bad = True
                    break
                idx += 1
            if not bad:
                intervals.append((end, beg))
                
        ans, prev = [], -1
        for end, beg in sorted(intervals):
            if beg > prev:
                ans.append(s[beg:end + 1])
                prev = end
                
        return ans
