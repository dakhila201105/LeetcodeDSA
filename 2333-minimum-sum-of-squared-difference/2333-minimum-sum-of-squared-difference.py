
class Solution:
    def minSumSquareDiff(
        self,
        nums1: list[int],
        nums2: list[int],
        k1: int,
        k2: int
    ) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        max_diff = max(diffs)
        freq = [0] * (max_diff + 1)

        for d in diffs:
            freq[d] += 1

        for d in range(max_diff, 0, -1):
            if k == 0:
                break

            count = freq[d]
            operations = min(k, count)

            freq[d] -= operations
            freq[d - 1] += operations
            k -= operations

        return sum(d * d * count for d, count in enumerate(freq))
