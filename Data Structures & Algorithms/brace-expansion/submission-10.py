## Iteration Solution - alternative 
# Time complexity: O(N * 3^(N/7))
# Space Complexity: O(N * 3^(N/7))
# - where N is the lenght of string s
class Solution:
    def expand(self, s: str) -> List[str]:
        
        expandedWords = [""]
        i = 0
        while i < len(s):
            options = []
            
            ## extract available options for appending to existing words
            # If the first character is not '{', it means a single character
            if s[i] != "{":
                options.append(s[i])
            else:
                while s[i] != "}":
                    if 'a' <= s[i] <= 'z':
                        options.append(s[i])
                    i += 1
                options.sort()  # Sort the options alphabetically to adhere to lexicographical order requirement

            # increment i pointer to point to the next available option in the next iteration
            i += 1

            # go through the options retrieved and append them in in the existing words in the list 
            currentWords = []
            for word in expandedWords:
                for c in options:
                    currentWords.append(word + c)
            
            expandedWords = currentWords        # update the expandedWords list with newly updated list

        return expandedWords

