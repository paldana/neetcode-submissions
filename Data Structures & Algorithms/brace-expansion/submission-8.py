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
        expandedWords = [""]    # will contain the word that will be built 
        i = 0

        # Build the words every time we extract a valid option
        while i < len(s):
            options = []      # resets every loop iteration to only have new options to be appended to the expandedWords

            if s[i] != "{":
                options.append(s[i])
            else:
                while s[i] != "}":
                    if "a" <= s[i] <= "z":      # only extract valid options from string
                        options.append(s[i])
                    i += 1
                
                # to ensure we're getting the options in {} in correct order, sort the options array
                options.sort()
            
            i += 1  # point to the next valid option 

            # build the words
            newWord = []
            for word in expandedWords:
                for c in options:
                    newWord.append(word + c)
            # update expandedWords with the newly built strings
            expandedWords = newWord
        
        return expandedWords

        






