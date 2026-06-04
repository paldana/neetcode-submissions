from collections import defaultdict

class Solution:
    def getSignature(self, s: str) -> str:
        count = [0] * 26
        for c in s:
            # The ord() function in Python is a built-in function that returns an 
            # integer representing the Unicode code point of a single character. 
            # It stands for "ordinal"; 
            # i.e. ord('a') = 97 (Standard ASCII value)
            count[ord(c) - ord('a')] += 1

        result = []
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])

        print(result)           # i.e. for "cat" the signature will look like = ['a', '1', 'c', '1', 't', '1']
        print(''.join(result))  #      ==> a1c1t1
        return ''.join(result)  # this will be used as the key to the hashmap to group the anagrams

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        groups = defaultdict(list)

        for s in strs:
            groups[self.getSignature(s)].append(s)

        result.extend(groups.values())

        return result

# without using sorted function
# Space and Time complexity: O(n * k); 
#   - where n is the length of strs and k is the length of the longest word 