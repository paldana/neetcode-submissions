class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        anagrams = []
        hashmap = {}    # key: sorted string, value: list of anagrams

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in hashmap:
                hashmap[sorted_s] += [s]
            else:
                hashmap[sorted_s] = [s]
        
        for key, val in hashmap.items():
            anagrams.append(val)
        
        return anagrams

