from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())
        