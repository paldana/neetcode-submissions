## Iterative Approach
"""
    We'll be building the words as we go through the available options from the 
    given string and add it to our list of results until we form a full word.

    First we'll extract all options from s, such that the options in the { } will 
    be considered as a single option
"""
from collections import defaultdict


class Solution:
    def expand(self, s: str) -> List[str]:
        expandedWords = [""]
        
        # Extract all options from s
        i = 0
        while i < len(s):
            options = []
        
            if s[i] != "{":
                options.append(s[i])
            else:
                while s[i] != "}":
                    # only extract the valid options within {}
                    if 'a' <= s[i] <= 'z':
                        options.append(s[i])
                    i += 1     
                # options.sort()
            i += 1  # point to the next valid option
        
            # begin forming the words
            newWord = []
            for word in expandedWords:
                for c in options:
                    newWord.append(word + c)
            expandedWords = newWord
            
        return expandedWords








