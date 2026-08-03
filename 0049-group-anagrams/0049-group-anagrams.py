from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())
