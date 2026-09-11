from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)    # key: group of chars, val: list of anagrams
        for s in strs:
            anagrams["".join(sorted(list(s)))].append(s)
        return list(anagrams.values())
        
## Hashmap Solution
# Time: O(n * k log(k))
# Space: O(n * k)
# - where n = number of strings in the input
#         m = max. length of a string in the input