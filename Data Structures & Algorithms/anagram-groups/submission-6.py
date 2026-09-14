class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        anaMap = defaultdict(list)     # key: char signature, val: list of anagram words 

        for s in strs:
            charSignature = [0] * 26
            for c in s:
                charSignature[ord(c) - ord('a')] += 1
            anaMap[tuple(charSignature)].append(s)
        
        res = []
        for k, v in anaMap.items():
            res.append(v)
        
        return res

