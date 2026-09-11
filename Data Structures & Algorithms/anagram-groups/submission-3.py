from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)    # key: group of chars, val: list of anagrams
        for s in strs:
            anagrams["".join(sorted(list(s)))].append(s)
        
        res = []
        for key, val in anagrams.items():
            res.append(val)
        
        return res