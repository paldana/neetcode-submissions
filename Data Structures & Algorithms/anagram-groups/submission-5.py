from collections import defaultdict
class Solution:
    ## Hashmap Solution - 1
    # Time: O(n * k log(k))
    # Space: O(n * k)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for s in strs:
            charCount = [0] * 26
            for c in s:
                charCount[ord(c) - ord('a')] += 1
            # print(charCount)
            # print(tuple(charCount))
            anagramMap[tuple(charCount)].append(s)      # since list is unhashable, need to convert it to a tuple to be used as a key for a dictionary
        return list(anagramMap.values())


        
## Hashmap Solution - 2
# Time: O(n * k log(k))
# Space: O(n * k)
# - where n = number of strings in the input
#         m = max. length of a string in the input
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     anagrams = defaultdict(list)    # key: group of chars, val: list of anagrams
    #     for s in strs:
    #         anagrams["".join(sorted(list(s)))].append(s)
    #     return list(anagrams.values())
        