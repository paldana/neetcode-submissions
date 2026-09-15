## Iterative Approach
"""
    We'll be building the words as we go through the available options from the 
    given string and add it to our list of results until we form a full word.

    First we'll extract all options from s, such that the options in the { } will 
    be considered as a single option
"""
class Solution:
    def expand(self, s: str) -> List[str]:
        expandedWords = [""]
        i = 0

        while i < len(s):
            options = []
            if s[i] != "{":
                options.append(s[i])
            else: 
                while s[i] != "}":
                    if "a" <= s[i] <= "z":
                        options.append(s[i])
                    i += 1
                options.sort()
            i += 1

            newWords = []
            for word in expandedWords:
                for c in options:
                    newWords.append(word + c)
            
            expandedWords = newWords
        
        return expandedWords

        
        

"""
Complexity Analysis - Neetbot
Time complexity: O(n⋅m⋅k)
Space complexity: O(m⋅k)

where
    n is the length of the input string s
    m is the number of expanded words generated
    k is the maximum number of options in any brace group
"""




