class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        def backtrack(i, p):
            if i == len(digits):
                res.append("".join(p))
                return
                
            possible_letters = phone_map[digits[i]]
            for letter in possible_letters:
                p.append(letter)
                backtrack(i + 1, p)
                p.pop()
                
        backtrack(0, [])
        return res
