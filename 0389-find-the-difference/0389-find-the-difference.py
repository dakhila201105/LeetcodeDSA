class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        
        # XOR all characters in string s
        for char in s:
            result ^= ord(char)
            
        # XOR all characters in string t
        for char in t:
            result ^= ord(char)
            
        # The final result is the ASCII value of the unique character
        return chr(result)
