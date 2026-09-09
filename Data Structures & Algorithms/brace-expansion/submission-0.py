class Solution:
    def expand(self, s: str) -> List[str]:
        
        expandedWords = [""]
        i = 0
        while i < len(s):
            options = []
            
            # extract available options for appending to existing words
            if s[i] != "{":
                options.append(s[i])
            else:
                while s[i] != "}":
                    if 'a' <= s[i] <= 'z':
                        options.append(s[i])
                    i += 1
                options.sort()

            # increment i pointer to point to the next available option in the next iteration
            i += 1

            # go through the options retrieved and append them in in the existing words in the list 
            currentWords = []
            for word in expandedWords:
                for c in options:
                    currentWords.append(word + c)
            
            expandedWords = currentWords

        return expandedWords

