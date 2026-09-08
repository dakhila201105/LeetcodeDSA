class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # A power of two must be strictly greater than 0, 
        # and it must have exactly one bit set to 1 in binary.
        return n > 0 and (n & (n - 1)) == 0
